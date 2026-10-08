
def evaluer_temperature(temperature):
    if temperature < 0:
        print(f"{temperature}°C : gel")
    elif temperature < 15:
        print(f"{temperature}°C : froid")
    elif temperature < 25:
        print(f"{temperature}°C : doux")
    else:
        print(f"{temperature}°C : chaud")


evaluer_temperature(-3)
evaluer_temperature(0)
evaluer_temperature(15)
evaluer_temperature(31)


def est_bissextile(annee):
    if annee % 4 == 0 and (annee % 100 != 0 or annee % 400 == 0):
        print(f"{annee} : bissextile")
    else:
        print(f"{annee} : non bissextile")

est_bissextile(2024)
est_bissextile(1900)
est_bissextile(2000)