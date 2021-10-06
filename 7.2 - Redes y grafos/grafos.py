""" Modulo para la definición de funciones
    para crear y graficar grafos
    Oscar Franco-Bedoya
    Junio 2-2021 
"""

import networkx as nx
import matplotlib.pyplot as plt


def nodos_ejes():
    G = nx.Graph()  # Creación de un grafo dirigido vacio
    G.add_nodes_from([
        "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N",
        "O", "P", "Q"
    ])
    print(G.nodes())  #Imprime la lista de nodos
    G.add_edges_from([
        ("A", "E"), ("A", "D"), ("A", "F"), ("E", "D"), ("E", "B"), ("E", "Q"),
        ("B", "D"), ("B", "F"), ("B", "C"), ("C", "D"), ("C", "Q"), ("C", "O"),
        ("O", "Q"), ("O", "F"), ("F", "Q"), ("Q", "D"), ("F", "P"), ("P", "H"),
        ("P", "I"), ("P", "J"), ("P", "G"), ("P", "K"), ("P", "L"), ("P", "N"),
        ("P", "M"), ("J", "K"), ("K", "L"), ("L", "M")
    ])
    print(G.edges())  #Imprime la lista de ejes
    nx.draw(G, with_labels=True)
    plt.show()


def actores_peliculas():
    G2 = nx.Graph()  # Creación de un grafo no dirigido vacio
    G2.add_nodes_from([
        "Tom Hanks", "Bill Paxton", "Kevin Bacon", "Gari Sinlse", "Ed Harris"
    ])
    print(G2.nodes())  #Imprime la lista de nodos
    G2.add_edges_from([("Ed Harris", "Gari Sinlse"),
                       ("Gari Sinlse", "Kevin Bacon"),
                       ("Gari Sinlse", "Tom Hanks"),
                       ("Gari Sinlse", "Bill Paxton"),
                       ("Kevin Bacon", "Tom Hanks"),
                       ("Bill Paxton", "Tom Hanks")])
    print(G2.edges())  #Imprime la lista de ejes
    nx.draw(G2, with_labels=True)
    plt.show()


def desde_cero():
    GBigBangTheory = nx.Graph()  # Creación de un grafo no dirigido vacio
    GBigBangTheory.add_nodes_from([
        "Leonard Hofstadter", "Sheldon Cooper", "Penny", "Howard Wolowitz",
        "Raj Koothrappali", "Bernadette Rostenkowski", "Amy Farrah Fowler",
        "Stuart Bloom"
    ])
    print(GBigBangTheory.nodes())  #Imprime la lista de nodos
    GBigBangTheory.add_edges_from([("Leonard Hofstadter", "Sheldon Cooper"),
                                   ("Sheldon Cooper", "Penny"),
                                   ("Leonard Hofstadter", "Penny"),
                                   ("Howard Wolowitz", "Raj Koothrappali"),
                                   ("Howard Wolowitz",
                                    "Bernadette Rostenkowski"),
                                   ("Sheldon Cooper", "Amy Farrah Fowler"),
                                   ("Stuart Bloom", "Leonard Hofstadter")])
    print(GBigBangTheory.edges())  #Imprime la lista de ejes
    nx.draw(GBigBangTheory, with_labels=True)
    plt.show()

  