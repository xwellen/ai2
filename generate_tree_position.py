import matplotlib.pyplot as plt
import networkx as nx

def generate_tree_position(tree):
    for i, layer in enumerate(nx.topological_generations(tree)):
        for n in layer:
            tree.nodes[n]["layer"] = i
    tree_pos = nx.multipartite_layout(tree, subset_key="layer", align="horizontal")
    for k in tree_pos:
        tree_pos[k][-1] *= -1
    return tree_pos
