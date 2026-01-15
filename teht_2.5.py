#massan mittayksiköt
leiviskä = float(input("Anna leiviskät.\n"))
naula = float(input("Anna naulat.\n"))
luoti = float(input("Anna luodit.\n"))

leiviskä_nauloina = 20
naula_luoteina = 32
luoti_gramma = 13.3

#Convert grammoiksi
kokonais_luodit = (leiviskä * leiviskä_nauloina * naula_luoteina) + (naula * naula_luoteina) + luoti
kokonais_grammat = (kokonais_luodit * luoti_gramma)

#gramma ja kilogramma
kilogrammat = int(kokonais_grammat // 1000)
grammat = int(kokonais_grammat % 1000)

#Tulos
print("Massa nykymittojen mukaan:")
print(f"{kilogrammat} kilogrammaa ja {grammat:.2f} grammaa.")