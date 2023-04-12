# 7 Uzduotis
automobiliai = {
    '1' : {
        'marke' : 'BMW',
        'modelis' : 'e46',
        'metai' : '2003',
        'spalva' : 'Juoda',
        'variklis' : 'Benzinas'
    },
    '2': {
        'marke' : 'Audi',
        'modelis' : 'A3',
        'metai' : '2023',
        'spalva' : 'Balta',
        'variklis' : 'Dyzelis'
    },
    '3': {
        'marke' : 'Citroen',
        'modelis' : 'C4',
        'metai' : '2010',
        'spalva' : 'Balta',
        'variklis' : 'Benzinas'

    }}

print("Informacija apie antrąjį automobilį" ,automobiliai['2'])
automobiliai['2']['variklis'] = 'Elektra'
print("Informacija apie antrąjį automobilį" ,automobiliai['2'])
automobiliai[4] = {
        'marke' : 'Tesla',
        'modelis' : 'S',
        'metai' : '2017',
        'spalva' : 'Raudona',
        'variklis' : 'Elektra'
    }
print(automobiliai)
del automobiliai['1']
print(automobiliai)
print(len(automobiliai))

tikrinama_masina = input("Įveskite tikrinamos mašinos modelį ")
if tikrinama_masina in [masina['modelis'] for masina in automobiliai.values()]:
    print(tikrinama_masina," egzistuoja duomenų bazėje")
else:
    print(tikrinama_masina," nėra duomenų bazėje")