import sys
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QLineEdit, QLabel, QInputDialog
from PyQt5.QtWidgets import QGridLayout

#class Example
class Example(QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.InitUI()

    def InitUI(self):
        self.btn = QPushButton("Dialog", self)
        self.btn.move(20, 20)
        self.btn.clicked.connect(self.ShowDialog)

        self.le = QLineEdit(self)
        self.le.move(130, 22)

        self.setWindowTitle("Input Dialog")
        self.show()

    def ShowDialog(self):
        text,ok = QInputDialog.getText(self, "Input Dialog", "Enter your name:")
        if ok:
            self.le.setText(str(text))

#calss CalculateTax
class CalculateTax(QWidget):
    def __init__(self):
        super(CalculateTax, self).__init__()
        self.InitDialog()
    def InitDialog(self):
        #添加控件
        self.titleLabel = QLabel("Sales Tax Calculator", self)
        self.priceLabel = QLabel("Price: ", self)
        self.priceLe = QLineEdit(self)
        self.taxRateLabel = QLabel("TaxRate: ", self)
        self.taxRateLe = QLineEdit(self)
        self.calculateBtn = QPushButton("计算")
        self.resultLabel = QLabel("Result: ", self)
        self.resultLe = QLineEdit(self)

        #connect
        #self.calculateBtn.clicked.connect(self.CalculateTax)
        self.calculateBtn.clicked.connect(self.CalculateTax)

        #布局管理
        self.mainLayout = QGridLayout(self)
        self.mainLayout.addWidget(self.titleLabel, 0, 1)
        self.mainLayout.addWidget(self.priceLabel, 1, 0)
        self.mainLayout.addWidget(self.priceLe, 1, 1)
        self.mainLayout.addWidget(self.taxRateLabel, 2, 0)
        self.mainLayout.addWidget(self.taxRateLe, 2, 1)
        self.mainLayout.addWidget(self.calculateBtn, 2, 2)
        self.mainLayout.addWidget(self.resultLabel, 3, 0)
        self.mainLayout.addWidget(self.resultLe, 3, 1)

        self.setWindowTitle("Calculate Tax")
        self.show()
    def CalculateTax(self):
        priceStr = self.priceLe.text()
        checkRe = priceStr.isnumeric()
        if checkRe == True:
            priceInt = int(priceStr)
            #print(priceInt)
        else:
            print("Price中请输入数字！")

        taxRateStr = self.taxRateLe.text()
        checkRe = taxRateStr.isnumeric()
        if checkRe == True:
            taxRateInt = int(taxRateStr)
            #print(taxRateInt)
        else:
            print("TaxRate中请输入数字！")

        if checkRe == True:
            resultValue = priceInt * taxRateInt
            self.resultLe.setText(str(resultValue))
            #print("计算结果为{0}".format(resultValue))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    #ex = Example()
    ey = CalculateTax()
    sys.exit(app.exec_())
