import sys
import random

from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout
from PyQt5.QtWidgets import QPushButton, QLabel
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QBasicTimer, QSize

UNACTIVE = "bo1.png"
BAD = "bo2.png"
GOOD = "bo3.png"
TIME = 30

class MyWidget(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):

		self.now = 0

		self.timer = QBasicTimer()
		self.step = 0

		grid = QGridLayout()
		grid.setSpacing(10)

		self.holes = []
		n, k = 0, 0
		for i in range(9):
			self.holes.append(QPushButton("U", self))
			self.holes[i].setFlat(True)
			self.holes[i].setIcon(QIcon(UNACTIVE))
			self.holes[i].setIconSize(QSize(200,200))

			self.holes[i].clicked.connect(self.smash)

			grid.addWidget(self.holes[i], n, k)

			if k < 2:
				k += 1
			else:
				n += 1
				k = 0

		self.count = QLabel('0')
		self.time = QLabel(str(TIME))
		self.runBtn = QPushButton("В бой")
		self.runBtn.clicked.connect(self.startGame)

		grid.addWidget(self.count, n, 0)
		grid.addWidget(self.time, n, 1)
		grid.addWidget(self.runBtn, n, 2)

		font = QFont('Serif', 15, QFont.Light)
		self.count.setFont(font)
		self.time.setFont(font)
		self.runBtn.setFont(font)

		self.setLayout(grid)
		self.setWindowTitle("Не Юи, а Гуи")
		self.setGeometry(20, 100, 800, 400)
		self.show()


	def showHim(self):
		number = random.randint(0,8)
		kind = random.randint(0,1)
		if kind:
			self.holes[number].setText("G")
			self.holes[number].setIcon(QIcon(GOOD))
		else:
			self.holes[number].setText("B")
			self.holes[number].setIcon(QIcon(BAD))
		self.now = number

	def clearHim(self):
		self.holes[self.now].setText("U")
		self.holes[self.now].setIcon(QIcon(UNACTIVE))

	def timerEvent(self, e):
		self.clearHim()
		self.showHim()

		if self.step >= TIME * 2:
			self.timer.stop()
			self.runBtn.setEnabled(True)
			self.time.setText(str(TIME))
			self.step = 0
			self.clearHim()
			return

		self.step += 1
		if self.step % 2:
			time = int(self.time.text()) - 1
			self.time.setText(str(time))

	def startGame(self):
		time = TIME * 1000 // 60
		# time = 500
		self.timer.start(time, self)
		self.count.setText("0")
		self.runBtn.setEnabled(False)

	def smash(self):
		sender = self.sender()
		if sender.text() == "B":
			self.clearHim()
			count = int(self.count.text()) + 1
			self.count.setText(str(count))
		if sender.text() == "G":
			self.clearHim()
			count = int(self.count.text()) - 1
			self.count.setText(str(count))


if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = MyWidget()
	sys.exit(app.exec_())
