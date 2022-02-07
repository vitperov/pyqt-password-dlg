from PyQt5 import QtWidgets
from pyqtgraph.Qt import QtCore, QtGui

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

import hashlib

class AskPasswordDlg(QtGui.QDialog):
    def __init__(self, passwordSha256):
        super().__init__()
        self.result = False
        self.pwd = passwordSha256
        self.setWindowTitle("Input password")

        self.layout = QGridLayout()

        self.layout.addWidget(QLabel("Password:"), 0, 0)

        self.pwdEdit = QtGui.QLineEdit()
        self.pwdEdit.setEchoMode(QtGui.QLineEdit.Password)
        self.layout.addWidget(self.pwdEdit, 0, 1)

        def onEnterClick(value):
            inputPwd = self.pwdEdit.text().encode("latin-1","ignore")
            encrypted = hashlib.sha256(inputPwd).hexdigest()
            if encrypted == self.pwd:
                self.result = True
                self.accept()
            else:
                self.wrongPwdLabel.show()
                self._hideWrongPwdTimer.start(3000)

        self.wrongPwdLabel = QLabel("Wrong password")
        self.wrongPwdLabel.setStyleSheet("QLabel { color : red; qproperty-alignment: AlignCenter;}");
        self.layout.addWidget(self.wrongPwdLabel, 1, 0, 1, 2)
        self.wrongPwdLabel.hide()
        
        self.layout.addWidget(QLabel(" "), 1, 2)
        
        cancelBtn = QPushButton("Cancel")
        self.layout.addWidget(cancelBtn, 2, 0)
        cancelBtn.clicked.connect(self.reject)
        
        okBtn = QPushButton("Ok")
        self.layout.addWidget(okBtn, 2, 2)
        okBtn.clicked.connect(onEnterClick)
        okBtn.setDefault(True)

        self.setLayout(self.layout)


        self._hideWrongPwdTimer=QTimer()
        self._hideWrongPwdTimer.setSingleShot(True)
        self._hideWrongPwdTimer.timeout.connect(self.wrongPwdLabel.hide)

    def setCSS(self, filename):
        rc = QFile(filename)
        rc.open(QFile.ReadOnly)
        content = rc.readAll().data()
        self.setStyleSheet(str(content, "utf-8"))

    @staticmethod
    def runDlg(passwordSha256, styleSheetFile=None):
        dlg = AskPasswordDlg(passwordSha256)
        dlg.setModal(True)
        if styleSheetFile is not None:
            dlg.setCSS(styleSheetFile)
        dlg.exec_()
        return dlg.result

