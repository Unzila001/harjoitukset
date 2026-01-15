import random
#kolmenumeroisen koodi
koodi_3 = ""
for i in range(3):
    koodi_3 += str(random.randint(0,9))

#nelinumeroisen koodi
koodi_4 = ""
for i in range(4):
    koodi_4 += str(random.randint(1,6))

#Tulos
print ("Kolmenumeroisen koodi:", koodi_3)
print ("nelinumeroisen koodi:", koodi_4)