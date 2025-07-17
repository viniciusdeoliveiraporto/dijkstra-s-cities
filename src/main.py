import pandas as pd
from agent_map import AgentMap
from utils import convert_df_to_graph

if __name__ == '__main__':
    while True:
        """ Caso queira trocar as informações das cidades, altere o arquivo ../data/cities.csv,
            mantendo a estrutura. Cada linha do csv deve possuir o formato:
            nome da cidade referência, cidade vizinha 1, distância até cidade 1, cidade vizinha 2, distância até cidade 2, ...
        """

        df_cities = pd.read_csv("../data/cities.csv")
        if not df_cities.empty:
            cities_graph = convert_df_to_graph(df_cities)
            am = AgentMap(cities_graph)
        
            cidade_origem = input("Qual o nome da cidade de origem? ").upper()
            cidade_destino = input("Qual o nome da cidade de destino? ").upper()
            result = am.best_path(cidade_origem, cidade_destino)
            if isinstance(result, tuple):
                path, distance_city1_to_city2 = result
                print(f"The distance of the best path is {distance_city1_to_city2} Km!\nFollow this path: {path}.")
            else:
                print(result)
        else:
            print("Arquivo não encontrado")

        escolha = input("Digite 0 para sair do programa e qualquer outra coisa para continuar: ")
        if escolha == "0":
            break
        