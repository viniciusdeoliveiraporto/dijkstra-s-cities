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

        if cities.get(city1) is None or cities.get(city2)  is None:
            return "No able path!"
        
        if city1 == city2:
            return 0.0,[]
        
        pq = PriorityQueue()

        pq.put((0.0, city1))
        
        distances[city1] = 0.0
        while not pq.empty():
            current_distance, current_city = pq.get()

            if distances[current_city] < current_distance:
                continue

            if graph.get(current_city) is not None:
                for neighbor in graph[current_city]:
                    new_distance = current_distance + graph[current_city][neighbor]

                    if distances[neighbor] > new_distance:
                        distances[neighbor] = new_distance
                        previous[neighbor] = current_city
                        pq.put((new_distance, neighbor))

        distance_city1_to_city2 = distances[city2]
        path = [city2]

        if distances[city2] != float('inf'): # Existe um caminho de city1 até city 2
            current_city = city2
            while current_city != city1:
                if previous[current_city] is not None:
                    current_city = previous[current_city]
                    path.append(current_city)

            path = path[::-1] # inverte o caminho

            
        else:
            return "No able path!"
        

        return distance_city1_to_city2, path



