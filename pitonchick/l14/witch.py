import random
f = open("Толстой Лев. Война и мир. Том 1 - royallib.ru.txt", "r", encoding="utf-8")
text = f.read()
f.close()
input("Введите ваш вопрос: ")
answer_len = 26
position = random.randint(0, len(text) - answer_len)
answer = text[position:position + answer_len]
answer = answer[answer.find(" ") + 1:answer.rfind(" ")]
print(answer)