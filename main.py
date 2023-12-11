

from PyQt5 import QtCore, QtGui, QtWidgets
import sys

#автоматическое преобразование
from subprocess import Popen
p = Popen("convert.bat")
import time
time.sleep(0.5)

import design  # Это наш конвертированный файл дизайна





class App(QtWidgets.QMainWindow, design.Ui_MainWindow):

    def calcInstallments(self):
        # Получаем значения
        Loan = float(self.installmentsSum.value())
        InterestRate =0
        Period = self.installmentsPeriod.value()
        res:QtWidgets.QPlainTextEdit = self.plainTextEdit_3
        answerText = self.label_12
        dept=0
        Sum = Loan
        text ="№\tСумма Платежа\tОстаток Долга\n"
        for i in range(0,int(Period)):
            everyMonthPayment = Sum/(Period-i) + Sum*InterestRate*12/365
            Sum -= everyMonthPayment
            dept += everyMonthPayment
            text+=str(i+1)+"\t"+str(round(everyMonthPayment,2))+"\t\t"+str(round(Sum,2))+"\n"
        res.setPlainText(text)
        text="Ежемесячный платёж:\t"+str(round(everyMonthPayment,2))+"\n"
        text+="Сумма процентов:\t"+str(round(dept-Loan,2))+"\n"
        text+="Долг+проценты:\t\t"+str(round(dept,2))+"\n"
        answerText.setText(text)


    # Функция для расчёта кредита 
    def calcLoan(self):
        if self.radioButton_3.isChecked():
            self.calcLoanAnnual()
        else:
            self.calcLoanDifferentially()


    # Функция для расчёта ипотеки 
    def calcMortgage(self):
        if self.radioButton_2.isChecked():
            self.calcMortgageAnnual()
        else:
            self.calcMortgageDifferentially()
    def calcMortgageDifferentially(self):
        # Получаем значения
        Loan = float(self.mortgageSum.value())
        InterestRate = self.mortgageInterestRate.value()/100
        Period = self.mortgagePeriod.value()
        res:QtWidgets.QPlainTextEdit = self.plainTextEdit
        answerText = self.label_4
        dept=0
        Sum = Loan
        text ="№\tСумма Платежа\tОстаток Долга\n"
        for i in range(0,int(Period)):
            
            everyMonthPayment = Sum/(Period-i) + Sum*InterestRate*12/365
            Sum -= everyMonthPayment
            dept += everyMonthPayment
            text+=str(i+1)+"\t"+str(round(everyMonthPayment,2))+"\t\t"+str(round(Sum,2))+"\n"
        res.setPlainText(text)
        text="Ежемесячный платёж:\t"+str(round(everyMonthPayment,2))+"\n"
        text+="Сумма процентов:\t"+str(round(dept-Loan,2))+"\n"
        text+="Долг+проценты:\t\t"+str(round(dept,2))+"\n"
        answerText.setText(text)
    def calcLoanDifferentially(self):
         # Получаем значения
        Loan = float(self.loanSum.value())
        InterestRate = self.loanInterestRate.value()/100
        Period = self.loanPeriod.value()
        res:QtWidgets.QPlainTextEdit = self.plainTextEdit_2
        answerText = self.label_8
        dept=0
        Sum = Loan
        text ="№\tСумма Платежа\tОстаток Долга\n"
        for i in range(0,int(Period)):
            
            everyMonthPayment = Sum/(Period-i) + Sum*InterestRate*12/365
            Sum -= everyMonthPayment
            dept += everyMonthPayment
            text+=str(i+1)+"\t"+str(round(everyMonthPayment,2))+"\t\t"+str(round(Sum,2))+"\n"
        res.setPlainText(text)
        text="Ежемесячный платёж:\t"+str(round(everyMonthPayment,2))+"\n"
        text+="Сумма процентов:\t"+str(round(dept-Loan,2))+"\n"
        text+="Долг+проценты:\t\t"+str(round(dept,2))+"\n"
        answerText.setText(text)

    def calcLoanAnnual(self):
        # Получаем значения
        Sum = float(self.loanSum.value())
        InterestRate = self.loanInterestRate.value()/100
        Period = self.loanPeriod.value()
        res:QtWidgets.QPlainTextEdit = self.plainTextEdit_2
        answerText = self.label_8

        everyMonthPayment = Sum * (InterestRate * (1 + InterestRate) ** Period) / ((1 + InterestRate) ** Period - 1)
        dept = everyMonthPayment*Period
        text="Ежемесячный платёж:\t"+str(round(everyMonthPayment,2))+"\n"
        text+="Сумма процентов:\t"+str(round(dept-Sum,2))+"\n"
        text+="Долг+проценты:\t\t"+str(round(dept,2))+"\n"
        answerText.setText(text)
        
        text ="№\tСумма Платежа\tОстаток Долга\n"
        for i in range(1,int(Period)+1):
            dept-=everyMonthPayment
            text+=str(i)+"\t"+str(round(everyMonthPayment,2))+"\t\t"+str(round(dept,2))+"\n"
        res.setPlainText(text)
    def calcMortgageAnnual(self):
        # Получаем значения
        Sum = float(self.mortgageSum.value())
        InterestRate = self.mortgageInterestRate.value()/100
        Period = self.mortgagePeriod.value()
        res:QtWidgets.QPlainTextEdit = self.plainTextEdit
        answerText = self.label_4

        everyMonthPayment = Sum * (InterestRate * (1 + InterestRate) ** Period) / ((1 + InterestRate) ** Period - 1)
        dept = everyMonthPayment*Period
        text="Ежемесячный платёж:\t"+str(round(everyMonthPayment,2))+"\n"
        text+="Сумма процентов:\t"+str(round(dept-Sum,2))+"\n"
        text+="Долг+проценты:\t\t"+str(round(dept,2))+"\n"
        answerText.setText(text)
        
        text ="№\tСумма Платежа\tОстаток Долга\n"
        for i in range(1,int(Period)+1):
            dept-=everyMonthPayment
            text+=str(i)+"\t"+str(round(everyMonthPayment,2))+"\t\t"+str(round(dept,2))+"\n"
        res.setPlainText(text)


    def addFunctions(self): 
        self.mortgageCalcButton.clicked.connect(self.calcMortgage)
        self.loanCalcButton.clicked.connect(self.calcLoan)
        self.installmentsCalcButton.clicked.connect(self.calcInstallments)

    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.setFixedSize(800, 600) # устанавливаем размер окна
        self.addFunctions() # Добавляем наши фунции

def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = App()  # Создаём объект класса App
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()