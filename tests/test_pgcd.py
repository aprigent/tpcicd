import unittest
from my_arithmetic2_aprigent.pgcd import pgcd
#commentaire
class TestPGCDFunction(unittest.TestCase):

    def test_pgcd_1(self):
        result = pgcd(48, 18)
        self.assertEqual(result, 6)

    def test_pgcd_2(self):
        result = pgcd(60, 48)
        self.assertEqual(result, 12)

    def test_pgcd_3(self):
        result = pgcd(17, 5)
        self.assertEqual(result, 1)

    def test_pgcd_4(self):
        result = pgcd(1024, 256)
        self.assertEqual(result, 256)
    def test_pgcd_5(self):
        result = pgcd(1024, 256)
        self.assertEqual(result, 256)

if __name__ == '__main__':
    unittest.main()
