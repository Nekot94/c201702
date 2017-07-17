f = open("shepard.txt","w",encoding="utf-8")
f.write("писать\n")
f.write("и убивать")
f.close()

# f = open("shepard.txt","r",encoding="utf-8")
# text = f.read()
# f.close()
# print(text)

# f = open("shepard.txt","r",encoding="utf-8")
# text = f.readline()
# f.close()
# print(text)

# f = open("shepard.txt","r",encoding="utf-8")
# for line in f:
# 	print(line, end="")
# f.close()

with open("shepard2.txt", "a", encoding="utf-8") as f:
	f.write("ты монгрел")

