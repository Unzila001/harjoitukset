vuodenajat =(
    "Talvi",  # tamikuu
    "Talvi",  # helmikuu
    "Kevät",  # maaliskuu
    "Kevät",  # huhtikuu
    "Kevät",  # toukokuu
    "Kesä",  # kesäkuu
    "Kesä",  # heinäkuu
    "Kesä",  # elokuu
    "Syksy",  # syyskuu
    "Syksy",  # lokakuu
    "Syksy",  # marraskuu
    "Talvi"   # joulukuu
)
kuukausi = int(input("Anna kuukauden numero (1–12): "))

if 1 <= kuukausi <= 12:
    print(vuodenajat[kuukausi - 1])
else:
    print("Virheellinen kuukauden numero.")
