"""
Módulo de métricas do algoritmo, no qual os resultados obtidos são comparados
com a distância em linha reta entre as cidades selecionadas para teste.
Autor: João Matheus Villarim
Data: Julho 2025
"""
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
import pandas as pd
from agent_map import AgentMap
from utils import convert_df_to_graph
from random import randint

geolocator = Nominatim(user_agent="distance_calculator")

#obter cidades a partir de ../data/cities
def getCitiesFromCsv() -> list:
  cities = []
  try:
    with open("../data/cities.csv") as f:
      firstLine = f.readline() #ignorar a primeira linha
      for line in f.readlines():
        cities.append(line.split(",")[0])
      if "New York" in cities:
        cities.remove("New York") #não pertence à paraíba
  except FileNotFoundError:
    print(f"Erro: ../data/cities.csv não encontrado")
  return cities

#obter coordenadas de cada cidade e salvar em ../data/coordinates.csv
def saveCitiesCoordinates(cities: list) -> dict:
  coordinates = {}
  for city in cities:
    try:
      location = geolocator.geocode(f"{city}, Paraíba, Brazil")
      if location:
        coordinates[city] = (location.latitude, location.longitude)
    except Exception as e:
      print(f"Erro ao obter as coordenadas de {city}: {e}")
  try:
    with open("../data/coordinates.csv", "w") as f:
      f.write("city,latitude,longitude\n")
      for city in coordinates:
        latitude, longitude = coordinates[city]
        f.write(f"{city},{latitude},{longitude}\n")
  except Exception as e:
    print(e)

#obter cidades de ../data/coordinates.csv
def getCoordinatesFromCsv() -> dict:
  coordinates = {}
  try:
    with open("../data/coordinates.csv") as f:
      firstLine = f.readline() #ignorar a primeira linha
      for city in f.readlines():
        name, latitude, longitude = city.split(",")
        coordinates[name] = (float(latitude), float(longitude))
  except Exception as e:
    print(e)
  return coordinates

#utilizando o algoritmo do projeto para obter a distância
def getDijkstraDistance(origin: str, destination: str, agent_map: AgentMap):
  result = agent_map.best_path(origin, destination)
  if isinstance(result, tuple):
    path, distance = result
    return distance
  
#obter distância em linha reta
def getStraightLineDistance(coordinates: dict, origin: str, destination: str):
  return geodesic(coordinates[origin], coordinates[destination]).kilometers

cities = getCitiesFromCsv()
coordinates = getCoordinatesFromCsv()

df_cities = pd.read_csv("../data/cities.csv") #dataframe para algoritmo
if not df_cities.empty:
  cities_graph = convert_df_to_graph(df_cities)
  am = AgentMap(cities_graph)

  for comparison in range(10):
    origin = cities[randint(0, 61)]
    destination = cities[randint(0, 61)]

    dijkstra_distance = getDijkstraDistance(origin, destination, am)
    if isinstance(dijkstra_distance, float):
      print(f"A distância entre {origin} e {destination} é {dijkstra_distance}")
    else:
      print(f"Não há caminho entre {origin} e {destination}")
