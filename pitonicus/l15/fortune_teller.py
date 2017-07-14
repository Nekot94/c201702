import random 

with open("принц.txt", "r", encoding="utf-8") as f:
	text = f.read()
input("Введи вопрос: ")
answer_len = 30
position = random.randint(0, len(text) - answer_len)
answer = text[position:position + answer_len + 1]
answer = answer[answer.find(" ") + 1: answer.rfind(" ")]
print(answer)