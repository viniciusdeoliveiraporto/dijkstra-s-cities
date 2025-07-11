import unittest

class test_best_path(unittest.TestCase):

    def test_base_case(self):
        self.assertEqual(best_path("Campina Grande", "Lagoa Seca"), 8.8)

    def test_None(self):
        self.assertIsNone(best_path(8.8, "Lagoa Seca"))

    def test_Invalid(self):
        soma = 2 + 2
        self.assertEqual(soma,4)
        self.assertIsNone(best_path(0.0, "Lagoa Seca"))
        self.assertIsNone(best_path("Campina Grande", 0.0))


if __name__ == '__main__':
    unittest.main()