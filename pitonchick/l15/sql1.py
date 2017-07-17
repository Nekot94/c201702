import sqlite3
conn = sqlite3.connect("menu.db")
curs = conn.cursor()

curs.execute("DROP TABLE beach_menu")

curs.execute("""CREATE TABLE beach_menu
(name VARCHAR(40) PRIMARY KEY,
price INT,
insalubrity REAL
)""")

curs.execute("INSERT INTO beach_menu VALUES ('макароны', 50, 20.5)")
curs.execute("INSERT INTO beach_menu VALUES ('доширак', 30, 99.9)")

name, price, insalubrity = 'яжка', 100, 100

curs.execute("INSERT INTO beach_menu VALUES (?, ?, ?)", (name, price, insalubrity))

ins = "INSERT INTO beach_menu VALUES (?, ?, ?)"

name, price, insalubrity = 'греча', 50, 5

curs.execute(ins, (name, price, insalubrity))

conn.commit()

curs.close()
conn.close()



