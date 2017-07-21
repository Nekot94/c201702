import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QLabel
from PyQt5.QtWidgets import QCheckBox, QGridLayout, QAction, QFileDialog, qApp

class MyWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		exitAction = QAction("&Выход", self)
		exitAction.setShortcut("Ctrl+Q")
		exitAction.setStatusTip("Выход")
		exitAction.triggered.connect(qApp.quit) 

		openAction = QAction("&Открыть", self)
		openAction.setShortcut("Ctrl+O")
		openAction.setStatusTip("Открывашка")
		openAction.triggered.connect(self.openTest)

		self.statusBar()
		menu = self.menuBar()
		fileMenu = menu.addMenu("&Файл")
		fileMenu.addAction(openAction)
		fileMenu.addAction(exitAction)

		grid = QGridLayout()
		grid.setSpacing(10)

		self.question = QLabel()
		grid.addWidget(self.question, 0,0)

		self.answers = []
		n, k = 1, 0
		for i in range(4):
			self.answers.append(QCheckBox())
			grid.addWidget(self.answers[i], n, k)
			if k < 1:
				k += 1
			else:
				k = 0
				n += 1

		self.nextButton = QPushButton("Далее")
		grid.addWidget(self.nextButton, n, 1)
		self.nextButton.clicked.connect(self.goNext)

		self.mainWidget = QWidget()
		self.mainWidget.setLayout(grid)
		self.mainWidget.hide()
		
		self.endWidget = QLabel()

		self.setCentralWidget(self.mainWidget)


		self.setWindowTitle("Это окошечко")
		self.setGeometry(30, 50, 800, 600)
		self.show()

	def openTest(self):
		fname = QFileDialog.getOpenFileName(self, 'Открыть тест', '.')
		self.test = []
		with open(fname[0], 'r', encoding="utf-8") as f:
			for line in f:
				self.test.append(line)
		# print(self.test)

		self.counts = len(self.test) // 3
		self.currentQuestion = 1
		self.line = 0
		self.rightCounts = 0

		self.goNext()
		self.mainWidget.show()


	def goNext(self):
		if self.currentQuestion > 1:
			right = 0
			for cAnswer in self.answers:
				if cAnswer.isChecked():
					if cAnswer.text() in self.rightAnswers:
						right += 1
					else:
						right = 0
						break

			if right == len(self.rightAnswers):
				self.rightCounts += 1

		if self.currentQuestion > self.counts:
			self.endWidget.setText('Результат: {0.rightCounts}/{0.counts}'.format(self))
			self.setCentralWidget(self.endWidget)
			return

		self.question.setText(self.test[self.line])
		answers = self.test[self.line + 1][:-1].split(', ')
		for cAnswer, answer in zip(self.answers, answers):
			cAnswer.setText(answer)
			cAnswer.setChecked(False)
		self.rightAnswers = self.test[self.line + 2][:-1].split(', ')

		self.line += 3
		self.currentQuestion += 1


if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = MyWindow()
	sys.exit(app.exec_())