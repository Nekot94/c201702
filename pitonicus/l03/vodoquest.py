qnsver = input("Вы проснулись от увлекательнейшего сна и хотите умыться\n" + \
    "1.умыться\n2.продолжить сон" )
if qnsver == "1":
    print("Вода разъедает тебе лицо. Ты забыл, что ты живёшь в Махачкале.\nПОТРАЧЕНО")
else:
    qnsver = input("Ты проснулся и вернулся в свою никчёмную жизнь.\n1.Вылезти.\n2.Остаться")
    if qnsver == "1":
        print("Украв трактор, ты пересекаешь границу Рашки. Ура, ты в Белорусии.\nПОТРАЧЕНО")
    else: 
        qnsver = input("Ты идёшь чинить Махачкалинские трубы и тут на" + \
            "тебя падают ничестоты\n1. отпрыгнуть\n2.принять судьбу с высоко поднятой головой")
        if qnsver == "1":
            print("От сульбы не уйдешь. Ты летишь в люк. Интересная смерть.\nПОТРАЧЕНО")
        else:
            qnsver = input("Ты чувствуешь, что можешь управлять вселенной, меняешь судьбы миллионов и просыпаешься." + \
                "\n1.умыться\n2.продолжить сон\n3. Позвать автора")
            if qnsver == "1":
                print("А водичка то вкусная.\n ПОБЕДА!!!")
            elif qnsver == "2":
                print("Ты теперь король махачкилинских труб. Они кланяютсе тебе. А ты танцуешь.\nХЭППИ ЭНД" + \
                    "\nКстати - трубы это ложь!")
            else:
                print("Ты благодаришь, этого красавцва, что облил тебя нечистотами.\nПОТРАЧЕНО")