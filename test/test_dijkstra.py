import unittest
from src.dijkstra import dijkstra

class test_dijkstra(unittest.TestCase):

    def setUp(self):
        self.dk = dijkstra()

    def test_base_case(self):
        self.assertEqual(self.dk.best_path("Campina Grande", "Lagoa Seca"), 8.8)

    def test_shortest_path_with_multiple_options(self):
        self.assertEqual(self.dk.best_path("Campina Grande", "Esperança"), 25.7)
        self.assertEqual(self.dk.best_path("Recife", "Salgueiro"), 513.0)

    def test_no_able_path(self):
        self.assertIsNone(self.dk.best_path("João Pessoa", "New York"), "No able path!")

    def test_None(self):
        self.assertIsNone(self.dk.best_path(None, "Lagoa Seca"), None)
        self.assertIsNone(self.dk.best_path("Lagoa Seca", None), None)

    def test_Invalid_parameters(self):
        self.assertIsNone(self.dk.best_path(0.0, "Lagoa Seca"), None)
        self.assertIsNone(self.dk.best_path("Campina Grande", 0.0), None)
        self.assertIsNone(self.dk.best_path(0.0, 1.1), None)
        self.assertIsNone(self.dk.best_path(2, "Lagoa Seca"), None)
        self.assertIsNone(self.dk.best_path("Campina Grande",3), None)
        self.assertIsNone(self.dk.best_path(2, 3), None)
        self.assertIsNone(self.dk.best_path(False, "Lagoa Seca"), None)
        self.assertIsNone(self.dk.best_path("Campina Grande", True), None)
        self.assertIsNone(self.dk.best_path(True, False), None)



if __name__ == '__main__':
    unittest.main()