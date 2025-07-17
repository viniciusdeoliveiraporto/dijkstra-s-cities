import pandas as pd

def convert_df_to_graph(df):
    graph = {}

    for _, row in df.iterrows():
        city = str(row.iloc[0]).strip().upper()
        graph.setdefault(city, {})

        for i in range(1, len(row), 2):
            if i + 1 >= len(row):
                break

            neighbor = row.iloc[i]
            distance = row.iloc[i + 1]

            if pd.isna(neighbor) or pd.isna(distance):
                continue

            neighbor = str(neighbor).strip().upper()
            try:
                distance = float(str(distance).replace(',', '.'))
            except ValueError:
                continue

            graph[city][neighbor] = distance
            graph.setdefault(neighbor, {})[city] = distance

    return graph
