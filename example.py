import sys
import hashlib

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QWidget


from AskPasswordDlg import *

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle('Input password dialogue example')
layout = QGridLayout()

runDlgBtn = QPushButton("Run dialogue")
layout.addWidget(runDlgBtn, 0, 0, 1, 2)
layout.addWidget(QLabel("Valid Password:"), 1, 0)
resultLbl = QLabel("?")
layout.addWidget(resultLbl, 1, 1)

def onRunDlgBtn():
    #pwd = hashlib.sha256(b'123').hexdigest() # do not store unencrypted password!
    #print(pwd)
    pwd = 'a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3'
        
    isPasswordCorrect = AskPasswordDlg.runDlg(pwd)
        
    # if you application has stylesheet file:
    #isPasswordCorrect = AskPasswordDlg.runDlg(pwd, "media/style.qss") 
    
    resultLbl.setText(str(isPasswordCorrect))

runDlgBtn.clicked.connect(onRunDlgBtn)

window.setLayout(layout)

window.show()
sys.exit(app.exec_())

