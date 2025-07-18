"""
Módulo de métricas do algoritmo, no qual os resultados obtidos são comparados
com a distância em linha reta entre as cidades selecionadas para teste.
Autor: João Matheus Villarim
Data: Julho 2025
"""
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
import matplotlib.pyplot
import pandas as pd
from agent_map import AgentMap
from utils import convert_df_to_graph
from random import randint
from numpy import mean
from scipy import stats
import matplotlib

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

#main
cities = getCitiesFromCsv()
coordinates = getCoordinatesFromCsv()
df_cities = pd.read_csv("../data/cities.csv") #dataframe para algoritmo

if not df_cities.empty:
  cities_graph = convert_df_to_graph(df_cities)
  am = AgentMap(cities_graph)
  dijkstra_results = []
  straightline_results = []

  for comparison in range(100): #comparações entre cidades aleatórias
    origin = cities[randint(0, 61)]
    destination = cities[randint(0, 61)]

    dijkstra_distance = getDijkstraDistance(origin, destination, am)
    if isinstance(dijkstra_distance, float):
      dijkstra_results.append(dijkstra_distance)

      straightline_distance = getStraightLineDistance(coordinates, origin, destination)
      straightline_results.append(straightline_distance)
  
  #obter as estatísticas
  #dijkstra
  dijkstra_mean = mean(dijkstra_results)
  df = len(dijkstra_results) - 1
  scale = stats.sem(dijkstra_results)
  dijkstra_confidence_interval = stats.t.interval(confidence=0.95,
                                                  df=df,
                                                  scale=scale,
                                                  loc=dijkstra_mean)

  #linha reta
  straightline_mean = mean(straightline_results)
  df = len(straightline_results) - 1
  scale = stats.sem(straightline_results)
  straightline_confidence_interval = stats.t.interval(confidence=0.95,
                                                      df=df,
                                                      scale=scale,
                                                      loc=straightline_mean)
  
  print(f"Intervalo de confiança de Dijkstra: {dijkstra_confidence_interval[0]} a {dijkstra_confidence_interval[1]}")
  print(f"Intervalo de confiança de linha reta: {straightline_confidence_interval[0]} a {straightline_confidence_interval[1]}")

  #gráfico
  labels = ["Algoritmo de Dijkstra", "Distância em linha reta"]
  means = [dijkstra_mean, straightline_mean]

  dijkstra_error = dijkstra_mean - dijkstra_confidence_interval[0]
  straightline_error = straightline_mean - straightline_confidence_interval[0]
  errors = [dijkstra_error, straightline_error]

  fig, ax = matplotlib.pyplot.subplots(figsize=(10, 7))

  ax.bar(x=labels,
       height=means,
       yerr=errors,
       capsize=10,
       color=['blue', 'green'],
       alpha=0.7,
       edgecolor='black')

  ax.set_ylabel("Distância Média (km)", fontsize=12)
  ax.set_title("Comparação de Distâncias com Intervalo de Confiança (95%)", fontsize=15, pad=20)
  ax.set_ylim(0, max(means) * 1.2)
  ax.yaxis.grid(True, linestyle='--', which='major', color='grey', alpha=0.3)

  for i, media in enumerate(means):
    ax.text(i, media + 2, f'{media:.2f}', ha='center', va='bottom', fontsize=11, fontweight='bold')

  matplotlib.pyplot.tight_layout()
  matplotlib.pyplot.savefig("../data/grafico.png")