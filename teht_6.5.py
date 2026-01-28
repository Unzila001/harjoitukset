def pois_parittomat(lista):
    tulos = []
    for luku in lista:
        if luku % 2 == 0:
            tulos.append(luku)
    return tulos

#Pääohjelma
luvut  = [2, 5, 9, 12, 20, 34, 55, 78]
karsitum_lista = pois_parittomat(luvut)

print("Alkuperäinen lista:", luvut)
print("Karsittu lista (vain parilliset luvut):", karsitum_lista)