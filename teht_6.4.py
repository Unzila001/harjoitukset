def lista_summa(luvut):
    summa = 0
    for num in luvut:
        summa += num
    return summa

#Pääohjelma
luvut = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
tulos = lista_summa(luvut)
print("Summa", tulos)