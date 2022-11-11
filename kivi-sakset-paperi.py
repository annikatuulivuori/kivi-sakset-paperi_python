import random

pelaaja_voitot = 0
tietokone_voitot = 0
tasapelit = 0

vaihtoehdot = ["kivi", "sakset", "paperi"]

while True:
    pelaaja_valinta = input("Valitse kivi, sakset tai paperi. Jos haluat lopettaa, paina q. > ").lower()
    tietokone_valinta = random.choice(vaihtoehdot)

    if pelaaja_valinta == "q":
        break

    print("Tietokone valitsi", tietokone_valinta)

    if pelaaja_valinta not in vaihtoehdot:
        print("Et valinnut oikein!")
        continue

    if pelaaja_valinta == tietokone_valinta:
        print("Tasapeli!")
        tasapelit += 1

    elif pelaaja_valinta == "kivi" and tietokone_valinta == "sakset":
        print("Voitit!")
        pelaaja_voitot += 1
    
    elif pelaaja_valinta == "sakset" and tietokone_valinta == "paperi":
        print("Voitit!")
        pelaaja_voitot += 1

    elif pelaaja_valinta == "paperi" and tietokone_valinta == "kivi":
        print("Voitit!")
        pelaaja_voitot += 1
    
    else:
        print("Tietokone voitti!")
        tietokone_voitot += 1

print("Päätit pelin")
print("Voitit", pelaaja_voitot, "kertaa")
print("Tietokone voitti", tietokone_voitot, "kertaa")
print("Tasapeli tuli", tasapelit, "kertaa")

