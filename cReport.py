""" 
cReport
Revised: Jan 9th 2006
Developer: Drunk Bum
Description: A reporting class to keep track of pass and failed steps. Designed
to work in conjunction with PAMIE.

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

import sys
sys.path.append(r'c:\python24\lib')

import time
import string
import datetime

class Report:
    showStatus = True               # Print the status of the steps.
    logHTML = True                  # Create the HTML Results file.
    stepsPassed = 0
    stepsFailed = 0
    
    def __init__(self):
        """ The class instantiation code.
        parameters:
            None
        returns:
            Nothing
        """
    
    def initialize(self):
        """ Initializes the reporting system.
            parameters:
                None
            returns:
                Nothing
        """
        if self.logHTML:
            fnum = open ("results.html", "w+")
            fnum.write ("<HTML><BODY bgcolor=\"#EBC573\"><HEAD>")
            fnum.write ("<STYLE>div.header { border-bottom: #BBBBFF 3px solid; } tr.hdr { background-color: #BBBBFF; } td { border-bottom: #BBBBFF 1px dashed; vertical-align=top} </STYLE></HEAD>")
            fnum.write ("<center><table width=\"100%\" bgcolor=\"#EEEAE1\">")
            fnum.write ("<tr><td colspan=2><b>PAMIE Test Results</b><br><i>Generated on " + str(datetime.datetime.now()) + "</i></td></tr>")
            fnum.write ("<tr class=\"hdr\"><td>&nbsp;</td><td><b>Step</b></td></tr>")
            fnum.close()

        self.stepsPassed = 0
        self.stepsFailed = 0

    def finalize(self):
        """ Finalizes the stats for the reporting system.
            parameters:
                None
            returns:
                Nothing
        """
        desc = str(self.stepsPassed) + " of " + str(self.stepsPassed + self.stepsFailed) + " steps passed."
        if self.showStatus: print "        - " + str(desc)
        if self.logHTML:
            fnum = open ("results.html", "a")
            fnum.write ("<tr><td>&nbsp;</td><td id=\"done\">" + str(desc) + "</td></tr>")
            fnum.write ("</table></center></BODY></HTML>")

    def status(self, description):
        """ Reports a status to the reporting system.
            parameters:
                description     - The text status to report.
            returns:
                Nothing
        """
        if self.logHTML:
            self.writeHTMLLog ("<tr><td width=30>&nbsp;</td><td>" + str(description) + "</td></tr>")
        if self.showStatus: print "        - " + str(description)

    def stepPass(self, name, actual):
        """ Reports a passed step.
            parameters:
                name        - Name of the step.
                actual      - The actual results of the step.
            returns:
                Nothing
        """
        desc = name + "  [" + str(actual) + "]"
        if self.logHTML:
            self.writeHTMLLog ("<tr><td width=30><img src=""checkMark.ico""></td><td>" + str(desc) + "</td></tr>")
        if self.showStatus: print "   PASS " + str(desc)
        self.stepsPassed += 1
        
    def stepFail(self, name, actual, expected):
        """ Reports a failed step.
            parameters:
                name        - Name of the step.
                actual      - The actual results of the step.
                expected    - The expected results of the step.
            returns:
                Nothing
        """
        desc = name + " - Result was [" + str(actual) + "] instead of [" + str(expected) + "]"
        if self.logHTML:
            self.writeHTMLLog ("<tr><td width=30><img src=\"x.ico\"></td><td>" + str(desc) + "</td></tr>")
        if self.showStatus: print "** FAIL " + str(desc)
        self.stepsFailed += 1

    def verify(self, name, actual, expected=True):
        """ Verifies that a step passes or fails.  Basically like the assert command,
            but automatically records the results to the reporting system.
            parameters:
                name          - Name of the step.
                actual        - The actual results of the step.
                [expected]    - The expected boolean result.  True by default.
            returns:
                Nothing
        """
        if actual == expected:
            self.stepPass (name, actual)
        else:
            self.stepFail (name, actual, expected)

    def writeHTMLLog(self, text):
        """ Writes text directly to the HTML log.
            parameters:
                text        - The text to write.
            returns:
                Nothing
        """
        fnum = open ("results.html", "a+")
        fnum.write (str(text) + "\n")
        fnum.close()
