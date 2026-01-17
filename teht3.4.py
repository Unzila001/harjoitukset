
#Kysy käytäjältä vuosiluku
vuosi = int(input("Anna vuosiluku: "))

if vuosi % 400 == 0:
    print("Vuosi on karkauvuosi.")
elif vuosi % 100 == 0:
    print("Vuosi ei ole karkauvuosi.")
elif vuosi % 4 == 0:
    print("Vuosi on karkauvuosi.")
else:
    print("Vuosi ei ole karkauvuosi.")