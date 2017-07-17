import sqlite3
conn = sqlite3.connect("games.db")
curs = conn.cursor()

curs.execute("DROP TABLE top_games")

curs.execute("""CREATE TABLE top_games (
name VARCHAR(60) PRIMARY KEY,
rating REAL,
genre VARCHAR(40)
)""")


curs.execute("INSERT INTO top_games VALUES('копатель онлайн', 100, 'песочница')")
curs.execute("INSERT INTO top_games VALUES('Дарк Сас', 10, 'РПГ')")

name, rating, genre = 'Аутласт', 15, 'Хоррор'
curs.execute("INSERT INTO top_games VALUES(?, ?, ?)", (name, rating, genre))

ins = "INSERT INTO top_games VALUES(?, ?, ?)"
data = 'Готика', 30.1, 'РПГ'
curs.execute(ins, data)

data = 'ГТА-5', 2.5, 'ЭКШН'
curs.execute(ins, data)

conn.commit()


curs.close()
conn.close()