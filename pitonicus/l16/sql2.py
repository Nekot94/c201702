import sqlite3
conn = sqlite3.connect("games.db")
curs = conn.cursor()

# curs.execute("SELECT * FROM top_games")
# rows = curs.fetchall()
# print(rows)

rows = curs.execute("SELECT name, rating FROM top_games WHERE genre = 'РПГ' ORDER BY rating DESC LIMIT 1")
for row in rows:
	print("Название: {0[0]}, рейтинг: {0[1]}".format(row))

curs.execute("UPDATE top_games SET rating = 1.1 WHERE name = 'ГТА-5'")
curs.execute("DELETE FROM top_games WHERE name = 'Аутласт'")
conn.commit()


curs.execute("SELECT * FROM top_games")
rows = curs.fetchall()
print(rows)

curs.close()
conn.close()










