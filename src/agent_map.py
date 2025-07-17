from queue import PriorityQueue

class AgentMap:
    """Classe para encontrar o menor caminho entre cidades usando Dijkstra."""
    def __init__(self, graph:dict):
        self.graph = graph

    def prepare_graph(self, graph):
        """Prepara as variáveis distances, previous e cities"""
        distances = {}
        previous = {}
        cities = {}
        for origin, neighboor in graph.items():
            cities[origin] = True
            distances[origin] = float('inf')
            previous[origin] = None
            for city in neighboor.keys():
                cities[city]= True
                distances[city] = float('inf')
                previous[city] = None

        return distances, previous, cities
    
    def find_path(self, previous, city1, city2):
        """Reconstrói o caminho que foi percorrido de city2 até voltar à city1"""
        path = [city2]
        current_city = city2
        while current_city != city1:
            if previous[current_city] is not None:
                current_city = previous[current_city]
                path.append(current_city)
        return path[::-1] 

    def best_path(self, city1: str, city2: str, new_graph:dict=None):
        """Retorna a menor distância e o caminho entre duas cidades."""

        if new_graph is not None:
            self.graph = new_graph

        if not isinstance(city1, str) or not isinstance(city2, str) or not isinstance(self.graph, dict):
            return None
        
        # retirar possíveis espaços 
        city1 = " ".join(city1.split())
        city2 = " ".join(city2.split())

        city1 = city1.upper() # padronizar para uppercase
        city2 = city2.upper() # padronizar para uppercase

        distances, previous, cities = self.prepare_graph(self.graph)

        # Verifica se city1 ou city2 não existem
        if (cities.get(city1) is None or cities.get(city2) is None):
            return "One of the cities doesn't exist!"
        
        if city1 == city2:
            return [], 0.0
        
        pq = PriorityQueue()

        pq.put((0.0, city1))
        distances[city1] = 0.0

        while not pq.empty():
            current_distance, current_city = pq.get()
            
            if distances[current_city] < current_distance:
                continue

            if self.graph.get(current_city) is not None:
                for neighbor in self.graph[current_city]:
                    new_distance = current_distance + self.graph[current_city][neighbor]
                    if distances[neighbor] > new_distance:
                        distances[neighbor] = new_distance
                        previous[neighbor] = current_city
                        pq.put((new_distance, neighbor))

        distance_city1_to_city2 = distances[city2]
        path = []
        if distance_city1_to_city2 != float('inf'): # Existe um caminho de city1 até city 2
            path = self.find_path(previous, city1, city2)
        else:
            return "No able path!"
        
        return path, distance_city1_to_city2
