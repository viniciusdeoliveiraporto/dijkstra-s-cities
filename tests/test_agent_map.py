import unittest
import pandas as pd
from src.agent_map import AgentMap
from src.utils import convert_df_to_graph

class TestAgentMap(unittest.TestCase):

    def setUp(self):
        df_cities = pd.read_csv("data/cities.csv")
        cities_graph = convert_df_to_graph(df_cities)
        self.am = AgentMap(cities_graph)

    def test_best_path_base_case(self):
        self.assertEqual(self.am.best_path("Campina Grande", "Lagoa Seca"), (["CAMPINA GRANDE", "LAGOA SECA"], 8.8))
        self.assertEqual(self.am.best_path("João Pessoa", "Cabedelo"), (["JOÃO PESSOA", "CABEDELO"], 12.4))
        self.assertEqual(self.am.best_path("Patos", "São Mamede"), (["PATOS", "SÃO MAMEDE"], 24.6))

    def test_switch_sense(self):
        self.assertEqual(self.am.best_path("Lagoa Seca", "Campina Grande"), (["LAGOA SECA", "CAMPINA GRANDE"], 8.8))
        self.assertEqual(self.am.best_path("Campina Grande", "Lagoa Seca"), (["CAMPINA GRANDE", "LAGOA SECA"], 8.8))
        self.assertEqual(self.am.best_path("Cabedelo", "João Pessoa"), (["CABEDELO", "JOÃO PESSOA"], 12.4))

    def test_shortest_path_with_multiple_options(self):
        self.assertEqual(self.am.best_path("Campina Grande", "Boqueirão"), (["CAMPINA GRANDE", "QUEIMADAS", "BOQUEIRÃO"], 46.2))
        self.assertEqual(self.am.best_path("Campina Grande", "Esperança"), (["CAMPINA GRANDE", "LAGOA SECA", "ESPERANÇA"], 25.8))
        self.assertEqual(self.am.best_path("Campina Grande", "João Pessoa"), 
                         (["CAMPINA GRANDE", "RIACHÃO DO BACAMARTE", "SANTA RITA", "JOÃO PESSOA"], 131.8))
        self.assertEqual(self.am.best_path("Campina Grande", "Patos"), 
                         (["CAMPINA GRANDE", "SOLEDADE", "JUAZEIRINHO", "ASSUNÇÃO", "SALGADINHO", "AREIA DE BARAÚNAS", "PATOS"], 175.2))
        self.assertEqual(self.am.best_path("Campina Grande", "Lucena"), (["CAMPINA GRANDE", "RIACHÃO DO BACAMARTE", "SANTA RITA", "LUCENA"], 157.9))
        self.assertEqual(self.am.best_path("Queimadas", "Esperança"), (["QUEIMADAS", "CAMPINA GRANDE", "LAGOA SECA", "ESPERANÇA"], 42.8))

    def test_no_able_path(self):
        self.assertEqual(self.am.best_path("João Pessoa", "New York"), "No able path!")
        self.assertEqual(self.am.best_path("Campina Grande", "London"), "No able path!")

    def test_shortest_path_with_multiple_options_to_adjacent_city(self):
        self.assertEqual(self.am.best_path("Campina Grande", "Boa Vista"), (["CAMPINA GRANDE", "BOA VISTA"], 44.1))
        self.assertEqual(self.am.best_path("Campina Grande", "Cabaceiras"), (["CAMPINA GRANDE", "BOA VISTA", "CABACEIRAS"], 75.6))

    def test_inexistent_city(self):
        self.assertEqual(self.am.best_path("Inexistent City", "Lagoa Seca"), "One of the cities doesn't exist in the file!")
        self.assertEqual(self.am.best_path("Campina Grande", "Inexistent City"), "One of the cities doesn't exist in the file!")
        self.assertEqual(self.am.best_path("Inexistent City", "Inexistent City"), "One of the cities doesn't exist in the file!")

    def test_none(self):
        self.assertIsNone(self.am.best_path(None, "Lagoa Seca"))
        self.assertIsNone(self.am.best_path("Lagoa Seca", None))
        self.assertIsNone(self.am.best_path(None, None))

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

        new_graph_ex1 = 0.0
        self.assertIsNone(self.am.best_path("Campina Grande", "Boa Vista", new_graph_ex1))
        self.assertIsNone(self.am.best_path(0.0, "Boa Vista", new_graph_ex1))
        self.assertIsNone(self.am.best_path("Campina Grande", 0.0, new_graph_ex1))
        self.assertIsNone(self.am.best_path(0.0, 0.0, new_graph_ex1))

        new_graph_ex2 = 2
        self.assertIsNone(self.am.best_path("Campina Grande", "Boa Vista", new_graph_ex2))
        self.assertIsNone(self.am.best_path(2, "Boa Vista", new_graph_ex2))
        self.assertIsNone(self.am.best_path("Campina Grande", 2, new_graph_ex2))
        self.assertIsNone(self.am.best_path(2, 2, new_graph_ex2))

        new_graph_ex3 = False
        self.assertIsNone(self.am.best_path("Campina Grande", "Boa Vista", new_graph_ex3))
        self.assertIsNone(self.am.best_path(False, "Boa Vista", new_graph_ex3))
        self.assertIsNone(self.am.best_path("Campina Grande", False, new_graph_ex3))
        self.assertIsNone(self.am.best_path(False, False, new_graph_ex3))

        new_graph_ex4 = []
        self.assertIsNone(self.am.best_path("Campina Grande", "Boa Vista", new_graph_ex4))

        new_graph_ex5 = ()
        self.assertIsNone(self.am.best_path("Campina Grande", "Boa Vista", new_graph_ex5))

    def test_same_city(self):
        self.assertEqual(self.am.best_path("João Pessoa", "João Pessoa"), ([], 0.0))
        self.assertEqual(self.am.best_path("Soledade", "Soledade"), ([], 0.0))

    def test_sensitive_case(self):
        self.assertEqual(self.am.best_path("Campina Grande", "lagoa seca"), (["CAMPINA GRANDE", "LAGOA SECA"], 8.8))
        self.assertEqual(self.am.best_path("campina grande", "Lagoa Seca"), (["CAMPINA GRANDE", "LAGOA SECA"], 8.8))
        self.assertEqual(self.am.best_path("campina grande", "lagoa seca"), (["CAMPINA GRANDE", "LAGOA SECA"], 8.8))
        self.assertEqual(self.am.best_path("CAMPINA GRANDE", "LAGOA SECA"), (["CAMPINA GRANDE", "LAGOA SECA"], 8.8))
        self.assertEqual(self.am.best_path("campina grande", "LAGOA SECA"), (["CAMPINA GRANDE", "LAGOA SECA"], 8.8))
        self.assertEqual(self.am.best_path("CAMPINA GRANDE", "lagoa seca"), (["CAMPINA GRANDE", "LAGOA SECA"], 8.8))

    def test_extra_space(self):
        self.assertEqual(self.am.best_path("Campina Grande", " Lagoa Seca "), (["CAMPINA GRANDE", "LAGOA SECA"], 8.8))
        self.assertEqual(self.am.best_path(" Campina Grande ", " Lagoa Seca "), (["CAMPINA GRANDE", "LAGOA SECA"], 8.8))
        self.assertEqual(self.am.best_path(" Campina Grande", "Lagoa Seca "), (["CAMPINA GRANDE", "LAGOA SECA"], 8.8))

    def test_new_graph(self):
        self.assertEqual(self.am.best_path("Campina Grande", "Boqueirão", None), (["CAMPINA GRANDE", "QUEIMADAS", "BOQUEIRÃO"], 46.2))
        self.assertEqual(self.am.best_path("Montadas", "Puxinanã", {}), "One of the cities doesn't exist in the file!")
        new_graph_ex1 = {'KEHL': {'ESTRASBURGO': 5.8}}
        self.assertEqual(self.am.best_path("KEHL", "ESTRASBURGO", new_graph_ex1), (["KEHL", "ESTRASBURGO"], 5.8))

if __name__ == '__main__':
    unittest.main()
