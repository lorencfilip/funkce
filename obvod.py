def obvod(a):
    vysledek = 4*a
    return vysledek


def obsah(a):
    vysledek = a**2
    return vysledek


def objem(a):
    vysledek = a**4
    return vysledek

promena1 = int(input("Zadejte proměnou 1: "))

print("pro výpočet obvodu, zadejte 1")
print("pro vypocet obsahu, zadejte 2")
print("pro vypocet objemu kvádru, zadejte 3")

volba = input("zadejte vyši volbu: ")

