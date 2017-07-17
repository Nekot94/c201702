import json
with open("base.json", "r", encoding="utf-8") as fjson:
	text = fjson.read()

text = json.loads(text)

print(text["Шамиль"]["Никнэйм"])
for element in text:
	print(text[element]["Никнэйм"], text[element]["Пол"])

text2 = json.dumps({"Ничего":"Нет"})
with open("base2.json", "w", encoding="utf-8") as fjson:
	fjson.write(text2)