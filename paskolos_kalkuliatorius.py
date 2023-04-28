class Paskola:
    def __init__(self, paskolos_dydis, metines_palukanos, terminas):
        self.paskolos_dydis = paskolos_dydis
        self.metines_palukanos = metines_palukanos
        self.terminas = terminas

class PaskolosKalkuliatorius:
    def __init__(self, paskola):
        self.paskola = paskola
    
    def calculate_shedule(self):
        # Formulė apskaiciuoti menesio paskolos dydi su palukanom
        # bendra palukanu formule
        # Metams P = r(P*V) / 1-(1+r)**-n
        # Menesiams P = a(r/n)) / 1-(1+r/n)**-n (naudojama)
        # a = pask.dydis
        # r = metines.palukanos
        # n = menesiai
        mokejimas = self.paskola.paskolos_dydis * (self.paskola.metines_palukanos / self.paskola.terminas) / \
                  (1 - (1 + self.paskola.metines_palukanos / self.paskola.terminas) ** -self.paskola.terminas)
        likutis = self.paskola.paskolos_dydis
        schedule = []

        for menesis in range(self.paskola.terminas):
            palukanos = likutis * self.paskola.metines_palukanos / self.paskola.terminas
            paskolos_dydis = mokejimas - palukanos
            likutis -= paskolos_dydis

            schedule.append({
                "menesis": menesis+1,
                "likutis": likutis,
                "palukanos": palukanos,
                "paskolos_dydis": paskolos_dydis,
                "mokejimas": mokejimas
            })

        return schedule

paskola = Paskola(paskolos_dydis=10000, metines_palukanos=0.05, terminas=12)
kalkuliatorius = PaskolosKalkuliatorius(paskola)
grafikas = kalkuliatorius.calculate_shedule()

print(f"Pradinė paskola: {paskola.paskolos_dydis}")
for menesis in grafikas:
    print(f"Menesis: {menesis['menesis']}")
    print(f"Likutis sumokėjus už {menesis['menesis']} mėnesį: {menesis['likutis']:.2f}")
    print(f"Palukanos: {menesis['palukanos']:.2f}")
    print(f"Paskolos dydis: {menesis['paskolos_dydis']:.2f}")
    print(f"Bendra mėnesinio mokejimo suma: Paskolos dydis + palukanos: {menesis['mokejimas']:.2f}")
    print("--------------")