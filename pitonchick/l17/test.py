






















						break
						right += 1
						right = 0
					else:
					if cAnswer.text() in self.rightAnswers:
				if cAnswer.isChecked():
				k += 1
				k = 0
				n += 1
				self.rightCounts += 1
				self.test.append(line)
			cAnswer.setChecked(False)
			cAnswer.setText(answer)
			else:
			for cAnswer in self.answers:
			for line in f:
			grid.addWidget(self.answers[i],n, k)
			if k < 1:
			if right == len(self.rightAnswers):
			return
			right = 0
			self.answers.append(QCheckBox())
			self.endWidget.setText("Результат: {0.rightCounts}/{0.counts}".format(self))
			self.setCentralWidget(self.endWidget)
		answers = self.test[l+1][:-1].split(', ')
		exitAction = QAction("&Выход",self)
		exitAction.setShortcut("Ctrl+Q")
		exitAction.setStatusTip("Выход")
		exitAction.triggered.connect(qApp.quit)
		fileMenu = menu.addMenu("&Файл")
		fileMenu.addAction(exitAction)
		fileMenu.addAction(openAction)
		fName = QFileDialog.getOpenFileName(self, 'Открыть файл', '.')
		for cAnswer, answer in zip(self.answers, answers):
		for i in range(4):
		grid = QGridLayout()
		grid.addWidget(self.nextButton,n,1)
		grid.addWidget(self.question, 0, 0)
		grid.setSpacing(10)
		if self.currentQuestion > 1:
		if self.currentQuestion > self.counts:
		l = self.line
		menu = self.menuBar()
		n, k = 1, 0
		openAction = QAction("&Открыть тест",self)
		openAction.setShortcut("Ctrl+O")
		openAction.setStatusTip("Открыть тест")
		openAction.triggered.connect(self.openTest)
		print(self.test)
		self.answers = []
		self.counts = len(self.test) // 3
		self.currentQuestion += 1
		self.currentQuestion = 1
		self.endWidget = QLabel()
		self.goNext()
		self.initUI()
		self.line += 3
		self.line = 0
		self.mainWidget = QWidget()
		self.mainWidget.hide()
		self.mainWidget.setLayout(grid)
		self.mainWidget.show()
		self.nextButton = QPushButton("Дальше")
		self.nextButton.clicked.connect(self.goNext)
		self.question = QLabel()
		self.question.setText(self.test[l])
		self.rightAnswers = self.test[l+2][:-1].split(', ')
		self.rightCounts = 0
		self.setCentralWidget(self.mainWidget)
		self.setGeometry(20, 100, 800, 600)
		self.setWindowTitle("тесты")
		self.show()
		self.statusBar()
		self.test = []
		super().__init__()
		with open(fName[0], 'r', encoding='utf-8') as f:
	app = QApplication(sys.argv)
	def __init__(self):
	def goNext(self):
	def initUI(self):
	def openTest(self):
	sys.exit(app.exec_())
	window = MyWidget()
class MyWidget(QMainWindow):
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QAction, QFileDialog
from PyQt5.QtWidgets import QLabel, QPushButton, QCheckBox, QGridLayout, qApp
if __name__ == "__main__":
import sys