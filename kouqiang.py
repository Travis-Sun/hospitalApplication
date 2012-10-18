from cPAMIE import PAMIE

ie = PAMIE()
ie.navigate("www.google.com")
ie.textBoxSet("q", "python")
ie.buttonClick("btnG")
