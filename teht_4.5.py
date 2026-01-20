tunnus = "python"
salasana = "rules"
syötetty = 0
while syötetty < 5:
    user = input("Anna tunnus: ")
    user_1 = input("Anna salasana: ")
    syötetty += 1
    if user == tunnus and user_1 == salasana:
        print("Tervetuloa")
        break
    else:
        print("Pääsy evätty")