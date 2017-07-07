class Kumis:
    def __init__(self, percent_fat, color):
        self.percent_fat = percent_fat
        self.color = color
        self.country = "Казахстан"

    def ferment(self, time):
        return "Испортился" if time > 10 else "Все хорошо"

the_best_kumis_in_the_world = Kumis(120,"Серый")
print(the_best_kumis_in_the_world.country)
kumis = Kumis(227,"Белый")
print(kumis.ferment(14))