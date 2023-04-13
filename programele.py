import sys

print("Sveiki, pasirinkite norimą programą:")
print("A: Skaičiuotuvas")
print("B: Žaidimas `Šilta/Šalta`")
bandymai = 0
while bandymai < 2:
    Pasirinkimas = input("Įveskite norimos programos raidę: ")
    Pasirinkimas = Pasirinkimas.lower()

    if Pasirinkimas == "a" or Pasirinkimas == "b":
        print("Jūs pasirinkote", Pasirinkimas)
        break
    else:
        print("Jūs įvedėte blogą pasirinkimą")
        bandymai += 1

if bandymai == 2 or Pasirinkimas == "b":
    print("Jūs įvedėte blogą pasirinkimą du kartus, programa bus uždaryta.")
    sys.exit()

if Pasirinkimas == "a":
    print("Šis skaičiuotuvas priima tik du skaičius, paprašysiu įvesti po vieną atskirai")
    while True:
        try:
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
        except ValueError:
            print("Neteisingai įvestas skaičius, programa perkraunama, įveskite viską iš naujo")
        