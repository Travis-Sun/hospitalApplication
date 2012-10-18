import cPAMIE
import cReport
import cModalPopUp
import winGuiAuto
import time
import os, sys

# Initialize our stuff.
ie = cPAMIE.PAMIE()
rep = cReport.Report()
wga = winGuiAuto

# Get our path names
pathName = os.path.dirname(sys.argv[0])
fullPathName = '%s\\buildcert\\'%os.path.abspath(pathName)

# Run the Pamie build certification tests
rep.initialize()
ie.colorHighlight = "aqua"
ie.navigate(fullPathName + 'index.html')
ie.showDebugging = False
rep.status ("It's PAMIE Time!")

def goGoGadgetTests():
    #-----------------------------------------------------------------------------
    rep.status ("Validate elements in a form...")
    #-----------------------------------------------------------------------------
    ie.formName = "frmFruit"
    
    # Buttons
    rep.status ("Verify the button functions")
    rep.verify ("buttonExists for real", ie.buttonExists ("FruitSave"), True)
    rep.verify ("buttonExists really doesn't", ie.buttonExists ("Faker"), False)
    rep.verify ("buttonClick", ie.buttonClick ("FruitSave"), True)
    rep.verify ("buttonClick Index", ie.buttonClick (0), True)
    myButton = ie.buttonGet ("FruitSave")
    rep.verify ("buttonGet retrieved button", myButton.name, "FruitSave")
    rep.verify ("buttonGetValue retrieved value", ie.buttonGetValue ("FruitSave", "value"), "Save")
    rep.verify ("buttonImageClick", ie.buttonImageClick ("FruitImage"), True)
    
    bForm = False               # A button on the form
    bNotForm = False            # A button outside the form
    myValues = ie.buttonsGet()
    for my in myValues[:]:
        if my.Name == "FruitSave":
            bForm = True
        elif my.Name == "VegSave":
            bNotForm = True
    rep.verify ("buttonsGet found button in the form", bForm)
    rep.verify ("buttonsGet did not find button outside the form", bNotForm, False)
    
    bForm = False               # A button on the form
    bNotForm = False            # A button outside the form
    myValues = ie.buttonsGetValue("name")
    for my in myValues[:]:
        if my == "FruitSave":
            bForm = True
        elif my == "VegSave":
            bNotForm = True
    rep.verify ("buttonsGetValue found button in the form", bForm)
    rep.verify ("buttonsGetValue did not find button outside the form", bNotForm, False)
    
    # Checkboxes
    rep.status ("Verify the checkbox functions")
    rep.verify ("checkBoxExists for real", ie.checkBoxExists ("chkFruitRipe"), True)
    rep.verify ("checkBoxExists really doesn't", ie.checkBoxExists ("Faker"), False)
    rep.verify ("checkBoxSet", ie.checkBoxSet ("chkFruitRipe", 1), True)
    mycheckBox = ie.checkBoxGet ("chkFruitRipe")
    rep.verify ("checkBoxGet retrieved checkbox", mycheckBox.name, "chkFruitRipe")
    rep.verify ("checkBoxGetValue retrieved value", ie.checkBoxGetValue ("chkFruitRipe", "checked"), True)
    
    myValues = ie.checkBoxesGetChecked("chkFruitRipe")
    bFound = False
    for my in myValues[:]:
        if my.value == "Ripe Fruit":
            bFound = True
    rep.verify ("checkBoxesGetChecked did not find the checked box", bFound)
    
    bForm = False               # A checkBox on the form
    bNotForm = False            # A checkBox outside the form
    myValues = ie.checkBoxesGet()
    for my in myValues[:]:
        if my.Name == "chkFruitRipe":
            bForm = True
        elif my.Name == "chkVegRipe":
            bNotForm = True
    rep.verify ("checkBoxesGet found checkbox in the form", bForm)
    rep.verify ("checkBoxesGet did not find checkbox outside the form", bNotForm, False)
    
    bForm = False               # A checkBox on the form
    bNotForm = False            # A checkBox outside the form
    myValues = ie.checkBoxesGetValue("name")
    for my in myValues[:]:
        if my == "chkFruitRipe":
            bForm = True
        elif my == "chkVegRipe":
            bNotForm = True
    rep.verify ("checkBoxesGetValue found checkbox in the form", bForm)
    rep.verify ("checkBoxesGetValue did not find checkbox outside the form", bNotForm, False)
    
    # Divs
    rep.status ("Verify the div functions")
    rep.verify ("divExists for real", ie.divExists ("divForm"), True)
    rep.verify ("divExists really doesn't", ie.divExists ("Faker"), False)
    myDiv = ie.divGet ("divForm")
    rep.verify ("divGet retrieved div", myDiv.id, "divForm")
    rep.verify ("divGetValue retrieved value", ie.divGetValue ("divForm", "id"), "divForm")
    
    bForm = False               # A div on the form
    bNotForm = False            # A div outside the form
    myValues = ie.divsGet()
    for my in myValues[:]:
        if my.id == "divForm":
            bForm = True
        elif my.id == "divNoForm":
            bNotForm = True
    rep.verify ("divsGet found div in the form", bForm)
    rep.verify ("divsGet did not find div outside the form", bNotForm, False)
    
    bForm = False               # A div on the form
    bNotForm = False            # A div outside the form
    myValues = ie.divsGetValue("id")
    for my in myValues[:]:
        if my == "divForm":
            bForm = True
        elif my == "divNoForm":
            bNotForm = True
    rep.verify ("divsGetValue found div in the form", bForm)
    rep.verify ("divsGetValue did not find div outside the form", bNotForm, False)
    
    # Images
    rep.status ("Verify the image functions")
    rep.verify ("imageExists for real", ie.imageExists ("FruitImage"), True)
    rep.verify ("imageExists really doesn't", ie.imageExists ("Faker"), False)
    rep.verify ("imageClick", ie.imageClick ("FruitImage"), True)
    rep.verify ("imageClick Index", ie.imageClick (0), True)
    myimage = ie.imageGet ("FruitImage")
    rep.verify ("imageGet retrieved image", myimage.name, "FruitImage")
    rep.verify ("imageGetValue retrieved value", ie.imageGetValue ("FruitImage", "name"), "FruitImage")
    
    bForm = False               # A image on the form
    bNotForm = False            # A image outside the form
    myValues = ie.imagesGet()
    for my in myValues[:]:
        if my.Name == "FruitImage":
            bForm = True
        elif my.Name == "VegImage":
            bNotForm = True
    rep.verify ("imagesGet found image in the form", bForm)
    rep.verify ("imagesGet did not find image outside the form", bNotForm, False)
    
    bForm = False               # A image on the form
    bNotForm = False            # A image outside the form
    myValues = ie.imagesGetValue("name")
    for my in myValues[:]:
        if my == "FruitImage":
            bForm = True
        elif my == "VegImage":
            bNotForm = True
    rep.verify ("imagesGetValue found image in the form", bForm)
    rep.verify ("imagesGetValue did not find image outside the form", bNotForm, False)
    
    # Input Elements
    bForm = False               # A element on the form
    bNotForm = False            # A element outside the form
    myValues = ie.inputElementsGet()
    for my in myValues[:]:
        if my.name == "txtFruitColor":
            bForm = True
        elif my.name == "txtVegColor":
            bNotForm = True
    rep.verify ("inputElementsGet found element in the form", bForm)
    rep.verify ("inputElementsGet did not find element outside the form", bNotForm, False)
    
    # Links
    rep.status ("Verify the link functions")
    rep.verify ("linkExists for real", ie.linkExists ("Refresh"), True)
    rep.verify ("linkExists really doesn't", ie.linkExists ("Faker"), False)
    rep.verify ("linkClick", ie.linkClick ("Refresh"), True)
    rep.verify ("linkClick Index", ie.linkClick (1), True)
    mylink = ie.linkGet ("Refresh")
    rep.verify ("linkGet retrieved link", mylink.innerText, "Refresh")
    rep.verify ("linkGetValue retrieved value", ie.linkGetValue ("Refresh", "innerText"), "Refresh")
    
    bForm = False               # A link on the form
    bNotForm = False            # A link outside the form
    myValues = ie.linksGet()
    for my in myValues[:]:
        if my.innerText == "Refresh":
            bForm = True
        elif my.innerText == "Clicky Clicky":
            bNotForm = True
    rep.verify ("linksGet found link in the form", bForm)
    rep.verify ("linksGet did not find link outside the form", bNotForm, False)
    
    bForm = False               # A link on the form
    bNotForm = False            # A link outside the form
    myValues = ie.linksGetValue("innerText")
    for my in myValues[:]:
        if my == "Refresh":
            bForm = True
        elif my == "Clicky Clicky":
            bNotForm = True
    rep.verify ("linksGetValue found link in the form", bForm)
    rep.verify ("linksGetValue did not find link outside the form", bNotForm, False)
    
    # Textareas
    rep.status ("Verify the textarea functions")
    rep.verify ("textAreaExists for real", ie.textAreaExists ("txtFruitComments"), True)
    rep.verify ("textAreaExists really doesn't", ie.textAreaExists ("Faker"), False)
    rep.verify ("textAreaSet", ie.textAreaSet ("txtFruitComments", "Fruits taste better then veggies!"), True)
    myTextArea = ie.textAreaGet ("txtFruitComments")
    rep.verify ("textAreaGet retrieved textarea", myTextArea.innerText, "Fruits taste better then veggies!")
    rep.verify ("textAreaGetValue retrieved value", ie.textAreaGetValue ("txtFruitComments", "id"), "txtFruitComments")
    
    bForm = False               # A textarea on the form
    bNotForm = False            # A textarea outside the form
    myValues = ie.textAreasGet()
    for my in myValues[:]:
        if my.id == "txtFruitComments":
            bForm = True
        elif my.id == "txtVegComments":
            bNotForm = True
    rep.verify ("textareaGet found textarea in the form", bForm)
    rep.verify ("textareaGet did not find textarea outside the form", bNotForm, False)
    
    bForm = False               # A textarea on the form
    bNotForm = False            # A textarea outside the form
    myValues = ie.textAreasGetValue("id")
    for my in myValues[:]:
        if my == "txtFruitComments":
            bForm = True
        elif my == "txtVegComments":
            bNotForm = True
    rep.verify ("textareaGetValue found textarea in the form", bForm)
    rep.verify ("textareaGetValue did not find textarea outside the form", bNotForm, False)
    
    # Textboxes
    rep.status ("Verify the textbox functions")
    rep.verify ("textBoxExists for real", ie.textBoxExists ("txtFruitWeight"), True)
    rep.verify ("textBoxExists really doesn't", ie.textBoxExists ("Faker"), False)
    rep.verify ("textboxeset", ie.textBoxSet ("txtFruitWeight", "10"), True)
    myTextBox = ie.textBoxGet ("txtFruitWeight")
    rep.verify ("textboxGet retrieved textbox", myTextBox.value, "10")
    rep.verify ("textboxGetValue retrieved value", ie.textBoxGetValue ("txtFruitWeight", "name"), "txtFruitWeight")
    
    bForm = False               # A textbox on the form
    bNotForm = False            # A textbox outside the form
    myValues = ie.textBoxesGet()
    for my in myValues[:]:
        if my.name == "txtFruitWeight":
            bForm = True
        elif my.name == "txtVegWeight":
            bNotForm = True
    rep.verify ("textboxGet found textbox in the form", bForm)
    rep.verify ("textboxGet did not find textbox outside the form", bNotForm, False)
    
    bForm = False               # A textbox on the form
    bNotForm = False            # A textbox outside the form
    myValues = ie.textBoxesGetValue("name")
    for my in myValues[:]:
        if my == "txtFruitWeight":
            bForm = True
        elif my == "txtVegWeight":
            bNotForm = True
    rep.verify ("textboxGetValue found textbox in the form", bForm)
    rep.verify ("textboxGetValue did not find textbox outside the form", bNotForm, False)
    
    #-----------------------------------------------------------------------------
    rep.status ("Validate elements NOT in a form...")
    #-----------------------------------------------------------------------------
    ie.formName = None
    
    # Buttons
    rep.status ("Verify the button functions")
    rep.verify ("buttonExists for real", ie.buttonExists ("VegSave"), True)
    rep.verify ("buttonExists really doesn't", ie.buttonExists ("Faker"), False)
    rep.verify ("buttonClick", ie.buttonClick ("VegSave"), True)
    rep.verify ("buttonClick Index", ie.buttonClick (0), True)
    myButton = ie.buttonGet ("VegSave")
    rep.verify ("buttonGet retrieved button", myButton.name, "VegSave")
    rep.verify ("buttonGetValue retrieved value", ie.buttonGetValue ("VegSave", "value"), "Save")
    rep.verify ("buttonImageClick", ie.buttonImageClick ("VegImage"), True)
    
    bForm = False               # A button on the form
    bNotForm = False            # A button outside the form
    myValues = ie.buttonsGet()
    for my in myValues[:]:
        if my.Name == "FruitSave":
            bForm = True
        elif my.Name == "VegSave":
            bNotForm = True
    rep.verify ("buttonsGet found button in the form", bForm)
    rep.verify ("buttonsGet did not find button outside the form", bNotForm)
    
    bForm = False               # A button on the form
    bNotForm = False            # A button outside the form
    myValues = ie.buttonsGetValue("name")
    for my in myValues[:]:
        if my == "FruitSave":
            bForm = True
        elif my == "VegSave":
            bNotForm = True
    rep.verify ("buttonsGetValue found button in the form", bForm)
    rep.verify ("buttonsGetValue did not find button outside the form", bNotForm)
    
    # Checkboxes
    rep.status ("Verify the checkbox functions")
    rep.verify ("checkBoxExists for real", ie.checkBoxExists ("chkVegRipe"), True)
    rep.verify ("checkBoxExists really doesn't", ie.checkBoxExists ("Faker"), False)
    rep.verify ("checkBoxSet", ie.checkBoxSet ("chkVegRipe", 1), True)
    mycheckBox = ie.checkBoxGet ("chkVegRipe")
    rep.verify ("checkBoxGet retrieved checkbox", mycheckBox.name, "chkVegRipe")
    rep.verify ("checkBoxGetValue retrieved value", ie.checkBoxGetValue ("chkVegRipe", "checked"), True)
    
    myValues = ie.checkBoxesGetChecked("chkVegRipe")
    bFound = False
    for my in myValues[:]:
        if my.value == "Ripe Vegetables":
            bFound = True
    rep.verify ("checkBoxesGetChecked did not find the checked box", bFound)
    
    bForm = False               # A checkBox on the form
    bNotForm = False            # A checkBox outside the form
    myValues = ie.checkBoxesGet()
    for my in myValues[:]:
        if my.Name == "chkFruitRipe":
            bForm = True
        elif my.Name == "chkVegRipe":
            bNotForm = True
    rep.verify ("checkBoxesGet found checkbox in the form", bForm)
    rep.verify ("checkBoxesGet did find checkbox outside the form", bNotForm)
    
    bForm = False               # A checkBox on the form
    bNotForm = False            # A checkBox outside the form
    myValues = ie.checkBoxesGetValue("name")
    for my in myValues[:]:
        if my == "chkFruitRipe":
            bForm = True
        elif my == "chkVegRipe":
            bNotForm = True
    rep.verify ("checkBoxesGetValue found checkbox in the form", bForm)
    rep.verify ("checkBoxesGetValue did find checkbox outside the form", bNotForm)
    
    # Divs
    rep.status ("Verify the div functions")
    rep.verify ("divExists for real", ie.divExists ("divNoForm"), True)
    rep.verify ("divExists really doesn't", ie.divExists ("Faker"), False)
    myDiv = ie.divGet ("divNoForm")
    rep.verify ("divGet retrieved div", myDiv.id, "divNoForm")
    rep.verify ("divGetValue retrieved value", ie.divGetValue ("divNoForm", "id"), "divNoForm")
    
    bForm = False               # A div on the form
    bNotForm = False            # A div outside the form
    myValues = ie.divsGet()
    for my in myValues[:]:
        if my.id == "divForm":
            bForm = True
        elif my.id == "divNoForm":
            bNotForm = True
    rep.verify ("divsGet found div in the form", bForm)
    rep.verify ("divsGet did not find div outside the form", bNotForm)
    
    bForm = False               # A div on the form
    bNotForm = False            # A div outside the form
    myValues = ie.divsGetValue("id")
    for my in myValues[:]:
        if my == "divForm":
            bForm = True
        elif my == "divNoForm":
            bNotForm = True
    rep.verify ("divsGetValue found div in the form", bForm)
    rep.verify ("divsGetValue did not find div outside the form", bNotForm)
    
    # Forms
    rep.status ("Verify the form functions")
    rep.verify ("formExists for real", ie.formExists ("frmFruit"), True)
    rep.verify ("formExists really doesn't", ie.formExists ("Faker"), False)
    
    myForm = ie.formGet ("frmFruit")
    rep.verify ("formGet retrieved form", myForm.name, "frmFruit")
    rep.verify ("formGetValue retrieved value", ie.formGetValue ("frmFruit", "name"), "frmFruit")
    
    bFound = False 
    myValues = ie.formsGet()
    for my in myValues[:]:
        if my.Name == "frmFruit":
            bFound = True
    rep.verify ("formsGet found form", bFound)
    
    bFound = False 
    myValues = ie.formsGetValue("name")
    for my in myValues[:]:
        if my == "frmFruit":
            bFound = True
    rep.verify ("formsGetValue found form", bFound)
    
    bFound = False 
    bFoundHidden = False 
    myValues = ie.formGetControlNames()
    for my in myValues[:]:
        if my == "txtFruitColor":
            bFound = True
        if my == "FruitCost":
            bFoundHidden = True
    rep.verify ("formGetControlNames found visible controls", bFound)
    rep.verify ("formGetControlNames found hidden controls", bFoundHidden)
    
    bFound = False 
    bFoundHidden = False 
    myValues = ie.formGetVisibleControlNames()
    for my in myValues[:]:
        if my == "txtFruitColor":
            bFound = True
        if my == "FruitCost":
            bFoundHidden = True
    rep.verify ("formGetControlNames found visible controls", bFound)
    rep.verify ("formGetControlNames found hidden controls", bFoundHidden, False)

    # Frames
    if ie.frameName:
        rep.status ("Verify the frame functions")
        rep.verify ("frameExists for real", ie.frameExists ("left"), True)
        rep.verify ("frameExists really doesn't", ie.frameExists ("Faker"), False)
        
        myFrame = ie.frameGet ("left")
        rep.verify ("frameGet retrieved frame", myFrame.name, "left")
        rep.verify ("frameGetValue retrieved value", ie.frameGetValue ("left", "name"), "left")

        bFound = False 
        myValues = ie.framesGetValue("name")
        for my in myValues[:]:
            if my == "left":
                bFound = True
        rep.verify ("frameGetValue found frame", bFound)

    # Images
    rep.status ("Verify the image functions")
    rep.verify ("imageExists for real", ie.imageExists ("VegImage"), True)
    rep.verify ("imageExists really doesn't", ie.imageExists ("Faker"), False)
    rep.verify ("imageClick", ie.imageClick ("VegImage"), True)
    rep.verify ("imageClick Index", ie.imageClick (0), True)
    myimage = ie.imageGet ("VegImage")
    rep.verify ("imageGet retrieved image", myimage.name, "VegImage")
    rep.verify ("imageGetValue retrieved value", ie.imageGetValue ("VegImage", "name"), "VegImage")
    
    bForm = False               # A image on the form
    bNotForm = False            # A image outside the form
    myValues = ie.imagesGet()
    for my in myValues[:]:
        if my.Name == "FruitImage":
            bForm = True
        elif my.Name == "VegImage":
            bNotForm = True
    rep.verify ("imagesGet found image in the form", bForm)
    rep.verify ("imagesGet did not find image outside the form", bNotForm)
    
    bForm = False               # A image on the form
    bNotForm = False            # A image outside the form
    myValues = ie.imagesGetValue("name")
    for my in myValues[:]:
        if my == "FruitImage":
            bForm = True
        elif my == "VegImage":
            bNotForm = True
    rep.verify ("imagesGetValue found image in the form", bForm)
    rep.verify ("imagesGetValue did not find image outside the form", bNotForm)
    
    # Input Elements
    bForm = False               # A element on the form
    bNotForm = False            # A element outside the form
    myValues = ie.inputElementsGet()
    for my in myValues[:]:
        if my.name == "txtFruitColor":
            bForm = True
        elif my.name == "txtVegColor":
            bNotForm = True
    rep.verify ("inputElementsGet found element in the form", bForm)
    rep.verify ("inputElementsGet did not find element outside the form", bNotForm)
    
    # Links
    rep.status ("Verify the link functions")
    rep.verify ("linkExists for real", ie.linkExists ("Clicky Clicky"), True)
    rep.verify ("linkExists really doesn't", ie.linkExists ("Faker"), False)
    rep.verify ("linkClick", ie.linkClick ("Clicky Clicky"), True)
    rep.verify ("linkClick Index", ie.linkClick (1), True)
    mylink = ie.linkGet ("Clicky Clicky")
    rep.verify ("linkGet retrieved link", mylink.innerText, "Clicky Clicky")
    rep.verify ("linkGetValue retrieved value", ie.linkGetValue ("Clicky Clicky", "innerText"), "Clicky Clicky")
    
    bForm = False               # A link on the form
    bNotForm = False            # A link outside the form
    myValues = ie.linksGet()
    for my in myValues[:]:
        if my.innerText == "Refresh":
            bForm = True
        elif my.innerText == "Clicky Clicky":
            bNotForm = True
    rep.verify ("linksGet found link in the form", bForm)
    rep.verify ("linksGet did not find link outside the form", bNotForm)
    
    bForm = False               # A link on the form
    bNotForm = False            # A link outside the form
    myValues = ie.linksGetValue("innerText")
    for my in myValues[:]:
        if my == "Refresh":
            bForm = True
        elif my == "Clicky Clicky":
            bNotForm = True
    rep.verify ("linksGetValue found link in the form", bForm)
    rep.verify ("linksGetValue did not find link outside the form", bNotForm)
    
    # Listboxes
    myBox = ie.listBoxGet ("selVegType")
    rep.verify ("listBoxGet", myBox.name, "selVegType")
    
    myValues = ie.listBoxGetOptions ("selVegType")
    bFound = False
    for my in myValues[:]:
        if my == "Lettuce":
            bFound = True 
    rep.verify ("listBoxGetOptions found the options", bFound)
    
    ie.listBoxSelect ("selVegType", "Lettuce")
    rep.verify ("listBoxGetSelected found the options", ie.listBoxGetSelected ("selVegType"), "Lettuce")
    
    # Tables
    rep.status ("Verify the table functions")
    rep.status (ie.tableGetData ("tNumbers"))
    rep.verify ("tableCellExists for real", ie.tableCellExists("tNumbers", "five"))
    rep.verify ("tableCellExists not for real", ie.tableCellExists("tNumbers", "fifty"), False)
    
    myRow = ["four", "five", "six"]
    rep.verify ("tableRowGetIndex for real", ie.tableRowGetIndex("tNumbers", myRow), 1)
    rep.verify ("tableRowExists for real", ie.tableRowExists("tNumbers", myRow))
    myRow = ["four", "*", "six"]
    rep.verify ("tableRowExists for real", ie.tableRowExists("tNumbers", myRow))
    myRow = ["four", "seven", "six"]
    rep.verify ("tableRowExists not for real", ie.tableRowExists("tNumbers", myRow), False)

    # Textareas
    rep.status ("Verify the textarea functions")
    rep.verify ("textAreaExists for real", ie.textAreaExists ("txtVegComments"), True)
    rep.verify ("textAreaExists really doesn't", ie.textAreaExists ("Faker"), False)
    rep.verify ("textAreaSet", ie.textAreaSet ("txtVegComments", "Eat your veggies!"), True)
    myTextArea = ie.textAreaGet ("txtVegComments")
    rep.verify ("textAreaGet retrieved textarea", myTextArea.innerText, "Eat your veggies!")
    rep.verify ("textAreaGetValue retrieved value", ie.textAreaGetValue ("txtVegComments", "id"), "txtVegComments")
    
    bForm = False               # A textarea on the form
    bNotForm = False            # A textarea outside the form
    myValues = ie.textAreasGet()
    for my in myValues[:]:
        if my.id == "txtFruitComments":
            bForm = True
        elif my.id == "txtVegComments":
            bNotForm = True
    rep.verify ("textareaGet found textarea in the form", bForm)
    rep.verify ("textareaGet did not find textarea outside the form", bNotForm)
    
    bForm = False               # A textarea on the form
    bNotForm = False            # A textarea outside the form
    myValues = ie.textAreasGetValue("id")
    for my in myValues[:]:
        if my == "txtFruitComments":
            bForm = True
        elif my == "txtVegComments":
            bNotForm = True
    rep.verify ("textareaGetValue found textarea in the form", bForm)
    rep.verify ("textareaGetValue did not find textarea outside the form", bNotForm)
    
    # Textboxes
    rep.status ("Verify the textbox functions")
    rep.verify ("textBoxExists for real", ie.textBoxExists ("txtVegWeight"), True)
    rep.verify ("textBoxExists really doesn't", ie.textBoxExists ("Faker"), False)
    rep.verify ("textboxeset", ie.textBoxSet ("txtVegWeight", "10"), True)
    myTextBox = ie.textBoxGet ("txtVegWeight")
    rep.verify ("textboxGet retrieved textbox", myTextBox.value, "10")
    rep.verify ("textboxGetValue retrieved value", ie.textBoxGetValue ("txtVegWeight", "name"), "txtVegWeight")
    
    bForm = False               # A textbox on the form
    bNotForm = False            # A textbox outside the form
    myValues = ie.textBoxesGet()
    for my in myValues[:]:
        if my.name == "txtFruitWeight":
            bForm = True
        elif my.name == "txtVegWeight":
            bNotForm = True
    rep.verify ("textboxGet found textbox in the form", bForm)
    rep.verify ("textboxGet did not find textbox outside the form", bNotForm)
    
    bForm = False               # A textbox on the form
    bNotForm = False            # A textbox outside the form
    myValues = ie.textBoxesGetValue("name")
    for my in myValues[:]:
        if my == "txtFruitWeight":
            bForm = True
        elif my == "txtVegWeight":
            bNotForm = True
    rep.verify ("textboxGetValue found textbox in the form", bForm)
    rep.verify ("textboxGetValue did not find textbox outside the form", bNotForm)
    
    #-----------------------------------------------------------------------------
    # print "Validate misc functions"
    #-----------------------------------------------------------------------------
    """
    TODO:
    rep.status (ie.bodyGetValue ("innerHTML"))
    rep.status (ie.bodyGetValue ("outerHTML"))
    
    print ie.dateGet()
    print ie.dayGetNext()
    
    print ie.randomDigits(5)
    print ie.randomString(5)
    """

def runFrameTests():
    rep.status ("Verify the frame functions")
    rep.verify ("frameExists for real", ie.frameExists ("main"), True)
    rep.verify ("frameExists really doesn't", ie.frameExists ("Faker"), False)
    
    myFrame = ie.frameGet ("left")
    rep.verify ("frameGet retrieved frame", myFrame.name, "left")
    rep.verify ("frameGetValue retrieved value", ie.frameGetValue ("left", "name"), "left")
    
    bFound = False 
    myValues = ie.framesGetValue("name")
    for my in myValues[:]:
        if my == "left":
            bFound = True
    rep.verify ("frameGetValue found frame", bFound)

def runModalTests():
    #-----------------------------------------------------------------------------
    # print "Validate the modal pop ups"
    #-----------------------------------------------------------------------------
    rep.status ("Verify the modal pop up functions")
    ie.linkClick ("Modal Popups")
    testFile = fullPathName + "index.html"
    location = ie.locationURL()
    
    # Click on the browse button to bring up the choose file dialog.
    rep.status ("Testing Download dialog")
    ie.formName = "installForm"
    btnname = "install"
    dialogThread = cModalPopUp.handlePopup("ChooseFile", testFile, "Open");
    dialogThread.setName('Close dialog thread')
    dialogThread.start();
    ie.buttonClick(btnname)
    time.sleep(0.5)
    dialogThread.join();
    rep.verify ("Download dialog", ie.textBoxGetValue(btnname, "value"), testFile)
    
    # Clicking on the button should popup a modal alert dialog box.
    rep.status ("Testing alert dialog")
    ie.formName = "form1"
    dialogThread = cModalPopUp.handlePopup("Alert", "OK");
    dialogThread.setName('Alert dialog thread')
    dialogThread.start();
    ie.buttonClick("alertBtn")
    time.sleep(0.5)
    dialogThread.join();
    rep.verify ("Alert Dialog", ie.locationURL(), location + "?alertBtn=Submit+Query")
    
    #Clicking on the button should popup a modal confirm dialog box.
    rep.status ("Testing confirm dialog")
    ie.formName = "form2"
    dialogThread = cModalPopUp.handlePopup("Confirm", "OK");
    dialogThread.setName('Confirm dialog thread')
    dialogThread.start();
    ie.buttonClick("confirmBtn")
    time.sleep(0.5)
    dialogThread.join();
    rep.verify ("Confirm dialog", ie.locationURL(), location + "?confirmBtn=Confirm+Dialog")
    
    #Clicking on the button should popup a modal prompt dialog box.
    rep.status ("Testing prompt dialog")
    ie.formName = "form3"
    dialogThread = cModalPopUp.handlePopup("Prompt", "Hello World", "OK");
    dialogThread.setName('Prompt dialog thread')
    dialogThread.start();
    ie.buttonClick("promptBtn")
    time.sleep(0.5)
    dialogThread.join();
    print 'Done testing prompt dialog';
    rep.verify ("Prompt dialog", ie.locationURL(), location + "?promptBtn=Prompt+Dialog")

# Run the whole suite of tests in a non-framed browser
ie.frameName = None
goGoGadgetTests()

# Run the whole suite of tests again in a frame
ie.linkClick ("Frame Me")
ie.frameName = "main"
goGoGadgetTests()

# Test the frame functions themselves.
ie.frameName = None
runFrameTests()

# Run the modal popup tests
ie.frameName = "main"
ie.linkClick ("Unframe")
ie.frameName = None
runModalTests()

#-----------------------------------------------------------------------------
# Finalize the reporting
#-----------------------------------------------------------------------------
rep.finalize()
ie.navigate (os.path.abspath(pathName) + "/results.html#done")
