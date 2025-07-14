from queue import PriorityQueue
import os
import csv

class Dijkstra:
    def __init__(self):
        pass


    def best_path(self, graph:dict, city1: str, city2: str): 

        if (type(city1) != str or type(city2) != str):
            return None
        
        #retirar possíveis espaços 
        city1 = " ".join([word for word in city1.strip(" ").split(" ") if word != ""])
        city2 = " ".join([word for word in city2.strip(" ").split(" ") if word != ""])

        city1 = city1.upper() # padronizar para uppercase
        city2 = city2.upper() # padronizar para uppercase


       
        distances = {}
        previous = {}
        cities = {}

        for key1,value in graph.items():
            cities[key1] = True
            distances[key1] = float('inf')
            previous[key1] = None
            for key2 in value.keys():
                cities[key2]= True
                distances[key2] = float('inf')
                previous[key2] = None

        if (cities.get(city1) is None or cities.get(city2)  is None):
            return "No able path!"
        
        if (city1 == city2):
            return 0.0,[]
        
        pq = PriorityQueue()

        pq.put((0.0, city1))
        
        distances[city1] = 0.0
        while(not pq.empty()):
            current_distance, current_city = pq.get()

            if (distances[current_city] < current_distance):
                continue

            if (graph.get(current_city) is not None):
                for neighbor in graph[current_city]:
                    new_distance = current_distance + graph[current_city][neighbor]

                    if (distances[neighbor] > new_distance):
                        distances[neighbor] = new_distance
                        previous[neighbor] = current_city
                        pq.put((new_distance, neighbor))

        distance_city1_to_city2 = distances[city2]
        path = [city2]

        if (distances[city2] != float('inf')): # Existe um caminho de city1 até city 2
            current_city = city2
            while(current_city != city1):
                if (previous[current_city] != None):
                    current_city = previous[current_city]
                    path.append(current_city)

            path = path[::-1] # inverte o caminho

            
        else:
            return "No able path!"
        

        return distance_city1_to_city2, path

d = Dijkstra()

if __name__ == '__main__':
    print('''Insira o caminho do csv contendo as informações das cidades
             Cada linha do csv deve possuir o formato:
                 nome da cidade referência, cidade vizinha 1, distância até cidade 1, cidade vizinha 2, distância até cidade 2, ....
          ''')
    csv_path = input()
    grafo = dict()

    if os.path.exists(csv_path):
        with open(csv_path, "r", encoding="utf-8") as arquivo_csv:
            cidade_origem = input("Qual o nome da cidade de origem? ").upper()
            cidade_destino = input("Qual o nome da cidade de destino? ").upper()
            leitor = csv.reader(arquivo_csv)
            for linha in leitor:
                if linha == []:
                    break
                dictionary = dict()
                for i in range(1, len(linha), 2):
                    distancia = linha[i+1].replace(",", ".")
                    cidade = linha[i].upper()
                    dictionary[cidade] = float(distancia)
                cidade_ref = linha[0].upper()
                grafo[cidade_ref] = dictionary
            print(d.best_path(grafo, cidade_origem, cidade_destino))
    else:
        print("Arquivo não encontrado")


#graph = {"CAMPINA GRANDE": {"LAGOA SECA": 2, "SÃO JOSÉ DA MATA": 11}, "LAGOA SECA": {"CAMPINA GRANDE": 2, "ESPERANÇA": 3}, "SÃO JOSÉ DA MATA": {"CAMPINA GRANDE": 11, "ESPERANÇA": 10}, "ESPERANÇA": {"SÃO JOSÉ DA MATA": 10, "LAGOA SECA": 3}, "SÃO PAULO": {"TESTE": 2}, "TESTE": {"SÃO PAULO": 2}}

#graph = {'CAMPINA GRANDE': {'LAGOA SECA': 8.8, 'QUEIMADAS': 17.0, 'Puxinanã': 14.6, 'Riachão do Bacamarte': 30.8, 'BOA VISTA': 44.1, 'SOLEDADE': 57.2, 'POCINHNHOS': 29.6, 'Fagundes': 26.9}}

#print(d.best_path(graph, "CAMPINA GRANDE", "POCINHNHOS"))  #Esperado (5, ['CAMPINA GRANDE', 'LAGOA SECA', 'ESPERANÇA'])

# print(d.best_path(graph, "Campina Grande", "Campina Grande")) #Esperado "(0.0,[])"  

# print(d.best_path(graph, "Campina Grande", "João Pessoa")) #Esperado "No able path!"


# print(d.best_path(graph, "Campina Grande", "São Paulo")) #Esperado "No able path!" 

# print(d.best_path(graph, 2, "João Pessoa"))  # Esperado None


