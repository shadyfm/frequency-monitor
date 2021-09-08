
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1067, 779)
        self.Test = QtWidgets.QPushButton(Form)
        self.Test.setGeometry(QtCore.QRect(120, 70, 131, 91))
        self.Test.setStyleSheet("background-color: rgb(138, 226, 52);")
        self.Test.setObjectName("Test")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.Test.setText(_translate("Form", "Original Name"))

def main():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()  
    
