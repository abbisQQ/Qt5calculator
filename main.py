import sys
from PyQt5.QtWidgets import *


class Application(QWidget):

    def __init__(self):
        # we initialize the class we inherit(Qwidget)
        super().__init__()
        self.dot_use = False
        self.screen = QLineEdit()
        self.setWindowTitle("PyQt5 Calculator")
        self.setFixedSize(250, 200)
        self.create_app()

    def create_app(self):
        # creating out gui
        grid = QGridLayout()

        button_ac = QPushButton("AC", self)
        button_ce = QPushButton("CE", self)
        button_div = QPushButton("/", self)
        button0 = QPushButton('0', self)
        button1 = QPushButton('1', self)
        button2 = QPushButton('2', self)
        button3 = QPushButton('3', self)
        button4 = QPushButton('4', self)
        button5 = QPushButton('5', self)
        button6 = QPushButton('6', self)
        button7 = QPushButton('7', self)
        button8 = QPushButton('8', self)
        button9 = QPushButton('9', self)
        button_minus = QPushButton("-", self)
        button_add = QPushButton("+", self)
        button_multiply = QPushButton("*", self)
        button_dot = QPushButton(".", self)
        button_equals = QPushButton("=", self)

        grid.addWidget(self.screen, 0, 0, 1, 4)
        # 1st row
        grid.addWidget(button_ac, 1, 0, 1, 1)
        grid.addWidget(button_dot, 1, 2, 1, 1)
        grid.addWidget(button_ce, 1, 1, 1, 1)
        grid.addWidget(button_div, 1, 3, 1, 1)
        # 2nd row
        grid.addWidget(button7, 2, 0, 1, 1)
        grid.addWidget(button8, 2, 1, 1, 1)
        grid.addWidget(button9, 2, 2, 1, 1)
        grid.addWidget(button_multiply, 2, 3, 1, 1)
        # 3rd row
        grid.addWidget(button4, 3, 0, 1, 1)
        grid.addWidget(button5, 3, 1, 1, 1)
        grid.addWidget(button6, 3, 2, 1, 1)
        grid.addWidget(button_minus, 3, 3, 1, 1)
        # 4th row
        grid.addWidget(button1, 4, 0, 1, 1)
        grid.addWidget(button2, 4, 1, 1, 1)
        grid.addWidget(button3, 4, 2, 1, 1)
        grid.addWidget(button_add, 4, 3, 1, 1)

        grid.addWidget(button0, 5, 0, 1, 2)
        grid.addWidget(button_dot, 5, 2, 1, 1)
        grid.addWidget(button_equals, 5, 2, 1, 1)

        self.setLayout(grid)
        self.show()

        button_ac.clicked.connect(lambda: self.calculate("AC"))
        button_ce.clicked.connect(lambda: self.calculate("CE"))
        button_dot.clicked.connect(lambda: self.calculate("."))
        button_equals.clicked.connect(lambda: self.calculate("="))
        button_minus.clicked.connect(lambda: self.calculate("-"))
        button_add.clicked.connect(lambda: self.calculate("+"))
        button_multiply.clicked.connect(lambda: self.calculate("*"))
        button_div.clicked.connect(lambda: self.calculate("/"))
        button1.clicked.connect(lambda: self.calculate("1"))
        button2.clicked.connect(lambda: self.calculate("2"))
        button3.clicked.connect(lambda: self.calculate("3"))
        button4.clicked.connect(lambda: self.calculate("4"))
        button5.clicked.connect(lambda: self.calculate("5"))
        button6.clicked.connect(lambda: self.calculate("6"))
        button7.clicked.connect(lambda: self.calculate("7"))
        button8.clicked.connect(lambda: self.calculate("8"))
        button9.clicked.connect(lambda: self.calculate("9"))
        button0.clicked.connect(lambda: self.calculate("0"))

    def calculate(self, b):
        if b == "AC":
            self.screen.setText("")
            self.dot_use = False
        elif b == "CE":
            if self.screen.text()[-1] == ".":
                self.dot_use = False
            self.screen.setText(self.screen.text()[:-1])
        elif b == ".":
            if self.screen.text().endswith("-") \
                    or self.screen.text().endswith("+") \
                    or self.screen.text().endswith("/") \
                    or self.screen.text().endswith("*"):
                pass
            elif not self.screen.text().endswith(".") and not self.dot_use:
                self.screen.setText(self.screen.text() + ".")
                self.dot_use = True

        elif b == "=":
            self.screen.setText(str(eval(self.screen.text())))
            if self.screen.text().__contains__("."):
                self.dot_use = True
            else:
                self.dot_use = False
        elif b == "-":
            if self.screen.text() == "":
                self.screen.setText("-")
            elif self.screen.text().endswith("-")\
                    or self.screen.text().endswith("+")\
                    or self.screen.text().endswith("/")\
                    or self.screen.text().endswith("*"):
                self.screen.setText(self.screen.text()[:-1]+"-")
            else:
                self.screen.setText(str(eval(self.screen.text())))
                self.screen.setText(self.screen.text()+"-")
                self.dot_use = False
        elif b == "+":
            if self.screen.text() == "-":
                self.screen.setText("")
            elif self.screen.text().endswith("-")\
                    or self.screen.text().endswith("+")\
                    or self.screen.text().endswith("/")\
                    or self.screen.text().endswith("*"):
                self.screen.setText(self.screen.text()[:-1]+"+")
            else:
                self.screen.setText(str(eval(self.screen.text())))
                self.screen.setText(self.screen.text()+"+")
                self.dot_use = False
        elif b == "*":
            if self.screen.text() == "-":
                self.screen.setText("")
            elif self.screen.text().endswith("-")\
                    or self.screen.text().endswith("+")\
                    or self.screen.text().endswith("/")\
                    or self.screen.text().endswith("*"):
                self.screen.setText(self.screen.text()[:-1]+"*")
            else:
                self.screen.setText(str(eval(self.screen.text())))
                self.screen.setText(self.screen.text()+"*")
                self.dot_use = False
        elif b == "/":
            if self.screen.text() == "-":
                self.screen.setText("")
            elif self.screen.text().endswith("-")\
                    or self.screen.text().endswith("+")\
                    or self.screen.text().endswith("/")\
                    or self.screen.text().endswith("*"):
                self.screen.setText(self.screen.text()[:-1]+"/")
            else:
                self.screen.setText(str(eval(self.screen.text())))
                self.screen.setText(self.screen.text()+"/")
                self.dot_use = False
        elif b == "0":
            if self.screen.text().endswith(("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ".")):
                self.screen.setText(self.screen.text() + "0")
        elif b == "1":
            self.screen.setText(self.screen.text() + "1")
        elif b == "2":
            self.screen.setText(self.screen.text() + "2")
        elif b == "3":
            self.screen.setText(self.screen.text() + "3")
        elif b == "4":
            self.screen.setText(self.screen.text() + "4")
        elif b == "5":
            self.screen.setText(self.screen.text() + "5")
        elif b == "6":
            self.screen.setText(self.screen.text() + "6")
        elif b == "7":
            self.screen.setText(self.screen.text() + "7")
        elif b == "8":
            self.screen.setText(self.screen.text() + "8")
        elif b == "9":
            self.screen.setText(self.screen.text() + "9")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Application()
    sys.exit(app.exec())
