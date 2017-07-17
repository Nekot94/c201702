import sqlite3
from collections import OrderedDict

QUESTIONS = OrderedDict({
	"surname": "Какова ваша фомилия !!!!!!",
	"naval": "Кто такой	Нэвельный"
	})

class MyBot:
	def __init__(self,name):
		self.conn = sqlite3.connect("myBot.db")
		self.curs = self.conn.cursor()
		self.name = name

	def __del__(self):
		self.curs.close()
		self.conn.close()

	def add_questions(self):
		ins = "INSERT INTO questions VALUES (?, ?)"
		for key,value in QUESTIONS.items():
			self.curs.execute(ins,(key,value) )
		self.conn.commit()

	def add_friend(self, *args):
		ins = "INSERT INTO friends VALUES (?, ?, ?)"
		self.curs.execute(ins, args)
		self.conn.commit()
	
	def drop_all(self):
		self.curs.execute("DROP TABLE questions")
		# self.curs.execute("DROP TABLE friends")

	def create_table(self):
		self.curs.execute("""CREATE TABLE questions
			(qtype VARCHAR(40) PRIMARY KEY,
			questions VARCHAR(50)
			)""")
		self.add_questions()
		rows = self.curs.execute("SELECT * FROM questions")
		crt = """CREATE TABLE friends
		(name VARCHAR(50) PRIMARY KEY, """
		for row in rows: 
			m = row[0] + " VARCHAR(100),"
			crt += m
		crt = crt[:-1] + ")"
		self.curs.execute(crt)
		self.add_friend("Сааду", "Магомедов", "ДЕБИЛЬ" )
		rows = self.curs.execute("SELECT * FROM friends")
		print(rows.fetchall())


	def start_chat(self):
		user_name = input("Меня зовут "+ self.name +", а тебя?")
		if self.is_known(user_name):
			self.about_you(user_name)

		else:
			self.ask_questions(user_name)


myBot = MyBot("Варис")
myBot.drop_all()
myBot.create_table()