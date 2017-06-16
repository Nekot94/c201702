text = input("Введите текст :")
# text = text[::-1]
# text = text[len(text)//2:] + text[:len(text)//2]
text = text.replace("а","в").replace("о","у")
print(text)