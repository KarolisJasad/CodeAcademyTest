import sys
import random

randomskaicius = random.randint(1, 100)
bandymai = 0

print("Sveiki, pasirinkite norimą programą:")
print("A: Skaičiuotuvas")
print("B: Žaidimas `Šilta/Šalta`")

while bandymai < 2:  # Nustatome, kad vartotojas gali spėti tik du kartus
    Pasirinkimas = input("Įveskite norimos programos raidę: ")
    Pasirinkimas = Pasirinkimas.lower() # Konvertuojame atsakymą į mažąsias raides, del sekančio IF patikrinimo

    if Pasirinkimas == "a" or Pasirinkimas == "b":
        print("Jūs pasirinkote", Pasirinkimas)
        break
    else:
        print("Jūs įvedėte blogą pasirinkimą")
        bandymai += 1

if bandymai == 2: # Patikriname ar vartotojas jau atliko du bandymus
    print("Jūs įvedėte blogą pasirinkimą du kartus, programa bus uždaryta.")
    sys.exit() # Sustabdome programą, jei per daug bandymų

if Pasirinkimas == "a": # Paleidžiame žaidimą pagal pasirinkimą
    print("Šis skaičiuotuvas priima tik du skaičius, paprašysiu įvesti po vieną atskirai")
    while True:
        try: # Naudojame Try, kad galėtume patikrinti ar skaičius tinkamai įvestas
           skaicius1 = float(input("Įveskite pirmą skaičių: "))
           skaicius2 = float(input("Įveskite antrą skaičių: "))
           operatorius = input("Įveskite norimą operatorių (+, -, /, *, or **): ")
           if operatorius in ['+', '-', '/', '*', '**']:
               if operatorius == '+':
                    print(skaicius1 + skaicius2)
               elif operatorius == '-':
                    print(skaicius1 - skaicius2)
               elif operatorius == '/':
                    while skaicius1 == 0 or skaicius2 == 0:
                        print("Dalyba iš 0 negalima")
                        sys.exit()
                    print(skaicius1 / skaicius2)
               elif operatorius == '*':
                    print(skaicius1 * skaicius2)
               elif operatorius == '**':
                    print(skaicius1 ** skaicius2)
               break
           else:
            print("Neteisingai pasirinktas operatorius, programa perkraunama, įveskite viską iš naujo")
        except ValueError:  # Patikrina ar vietoj skaičiaus nėra įvestas kitoks simbolis
            print("Neteisingai įvestas skaičius, programa perkraunama, įveskite viską iš naujo")
elif Pasirinkimas == "b":
    print("Pasirinkote programą šilta/šalta, spėsime skaičių nuo 0 iki 100")
while True:
    spejimas = input("Įveskite savo spėjimą: ")

    try:
        spejimas = int(spejimas)
    except ValueError:
        print("Blogai įvestas skaičius, įveskite teisingą skaičių.")
        continue
    
    if spejimas == randomskaicius:
        print("Sveikinu, atspėjote skaičių.")
        break
    elif spejimas < randomskaicius:
        print("Jūsų spėjimas yra žemesnis, bandykite dar kartą")
    elif spejimas > randomskaicius:
        print("Jūsų spėjimas didesnis, bandykite dar kartą")

        