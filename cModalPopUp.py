""" 
cModalPopUp.py
Revised: Jan 9th 2006
Developer: plhdpk 
Description: Class to handle pop up windows

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

import cPAMIE
import winGuiAuto
import win32gui
import time
import os, sys
import warnings
import threading
import traceback
import pprint

warnings.filterwarnings("ignore")

class handlePopup(threading.Thread):
    """ Construct a popup handler thread.
    parameters:
        type      - The type of popup to expect.
        *args     - One or more arguments to handle the popup, usually just a
                    control name such as 'OK' or 'Cancel' works but sometimes a
                    file name or string is needed as well.
    """

    showDebugging = False            # Show debug print lines?

    def __init__(self, type, *args):
        threading.Thread.__init__(self);
        self.wga = winGuiAuto;
        self.wn = win32gui;
        self.popupType = type;
        if type == 'ChooseFile':
            self.command = self.enterTextAndClickControl;
            self.popupName = 'Choose File';
            self.args = args;
        elif type == 'Alert':
            self.command = self.clickControl;
            self.popupName = 'Microsoft Internet Explorer';
            self.args = args;
        elif type == 'Confirm':
            self.command = self.clickControl;
            self.popupName = 'Microsoft Internet Explorer';
            self.args = args;
        elif type == 'Prompt':
            self.command = self.enterTextAndClickControl;
            self.popupName = 'Explorer User Prompt';
            self.args = args;
        else:
            self.command = self.clickControl;
            self.popupName = 'Microsoft Internet Explorer'
            self.args = 'Cancel;'

    def run(self):
        """ Override Threading's run() method.  Finds the dialog and calls
        the required command with the arguments supplied in the constructor.
        TODO: Need to find an exit strategy if the dialog is not found.
        parameters:
            None
        returns:
            Nothing
        """
        count = 10
        while(count <> 0):
            time.sleep(1);
            try:
                hwnd = self.wn.FindWindow("#32770", self.popupName)
                try:
                    apply(self.command, (hwnd, self.args,))
                    time.sleep(1)
                    return
                except:
                    if self.showDebugging:
                        (ErrorType,ErrorValue,ErrorTB)=sys.exc_info()
                        print sys.exc_info()
                        traceback.print_exc(ErrorTB)
            except:
                pass
            count -= 1;
        return

    def enterTextAndClickControl(self, hwnd, args):
        """ Used for file choosers or prompt dialogs that enter text into a text box.
            parameters:
                hwnd:       - The handle to the dialog.
                args[0]     - The text to set in the text box in the dialog.
                args[1]     - The button control name.
            returns:
                Nothing
        """
        text=args[0];
        control=args[1];
        if self.showDebugging:
            print "Text and Control is: %s %s" %(text, control)
            x = self.wga.dumpWindow(hwnd) # dump out all the controls
            pprint.pprint(x) # print out all the controls
        inputBox = self.wga.findControl(hwnd,
                    wantedClass="Edit")
        self.wga.setEditText(inputBox, text)
        time.sleep(.5)
        buttons = self.wga.findControls(hwnd,
                    wantedClass="Button",
                    wantedText=control)
        for b in buttons:
            self.wga.clickButton(b)

    def clickControl(self, hwnd, args):
        """ Used for simple dialogs that just have buttons such as 'ok', 'cancel'
            or 'clear'.
            parameters:
                hwnd:       - The handle to the dialog.
                args[0]     - The button control name.
            returns:
                Nothing
        """
        controlText = args[0];
        if self.showDebugging:
            x = self.wga.dumpWindow(hwnd) # dump out all the controls
            pprint.pprint(x) # print out all the controls
        button = self.wga.findControl(hwnd,
                    wantedClass="Button",
                    wantedText=controlText)
        self.wga.clickButton(button)
