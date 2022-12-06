import os

import matplotlib.pyplot as plt
import networkx as nx


def find_path_and_draw(graph, subgraph_edges, pos, title_string="Untitled", print_nodes=True, mark_destination=True,
                       mark_red=True, source_node=os.getenv("SOURCE_NODE"),
                       destination_node=os.getenv("DESTINATION_NODE")):
    G__ = nx.Graph()
    G__.add_edges_from(subgraph_edges)
    current_shortest_path_nodes = nx.shortest_path(G__, source_node, destination_node)
    current_path = []
    for i in range(len(current_shortest_path_nodes) - 1):
        current_path.append((current_shortest_path_nodes[i], current_shortest_path_nodes[i + 1]))
    if print_nodes:
        print("path:")
        print(current_path)
    # drawing

    nx.draw_networkx_edges(graph, pos, edgelist=graph.edges)
    # red color for all subgraph edges
    if mark_red:
        nx.draw_networkx_edges(graph, pos, edgelist=subgraph_edges, edge_color=(1, 0, 0), width=2)
    # yellow color for current path
    nx.draw_networkx_edges(graph, pos, edgelist=current_path, edge_color='#ffee00', width=2)
    # all nodes
    nx.draw_networkx_nodes(graph, pos, node_size=20)
    # source and dest nodes
    if mark_destination:
        nx.draw_networkx_nodes(graph, pos, nodelist=[source_node, destination_node],
                               node_size=20, node_color='#ffee00')
    else:
        nx.draw_networkx_nodes(graph, pos, nodelist=[source_node],
                               node_size=20, node_color='#ffee00')

    path_labels_dict = dict()
    for node in current_shortest_path_nodes:
        path_labels_dict.update({node: str(node)})

    nx.draw_networkx_labels(G__, pos, path_labels_dict, font_size=8)
    plt.title(title_string)
    plt.axis("off")
    plt.show()
