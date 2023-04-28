import unittest
from paskolos_kalkuliatorius import Paskola, PaskolosKalkuliatorius

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.paskola = Paskola(paskolos_dydis=10000, metines_palukanos=0.5, terminas=12)
        self.calc = PaskolosKalkuliatorius(self.paskola)
    
    def test_calculator(self):
        paskola = Paskola(paskolos_dydis=10000, metines_palukanos=0.05, terminas=12)
        kalkuliatorius = PaskolosKalkuliatorius(paskola)
        grafikas = kalkuliatorius.calculate_shedule()

        # Patikrinti, ar pirmo mėnesio mokėjimas apskaiciuotas teisingai
        self.assertAlmostEqual(grafikas[0]["likutis"], 9185.59, places=2)
        self.assertAlmostEqual(grafikas[0]["palukanos"], 41.67, places=2)
        self.assertAlmostEqual(grafikas[0]["paskolos_dydis"], 814.41, places=2)
        self.assertAlmostEqual(grafikas[0]["mokejimas"], 856.07, places=2)

if __name__ == '__main__':
    unittest.main()
