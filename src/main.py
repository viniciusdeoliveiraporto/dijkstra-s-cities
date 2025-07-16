from utils import convert_df_to_graph
import pandas as pd

df_cities = pd.read_csv("data/cities.csv")
cities_graph = convert_df_to_graph(df_cities)
print(cities_graph)