class DayError(Exception): 
    pass
    
class MonthError(Exception): 
    pass

while True:
    try:
        date = input("Введите дату в формате дд.мм.гггг: ")
        day = int(date[:2])
        month =int(date[3:5])
        year = int(date[6:])
        # print(day , month , year)
        if day < 1 or day > 31:
            raise DayError
        if month not in range(1,13):
            raise MonthError

        if (day > 21 and month == 4) or (day < 21 and month == 5):
            print("Ты - телец <3")

        break
    except ValueError:
        print("Введите в правильном формате")
    except DayError:
        print("Введи правельный день")
    except MonthError:
        print("Введи правельный месяц")
