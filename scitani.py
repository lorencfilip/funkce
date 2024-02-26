def obvod(a, b, c):
    vysledek = a+b+c
    return vysledek

def obsah(a, v):
    vysledek = a/2*v
    return vysledek


print("pro výpočet obvodu, zadejte 1")
print("pro vypocet obsahu, zadejte 2")

volba = input("zadejte vyši volbu: ")

if volba == 1:
    print("vybral jsi si obvod trojuhelniku: ")

    promena1 = input("zadejte proměnou 1: ")
    promena2 = input("zadejte proměnou 2: ")
    promena3 = input("zadejte proměnou 3: ")

    promena1 = int(promena1)
    promena2 = int(promena2)
    promena3 = int(promena3)

    vysledek = obvod(promena1, promena2, promena3)

elif volba == 2:
    print("vybral jsi si obsah trojuhelniku: ")

    promena1 = input("zadejte proměnou 1: ")
    promena2 = input("zadejte proměnou 2: ")


    promena1 = int(promena1)
    promena2 = int(promena2)


print("výsledek je : ",str(vysledek))