import sys
from PyQt5.QtWidgets import QApplication, QWidget

class MyWidget(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		self.setWindowTitle("Не Юи, а Гуи")
		self.setGeometry(20, 100, 800, 400)
		self.show()

if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = MyWidget()
	sys.exit(app.exec_())
