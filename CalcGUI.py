import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class CalcUI(QMainWindow):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("Calculator")
		self.setFixedSize(300,350)

		#currentNum stores numbers pressed
		#finNum stores the currentNum and the operator pressed
		self.currentNum = []
		self.finNum = []

		#Layout
		self.container = QVBoxLayout()
		self.widget = QWidget(self)
		self.widget.setLayout(self.container)
		self.setCentralWidget(self.widget)
		self.createDisplay()
		self.createKeypad()

	#GUI of calculator
	def createDisplay(self):
		self.display = QLineEdit()
		self.display.setFixedHeight(50)
		self.display.setAlignment(Qt.AlignRight)
		self.display.setReadOnly(True)
		self.display.setText("0")
		self.container.addWidget(self.display)

	def createKeypad(self):
		self.keypad = QGridLayout()
		
		#Use a dictionary to make it more elegant than this!!
		buttons = { "9":(0,2), "8":(0,1), "7":(0,0),
					"6":(1,2), "5":(1,1), "4":(1,0),
					"3":(2,2), "2":(2,1), "1":(2,0), 
					"0":(3,1)}
		#Buttons
		btn9 = QPushButton("9", clicked = lambda: self.num_clicked('9'))
		btn8 = QPushButton("8", clicked = lambda: self.num_clicked('8'))
		btn7 = QPushButton("7", clicked = lambda: self.num_clicked('7'))
		btn6 = QPushButton("6", clicked = lambda: self.num_clicked('6'))
		btn5 = QPushButton("5", clicked = lambda: self.num_clicked('5'))
		btn4 = QPushButton("4", clicked = lambda: self.num_clicked('4'))
		btn3 = QPushButton("3", clicked = lambda: self.num_clicked('3'))
		btn2 = QPushButton("2", clicked = lambda: self.num_clicked('2'))
		btn1 = QPushButton("1", clicked = lambda: self.num_clicked('1'))
		btn0 = QPushButton("0", clicked = lambda: self.num_clicked('0'))
		mult = QPushButton("*", clicked = lambda: self.op_clicked('*'))
		divd = QPushButton("/", clicked = lambda: self.op_clicked('/'))
		add = QPushButton("+", clicked = lambda: self.op_clicked('+'))
		sub = QPushButton("-", clicked = lambda: self.op_clicked('-'))
		equal = QPushButton("=", clicked = self.result)
		clear = QPushButton("C", clicked = self.clear)

		size = 60
		btn9.setFixedSize(size,size)
		btn8.setFixedSize(size,size)
		btn7.setFixedSize(size,size)
		btn6.setFixedSize(size,size)
		btn5.setFixedSize(size,size)
		btn4.setFixedSize(size,size)
		btn3.setFixedSize(size,size)
		btn2.setFixedSize(size,size)
		btn1.setFixedSize(size,size)
		btn0.setFixedSize(size,size)
		mult.setFixedSize(size,size)
		divd.setFixedSize(size,size)
		add.setFixedSize(size,size)
		sub.setFixedSize(size,size)
		equal.setFixedSize(size,size)
		clear.setFixedSize(size,size)

		self.keypad.addWidget(mult,0,3)
		self.keypad.addWidget(btn9,0,2)
		self.keypad.addWidget(btn8,0,1)
		self.keypad.addWidget(btn7,0,0)
		self.keypad.addWidget(divd,1,3)
		self.keypad.addWidget(btn6,1,2)
		self.keypad.addWidget(btn5,1,1)
		self.keypad.addWidget(btn4,1,0)
		self.keypad.addWidget(add,2,3)
		self.keypad.addWidget(btn3,2,2)
		self.keypad.addWidget(btn2,2,1)
		self.keypad.addWidget(btn1,2,0)
		self.keypad.addWidget(sub,3,3)
		self.keypad.addWidget(equal,3,2)
		self.keypad.addWidget(clear,3,1)
		self.keypad.addWidget(btn0,3,0)
		self.container.addLayout(self.keypad)


	#Functionality of calculator
	def num_clicked(self, num):
		#Do not display or count leading zeroes
		if len(self.currentNum) == 1 and self.currentNum[0] == '0' and num == '0': 
			self.display.setText('0')
			self.currentNum = []
		elif len(self.currentNum) == 1 and self.currentNum[0] == '0' and num != '0':
			self.currentNum[0] = num
			self.display.setText(num)
		else:
			self.currentNum.append(num)
			temp_num = ''.join(self.currentNum)
			if self.finNum:
				self.display.setText(''.join(self.finNum) + temp_num)
			else:
				self.display.setText(temp_num)

	def op_clicked(self, op):
		if len(self.currentNum) != 0:
			temp_num = ''.join(self.currentNum) + op
			self.finNum.append(temp_num)
			self.currentNum = []
		self.display.setText(''.join(self.finNum))

	def result(self):
		if len(self.currentNum) == 0 and len(self.finNum) == 0:
			self.display.setText('0')
		else:
			temp_num = ''.join(self.finNum) + ''.join(self.currentNum)
			try:
				answer = str(eval(temp_num))
				#Clear results in both lists and save answer in currentNum list
				self.clear()
				self.currentNum.append(answer)
				self.display.setText(answer)

			except ZeroDivisionError:
				self.display.setText("Cannot divide by zero")
				self.finNum = []
				self.currentNum =[]

			except SyntaxError:
				#Removes the operator at the end and performs the calculation with the answer
				temp_ans = temp_num + temp_num[:len(temp_num)-1]
				answer = str(eval(temp_ans))
				self.clear()
				self.currentNum.append(answer)
				self.display.setText(answer)
				
	def clear(self):
		self.finNum = []
		self.currentNum =[]
		self.display.setText("0")

def main():
	app = QApplication(sys.argv)
	calc = CalcUI()
	calc.show()
	sys.exit(app.exec_())

if __name__ == '__main__':
	main()
