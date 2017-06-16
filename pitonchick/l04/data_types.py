commands = ["Убей", "Прыгни", "Улыбнись"]
print(commands[0])
print(commands)
print(commands[1:])
commands.append("Кушать")
print(commands)
additional_commands = ["Спать", "Спать", "Спать"]
commands.extend(additional_commands)
print(commands)
commands.insert(1, False)
print(commands)
commands.remove("Прыгни")
print(commands)
print(commands.pop(1))
print(commands)
del commands[1]
print(commands)
commands[2] = "Лететь на самолете"
print(commands)
# commands2 = commands
commands2 = commands[:]
print(commands2)
commands2[0] = "Уничтожить"
print(commands2)
print(commands)

names = "Я", "ТЫ", "МЫ"
print(names[1])
print(names)
# names[2] = "Пять"


