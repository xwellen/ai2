import matplotlib.pyplot as plt
import networkx as nx

def draw_graph(G, pos, title_string="Untitled"):
    nx.draw_networkx_edges(G, pos, edgelist=G.edges)
    nx.draw_networkx_nodes(G, pos, node_size=20)
    plt.title(title_string)
    plt.axis("off")
    plt.show()