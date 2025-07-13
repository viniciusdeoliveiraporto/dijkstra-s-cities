from queue import PriorityQueue

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


        if (graph.get(city1) is None or graph.get(city2) is None):
            return "No able path!"
        
        if (city1 == city2):
            return 0.0,[]
        
        pq = PriorityQueue()

        pq.put((0.0, city1))

        distances = {city: float('inf') for city in graph}
        distances[city1] = 0.0
        previous = {city: None for city in graph}

        
        while(not pq.empty()):
            current_distance, current_city = pq.get()

            if (distances[current_city] < current_distance):
                continue

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

graph = {"CAMPINA GRANDE": {"LAGOA SECA": 2, "SÃO JOSÉ DA MATA": 11}, "LAGOA SECA": {"CAMPINA GRANDE": 2, "ESPERANÇA": 3}, "SÃO JOSÉ DA MATA": {"CAMPINA GRANDE": 11, "ESPERANÇA": 10}, "ESPERANÇA": {"SÃO JOSÉ DA MATA": 10, "LAGOA SECA": 3}, "SÃO PAULO": {"TESTE": 2}, "TESTE": {"SÃO PAULO": 2}}

print(d.best_path(graph, "       Campina           Grande ", "ESPERANÇA"))  #Esperado (5, ['CAMPINA GRANDE', 'LAGOA SECA', 'ESPERANÇA'])

print(d.best_path(graph, "Campina Grande", "Campina Grande")) #Esperado "(0.0,[])"  

print(d.best_path(graph, "Campina Grande", "João Pessoa")) #Esperado "No able path!"


print(d.best_path(graph, "Campina Grande", "São Paulo")) #Esperado "No able path!" 

print(d.best_path(graph, 2, "João Pessoa"))  # Esperado None


