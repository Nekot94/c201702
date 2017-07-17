import sqlite3
conn = sqlite3.connect("menu.db")
curs = conn.cursor()

# curs.execute("SELECT * FROM beach_menu")
# rows = curs.fetchall()
# print(rows)

# curs.execute("SELECT name, insalubrity FROM beach_menu WHERE insalubrity > 5 ORDER BY insalubrity DESC LIMIT 2")
# for row in curs:
# 	print("Название: {0[0]}, степень вредности: {0[1]}".format(row))

curs.execute("UPDATE beach_menu SET price = 120 WHERE name = 'яжка'")
curs.execute("DELETE FROM beach_menu WHERE insalubrity < 10")
conn.commit()

curs.execute("SELECT * FROM beach_menu")
rows = curs.fetchall()
print(rows)


curs.close()
conn.close()