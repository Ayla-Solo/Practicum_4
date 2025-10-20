a = input("Собака короткошерстой породы? ").lower()
b1 = input(" Рост собаки менее 50 см? ").lower()
b2 = b1
c1 = input("У собаки короткий хвост? ").lower()
c2 = input("Собака весит более 50 кг? ").lower()
c3 = input("У собаки доброжелательный характер? ").lower()
c4 = input("У собаки рост менее 70 см? ").lower()
d1 = input("У собаки длинные уши? ").lower()
d2 = d1
d3 = input("Окрас рыжий с белыми отметинами? ").lower()
e1 = input("У собаки короткое тело? ").lower()
e2 = input("Белоснежный окрас? ").lower()


if a == "да" and b1 == "да" and c1 == "да":
    print("английский бульдог")
elif a == "да" and b1 == "да" and c1 == "нет" and d1 == "да":
    print("гончая")
elif a == "да" and b1 == "да" and c1 == "нет" and d1 == "нет" and e1 == "да":
    print("мопс")
elif a == "да" and b1 == "да" and c1 == "нет" and d1 == "нет" and e1 == "нет":
    print("чихуахуа")
elif a == "да" and b1 == "нет" and c2 == "да":
    print("датский дог")
elif a == "да" and b1 == "нет" and c2 == "нет":
    print("фоксхаунд")



elif a == "нет" and b2 == "да" and c3 == "да":
    print("кокер-спаниэль")
elif a == "нет" and b2 == "да" and c3 == "нет":
    print("ирландский сеттер")
elif a == "нет" and b2 == "нет" and c4 == "да" and d2 == "да":
    print("большой вандейский грифон")
elif a == "нет" and b2 == "нет" and c4 == "да" and d2 == "нет":
    print("колли")
elif a == "нет" and b2 == "нет" and c4 == "нет" and d3 == "да":
    print("сенбернар")
elif a == "нет" and b2 == "нет" and c4 == "нет" and d3 == "нет" and e2=="да":
    print("ирландский волкодав")
elif a == "нет" and b2 == "нет" and c4 == "нет" and d3 == "нет" and e2=="нет":
    print("ньюфаундленд")

