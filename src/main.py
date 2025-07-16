import os
import csv
from dijkstra import Dijkstra

if __name__ == '__main__':
    while True:
        print('''Insira o caminho do csv contendo as informações das cidades
                Cada linha do csv deve possuir o formato:
                    nome da cidade referência, cidade vizinha 1, distância até cidade 1, cidade vizinha 2, distância até cidade 2, ....
            ''')
        csv_path = input()
        grafo = {}
        d = Dijkstra()
        
        if os.path.exists(csv_path):
            with open(csv_path, "r", encoding="utf-8") as arquivo_csv:
                cidade_origem = input("Qual o nome da cidade de origem? ").upper()
                cidade_destino = input("Qual o nome da cidade de destino? ").upper()
                leitor = csv.reader(arquivo_csv)
                for linha in leitor:
                    if linha == []:
                        break
                    dictionary = {}
                    for i in range(1, len(linha), 2):
                        distancia = linha[i+1].replace(",", ".")
                        cidade = linha[i].upper()
                        dictionary[cidade] = float(distancia)
                    cidade_ref = linha[0].upper()
                    grafo[cidade_ref] = dictionary
                print(d.best_path(grafo, cidade_origem, cidade_destino))
        else:
            print("Arquivo não encontrado")

        escolha = input("Digite 0 para sair do programa e qualquer outra coisa para continuar: ")
        if escolha == "0":
            break
        


