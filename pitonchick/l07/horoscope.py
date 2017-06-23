class DayError(Exception):
    pass

class MonthError(Exception):
    pass

while True:
    try:
        date  = input("Введите дату рождения в ввиде ДД.ММ.ГГГГ: ")
        day = int(date[0:2])
        # print(day)
        month = int(date[3:5])
        # print(month)
        year = int(date[6:])
        # print(year)
        if day <= 0 or day > 31:
            raise DayError 
        if month in range(1,32):
            raise MonthError

        if (day >21 and month == 6) or (day < 21 and month == 7):
            print("Ты Рак")
        break

    except ValueError:
        print("Введите дату в правильном формате")
    except DayError:
        print("Введите правильный день")
    except MonthError:
        print("Введите правильный месяц")