import unittest
from src.agent_map import AgentMap
import pandas as pd

class TestAgentMap(unittest.TestCase):

    def setUp(self):
        df_cities = pd.read_csv("data/cities_graph.csv")
        self.am = AgentMap(df_cities)

    def test_best_path_base_case(self):
        self.assertEqual(self.am.best_path("Campina Grande", "Lagoa Seca"), (["Campina Grande", "Lagoa Seca"], 8.8))

    def test_switch_sense(self):
        self.assertEqual(self.am.best_path("Lagoa Seca", "Campina Grande"), (["Lagoa Seca", "Campina Grande"], 8.8))
        self.assertEqual(self.am.best_path("Campina Grande", "Lagoa Seca"), (["Campina Grande", "Lagoa Seca"], 8.8))

    def test_shortest_path_with_multiple_options(self):
        self.assertEqual(self.am.best_path("Campina Grande", "Esperança"), (["Campina Grande", "Lagoa Seca", "São Sebastião de Lagoa de Roça", "Esperança"], 25.7))
        self.assertEqual(self.am.best_path("Campina Grande", "Boqueirão"), (["Campina Grande", "Queimadas", "Caturité", "Boqueirão"], 44.3))

    def test_no_able_path(self):
        self.assertEqual(self.am.best_path("João Pessoa", "New York"), "No able path!")

    def test_shortest_path_with_multiple_options_to_adjacent_city(self):
        self.assertEqual(self.am.best_path("Campina Grande", "Boa Vista"), (["Campina Grande", "Boa Vista"], 44.3))

    def test_inexistent_city(self):
        self.assertEqual(self.am.best_path("Inexistent City", "Lagoa Seca"), "One of the cities doesn't exist!")
        self.assertEqual(self.am.best_path("Campina Grande", "Inexistent City"), "One of the cities doesn't exist!")
        self.assertEqual(self.am.best_path("Inexistent City", "Inexistent City"), "One of the cities doesn't exist!")

    def test_none(self):
        self.assertIsNone(self.am.best_path(None, "Lagoa Seca"))
        self.assertIsNone(self.am.best_path("Lagoa Seca", None))
        self.assertIsNone(self.am.best_path(None, None), None)

    def test_invalid_parameters(self):
        self.assertIsNone(self.am.best_path(0.0, "Lagoa Seca"))
        self.assertIsNone(self.am.best_path("Campina Grande", 0.0))
        self.assertIsNone(self.am.best_path(0.0, 1.1))

        self.assertIsNone(self.am.best_path(2, "Lagoa Seca"))
        self.assertIsNone(self.am.best_path("Campina Grande",3))
        self.assertIsNone(self.am.best_path(2, 3))

        self.assertIsNone(self.am.best_path(False, "Lagoa Seca"))
        self.assertIsNone(self.am.best_path("Campina Grande", True))
        self.assertIsNone(self.am.best_path(True, False))

        self.assertIsNone(self.am.best_path("Rio de Janeiro", ["São Paulo"]))
        self.assertIsNone(self.am.best_path(["Rio de Janeiro"], "São Paulo"))
        self.assertIsNone(self.am.best_path(["Rio de Janeiro"], ["São Paulo"]))

        self.assertIsNone(self.am.best_path("Rio de Janeiro", {"city": "São Paulo"}))
        self.assertIsNone(self.am.best_path({"city": "Rio de Janeiro"}, "São Paulo"))
        self.assertIsNone(self.am.best_path({"city": "Rio de Janeiro"}, {"city": "São Paulo"}))

    def test_same_city(self):
        self.assertEqual(self.am.best_path("João Pessoa", "João Pessoa"), ([], 0.0))
        self.assertEqual(self.am.best_path("Soledade", "Soledade"), ([], 0.0))

    def test_sensitive_case(self):
        self.assertEqual(self.am.best_path("Campina Grande", "lagoa seca"), (["Campina Grande", "Lagoa Seca"], 8.8))
        self.assertEqual(self.am.best_path("campina grande", "Lagoa Seca"), (["Campina Grande", "Lagoa Seca"], 8.8))
        self.assertEqual(self.am.best_path("campina grande", "lagoa seca"), (["Campina Grande", "Lagoa Seca"], 8.8))
        self.assertEqual(self.am.best_path("CAMPINA GRANDE", "LAGOA SECA"), (["Campina Grande", "Lagoa Seca"], 8.8))
        self.assertEqual(self.am.best_path("campina grande", "LAGOA SECA"), (["Campina Grande", "Lagoa Seca"], 8.8))
        self.assertEqual(self.am.best_path("CAMPINA GRANDE", "lagoa seca"), (["Campina Grande", "Lagoa Seca"], 8.8))

    def test_extra_space(self):
        self.assertEqual(self.am.best_path("Campina Grande", " Lagoa Seca "), (["Campina Grande", "Lagoa Seca"], 8.8))
        self.assertEqual(self.am.best_path(" Campina Grande ", " Lagoa Seca "), (["Campina Grande", "Lagoa Seca"], 8.8))
        self.assertEqual(self.am.best_path(" Campina Grande", "Lagoa Seca "), (["Campina Grande", "Lagoa Seca"], 8.8))

    def test_new_graph(self):
        self.assertEqual(self.am.best_path("Montadas", "Puxinanã", None), "No able path!")
        self.assertEqual(self.am.best_path("Montadas", "Puxinanã", {}), "No able path!")
        new_graph_ex1 = {'CAMPINA GRANDE': {'Riachão do Bacamarte': 30.8, 'QUEIMADAS': 17.0}}
        self.assertEqual(self.am.best_path("Campina Grande", "Riachão do Bacamarte", new_graph_ex1), (["Campina Grande", "Riachão do Bacamarte"], 30.8))


if __name__ == '__main__':
    unittest.main()
