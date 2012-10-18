""" 
writeDocs.py
Revised: Jan 9th 2006
Developer: Drunk Bum
Description: A script to create HTML documention of the PAMIE classes.  The functions
should be documented in the following format for the documentation to generated
correctly:
    xxx represents the 3 double quotes:
        xxx Description of the function.
            ...
            more lines of description if needed
            parameters:
                param1   - Each parameter should be listed on a separate line.
                param2   - Each parameter should have a hyphen followed by a description
            returns:
                a description of what the function returns.
            examples:
                the examples are optional, but you could list them if you want.
        xxx


Licence: GNU General Public License (GPL)
This software is provided 'as-is', without any express or implied warranty.
In no event will the authors be held liable for any damages arising from the use of this software.

Permission is granted to anyone to use this software for any purpose,
including commercial applications, and to alter it and redistribute it freely, subject to the following restrictions:

1. The origin of this software must not be misrepresented; you must not claim that you wrote the original software.
   If you use this software in a product, an acknowledgment in the product documentation would be appreciated but is not required.
2. Altered source versions must be plainly marked as such, and must not be misrepresented as being the original software.
3. This notice may not be removed or altered from any source distribution.
"""

import os, sys
import shutil
import string
import time
import datetime
import traceback

# Classes to document
import cPAMIE
import cModalPopUp
import cReport

def getValue(obj, attr):
    try:
        return getattr(obj, attr)
    except:
        return ""
    
def classCreateFile(fileName):
    shutil.copyfile (fullPathName + "ref_classFunctions.tpl", fullPathName + fileName) 

def classEndFile(fileName):
    fnum = open (fullPathName + fileName, "a")
    fnum.write ("<br><div class=\"ftrMain\"><table width=\"100%\"><tr><td align=center valign=top><font size=2 color=\"#000060\">PAMIE documentation last updated on " + str(datetime.datetime.now()) + "</font></td></tr></table></div>")
    fnum.write ("</div></BODY></HTML>")
    fnum.close()
    
def classGetDescription (funcName, descLines):
    val = ""
    try:
        for line in descLines:
            if string.find(line, "parameters:") >= 0:
                break
            else:
                val += line
    except:
        print "** Error with documentation for " + funcName + " function."
    
    return val

def classGetParameters (funcName, descLines):
    paramDef = "<br><table>"
    funcDef = funcName + " (";

    try:
        start = False
        firstParam = True
        for line in descLines:
            if start:
                if string.find(line, "returns:") >= 0: break;
                
                if firstParam:
                    firstParam = False;
                else:
                    funcDef += ", ";
        
                pValues = line.split ("-")
                pName = pValues[0].strip()
                if len(pValues) > 1:
                    pDesc = pValues[1].strip()
                else:
                    pName = ""
                    pDesc = pValues[0].strip()                    
                
                if pDesc <> "None":
                    funcDef += pName
                    paramDef += "<tr><td width=100 class=\"attribute\">" + pName + "</td><td class=\"value\">" + pDesc + "</td></tr>"
            else:
                if string.find(line, "parameters:") >= 0:
                    start = True

        funcDef += ")<br>"
        paramDef += "</table>"
        if pDesc <> "None":
            return funcDef + paramDef
        else:
            return funcDef

    except:
        print "** Error with documentation for " + funcName + " function."

def classGetReturn (funcName, descLines):
    val = ""
    start = False

    try:
        for line in descLines:
            if start:
                if string.find(line, "examples:") >= 0: break;
                val += line
            else:
                if string.find(line, "returns:") >= 0:
                    start = True
    except:
        print "** Error with documentation for " + funcName + " function."
    
    return val

def classGetExamples (funcName, descLines):
    val = ""
    start = False

    try:
        for line in descLines:
            if start:
                val += line
            else:
                if string.find(line, "examples:") >= 0:
                    start = True
    except:
        print "** Error with documentation for " + funcName + " function."
    
    if start:
        return "<br><br>" + classGetSection ("lightbulb.gif", "Examples:") + val
    else:
        return ""

def classWriteFunction(fileName, funcName, desc):
    try:
        if not desc:
            print "** No documentation for " + funcName + " function."
            return
        
        descLines = desc.split("\n")
    
        fnum = open (fullPathName + fileName, "a")
        fnum.write ("<div id=\"" + funcName + "\" class=\"h4\">" + funcName + "() Function</div>")
        fnum.write (classGetDescription (funcName, descLines) + "<br><br><div class=\"funcindent\">")
            
        # Get parameters
        fnum.write (classGetSection ("Parameter.gif", "Parameters:"))
        fnum.write (classGetParameters (funcName, descLines))
        
        # Get return
        fnum.write ("<br>" + classGetSection ("ArrowGreen.gif", "Returns:"))
        fnum.write (classGetReturn(funcName, descLines))
    
        # Any examples?
        examples = classGetExamples(funcName, descLines)
        if examples:
            fnum.write (examples)
            
        fnum.write ("</div><br><br>")
        fnum.close()

    except:
        (ErrorType,ErrorValue,ErrorTB)=sys.exc_info()
        print sys.exc_info()
        traceback.print_exc(ErrorTB)
    
def classGetSection(image, text):
    return ("<div class=\"funcsec\"><table cellpadding=0 cellspacing=0><td valign=middle><img height=16 width=16 src=\"Images/" + image + "\" border=0></td><td valign=middle><div style=\"padding-top: 2px;\">&nbsp;&nbsp;<b>" + text + "</b></div></td></tr></table></div>")
    
def indexCreateFile():
    shutil.copyfile (fullPathName + "ref_indexSide.tpl", fullPathName + "ref_indexSide.html") 

def indexEndFile():
    indexWriteFile ("</div></BODY></HTML>")
    
def indexWriteFile(text):
    fnum = open (fullPathName + "ref_indexSide.html", "a")
    fnum.write (text)
    fnum.close()

def indexWriteHeader(hdr, link):
    indexWriteFile ("<a class=\"menuHead\" href=\"" + link + "\" target=\"main\">" + hdr + "</a><br>")
    
def indexWriteFunction(hdr, link):
    indexWriteFile ("<a class=\"menuOption\" href=\"" + link + "\" target=\"main\">" + hdr + "</a><br>")

def classDocument(pClass, funcFile, indexHdr):
    try:
        print "Documenting " + indexHdr + " class..."
        indexWriteHeader (indexHdr, funcFile)
        classCreateFile(funcFile)
        
        for func in dir(pClass):
            if func[0:1]!='_':
                docs = getValue(pClass, func)
                if docs:
                    name = getValue (docs, "__name__")
                    if name: 
                        desc = getValue (docs, "__doc__")
                        indexWriteFunction (name, funcFile + "#" + name)
                        classWriteFunction (funcFile, name, desc)

        indexWriteFile ("<br>")
        classEndFile (funcFile)

    except:
        (ErrorType,ErrorValue,ErrorTB)=sys.exc_info()
        print sys.exc_info()
        traceback.print_exc(ErrorTB)
        
def writeDocs():
    indexCreateFile()
    classDocument (cPAMIE.PAMIE, "ref_pamieFunctions.html", "PAMIE Functions")
    classDocument (cModalPopUp.handlePopup, "ref_ModalPopUpFunctions.html", "cModalPopUp Functions")
    classDocument (cReport.Report, "ref_Report.html", "cReport Functions")
    indexEndFile()
    
# Init
pathName = os.path.dirname(sys.argv[0])
fullPathName = '%s\\docs\\'%os.path.abspath(pathName)

# Make them docs
print "Generating Documentation..."
writeDocs()
print "Done!"
