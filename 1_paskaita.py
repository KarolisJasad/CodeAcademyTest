# print('Sveiki kolegos!')

# x = int(input("Įveskite pirmą skaičių: "))
# y = int(input("Įveskite antrą skaičių: "))
# suma = x+y

# print('Jusu skaiciai', x,y)
# print('Skaiciu suma', suma)

# def ar_lyginis(skaicius):
#     if skaicius % 2 == 0:
#         print(skaicius, "yra lyginis")
#         return True
#     else:
#         print(skaicius, "nera lyginis")
#         return False

# ar_lyginis(5)

# a = 6
# b = 5.23
# c = 3 + 4j

# print(a, type(a))
# print(b, type(b))
# print(c, type(c))

# x = 5
# y = 3.5
# z = 4 + 4j
# # y = z

# atsakymas1 = x+y
# atsakymas2 = x-y
# atsakymas3 = x*y*y
# atsakymas4 = x/y
# atsakymas5 = x**y

# print(atsakymas1)
# print(atsakymas2)
# print(atsakymas3)
# print(atsakymas4)
# print(atsakymas5)

# a = 10
# b = 5

# atsakymasa = a // b
# atsakymasb = a % b

# print(atsakymasa)
# print(atsakymasb)



#                           IF
# Pirma uzduotis 
# skaicius = int(input("Įveskite tikrinamą skaičių: "))
# def ar_teigiamas(skaicius):
#     if skaicius > 0:
#         print(skaicius, "yra teigiamas")
#         return True
#     else:
#         print(skaicius, "nera teigiamas")
#         return False

# ar_teigiamas(skaicius)

# #Antra uzduotis
# def ar_tarpe(skaicius):
#     if skaicius >=5 and skaicius <=10:
#         print(skaicius, "yra tarp 5 ir 10")
#         return True
#     else:
#         print(skaicius, "nera tarp 5 ir 10")
#         return False

# ar_tarpe(skaicius)

# #Trecia uzduotis
# skaicius1 = int(input("Įveskite pirmąjį tikrinamą skaičių: "))
# skaicius2 = int(input("Įveskite antrąjį tikrinamą skaičių: "))
# def ar_didesnis(skaicius1, skaicius2):
#     if skaicius1 >0 and skaicius2 >0:
#         print("Abu skaičiai yra didesni nei 0")
#         return True
#     else:
#         print("Bent vienas skaičius yra neigiamas arba lygus 0")
#         return False

# ar_didesnis(skaicius1, skaicius2)

# #Ketvirta uzduotis
# skaicius1 = int(input("Įveskite pirmąjį tikrinamą skaičių: "))
# skaicius2 = int(input("Įveskite antrąjį tikrinamą skaičių: "))
# def ar_vienaslyginis(skaicius1, skaicius2):
#     if skaicius1 % 2 == 0 or skaicius2 % 2 == 0:
#         print("Bent vienas skaičius yra lyginis")
#         return True
#     else:
#         print("Abu skaičiai yra nelyginiai")
#         return False

# ar_vienaslyginis(skaicius1, skaicius2)



#                       Eilutės
# 1 Uzduotis
# tekstas = input("Įveskite tekstą ")
# print(tekstas[0], " Pirmas simbolis")
# print(tekstas[-1], " Paskutinis simbolis")

# # 2 Uzduotis
# knyga = "Dievų miškas"
# print(knyga[:5], " pirmos penkios raidės knygos")

# 3 Uzduotis
# citata = "Nesugalvoju"
# print(citata[-3:], " paskutinės trys raidės")

# 4 uzduotis
# tekstas1 = input("Įveskite pirmą žodį ")
# # tekstas2 = input("Įveskite antrą žodį ")
# tekstas2 = tekstas1.find(" ")
# atsakymas = tekstas1[0] + ' - ' + tekstas1[tekstas2+1]
# print(atsakymas)

# 5 uzduotis
# tekstas = "Aš esu studentas"
# didziosios_raides = tekstas.upper()
# mazosios_raides = tekstas.lower()
# zodziu_sarasas = ["Aš", "esu", "studentas"]
# sujungimas = ", ".join(zodziu_sarasas)
# zodziu_sarasas = tekstas.split(", ")
# pozicija = tekstas.find("studentas")
# pakeistas_tekstas = tekstas.replace("studentas", "programuotojas")

# print("Pradinis tekstas: ", tekstas)
# print("Upper metodas: ", didziosios_raides)
# print("Lower metodas: ", mazosios_raides)
# print("Join metodas: ", sujungimas)
# print("Split metodas: ", zodziu_sarasas)
# print("Find metodas: ", pozicija)
# print("Replace metodas: ", pakeistas_tekstas)

# 6 uzduotis

# vardas = input("Įveskite savo vardą ")
# amzius = int(input("Įveskite savo amžių "))
# atsakymas = (100 - amzius) + 2023
# print(vardas, " sukaks 100 metų", atsakymas,"-aisais")

# 7 uzduotis

# ugis = float(input("Įveskite savo ųgį per kablelį centimetrais "))
# metrais = ugis / 100
# print(f"Jūsų ūgis centimetrais {ugis} cm , ūgis metrais {metrais:.3f} m")

# 8 uzduotis

# atlyginimas = float(input("Įveskite savo gaunąmą atlyginimą "))
# mokestis = float(input("Įveskite taikomą mokestį procentą "))
# atsakymas = atlyginimas - atlyginimas * (mokestis *0.01)
# print(f"Po mokeščių jūsų atlyginimas bus {atsakymas:.2f} e")

# 9 uzduotis

# konversija = input("Įveskite temperatūros tipą (C arba F) ")
# temperatura = float(input("Įveskite temperatūrą "))
# if konversija == "C":
#     fahrenheit = (temperatura * 1.8) + 32
#     print(f"{temperatura} celsijaus konvertuojasi į {fahrenheit:.2f} laipsnių Farenheito")
# elif konversija == "F":
#     celsius = (temperatura - 32) * 5/9
#     print(f"{temperatura} farenheito konvertuojasi į {celsius:.2f} laipsnių celsijaus")
# else:
#     print("Neteisingas konversijos tipas.")

#                       Ciklai

# 1 uzuotis

# maisto_sarasas = ['pica', 'lazanija', 'cepelinai', 'blynai', 'makaronai']
# print(maisto_sarasas)

# 2 uzduotis

# print(maisto_sarasas[0])
# print(maisto_sarasas[2])
# print(maisto_sarasas[4])

# 3 uzduotis

# print(maisto_sarasas[:3])
# print(maisto_sarasas[-2:])
# print(maisto_sarasas[1:4])
# print(maisto_sarasas[::2])

# 4 uzduotis

# maisto_sarasas.append('bandeles')
# print(maisto_sarasas)
# maisto_sarasas.insert(3, 'duona')
# print(maisto_sarasas)
# maisto_sarasas[1] = 'kebabas'
# print(maisto_sarasas)
# maisto_sarasas.pop(0)
# print(maisto_sarasas)
# maisto_sarasas.pop(2)
# print(maisto_sarasas)
# print(maisto_sarasas.index('blynai'))
# print(maisto_sarasas)
# maisto_sarasas.reverse()
# print(maisto_sarasas)

# # 5 uzduotis

# print (len(maisto_sarasas))

# # 6 uzduotis

# print('kebabas' in maisto_sarasas)