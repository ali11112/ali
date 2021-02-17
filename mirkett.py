from PyQt5 import QtWidgets
import sys
from PyQt5.QtWidgets import QApplication, QDialog


from PyQt5 import uic


class calculatorWindow(QtWidgets.QMainWindow, QDialog):
    firNumber = None
    typingNumber = False

    def __init__(self):
        super().__init__()


        uic.loadUi('result.ui', self)

        # our buttons
        self.pushButton_17.clicked.connect(self.numberPressed)
        self.pushButton_15.clicked.connect(self.numberPressed)
        self.pushButton_14.clicked.connect(self.numberPressed)
        self.pushButton_13.clicked.connect(self.numberPressed)
        self.pushButton_11.clicked.connect(self.numberPressed)
        self.pushButton_10.clicked.connect(self.numberPressed)
        self.pushButton_9.clicked.connect(self.numberPressed)
        self.pushButton_5.clicked.connect(self.numberPressed)
        self.pushButton_6.clicked.connect(self.numberPressed)
        self.pushButton_7.clicked.connect(self.numberPressed)

        self.pushButton_19.clicked.connect(self.decimalPressed)
        self.pushButton_2.clicked.connect(self.unaryOperation)
        self.pushButton_3.clicked.connect(self.unaryOperation)

        self.pushButton_16.clicked.connect(self.binaryOperation)
        self.pushButton_12.clicked.connect(self.binaryOperation)
        self.pushButton_8.clicked.connect(self.binaryOperation)
        self.pushButton_4.clicked.connect(self.binaryOperation)

        self.pushButton_20.clicked.connect(self.equl_pressed)
        self.pushButton.clicked.connect(self.clearbtn)

        self.pushButton_16.setCheckable(True)
        self.pushButton_12.setCheckable(True)
        self.pushButton_8.setCheckable(True)
        self.pushButton_4.setCheckable(True)

    # number pressed method
    def numberPressed(self):
        button = self.sender()

        if ((
                self.pushButton_16.isChecked() or self.pushButton_12.isChecked()
                or self.pushButton_4.isChecked() or self.pushButton_8.isChecked())
                and (
                not self.typingNumber)):
            lbl = format(float(button.text()), '.15g')
            self.typingNumber = True

        else:

            if (('.' in self.label.text()) and (button.text() == '0')):
                lbl = format(self.label.text() + button.text(), '.15')
            else:
                lbl = format(float(self.label.text() + button.text()), '.15g')

        self.label.setText(lbl)

    # decimel number pressed
    def decimalPressed(self):

        self.label.setText(self.label.text() + '.')

    # unaryopertio
    def unaryOperation(self):
        button = self.sender()

        labelNumber = float(self.label.text())

        if button.text() == "+/-":
            labelNumber = labelNumber * -1
        else:
            labelNumber = labelNumber * 0.01

        newLabel = format(labelNumber, '.15g')

        self.label.setText(newLabel)

    # binary operation
    def binaryOperation(self):
        button = self.sender()

        self.firNumber = float(self.label.text())

        button.setChecked(True)

    def equl_pressed(self):
        secondNumber = float(self.label.text())

        if (self.pushButton_16.isChecked()):
            labelNumber = self.firNumber + secondNumber
            newLabel = format(labelNumber, '.15g')
            self.label.setText(newLabel)
            self.pushButton_16.setChecked(False)

        elif (self.pushButton_12.isChecked()):
            labelNumber = self.firNumber - secondNumber
            newLabel = format(labelNumber, '.15g')
            self.label.setText(newLabel)
            self.pushButton_12.setChecked(False)

        elif (self.pushButton_8.isChecked()):
            labelNumber = self.firNumber * secondNumber
            newLabel = format(labelNumber, '.15g')
            self.label.setText(newLabel)
            self.pushButton_8.setChecked(False)

        elif (self.pushButton_4.isChecked()):
            labelNumber = self.firNumber / secondNumber
            newLabel = format(labelNumber, '.15g')
            self.label.setText(newLabel)
            self.pushButton_4.setChecked(False)
        self.typingNumber = False

    def clearbtn(self):
        self.pushButton_16.setChecked(False)
        self.pushButton_12.setChecked(False)
        self.pushButton_8.setChecked(False)
        self.pushButton_4.setChecked(False)

        self.typingNumber = False

        self.label.setText("0")


app = QApplication(sys.argv)
calculator = calculatorWindow()
calculator.show()

sys.exit(app.exec())