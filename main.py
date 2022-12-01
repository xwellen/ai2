# %% read data from csv and show graph
import os

import matplotlib.pyplot as plt
import networkx as nx

os.environ["SOURCE_NODE"] = "Брест"
os.environ["DESTINATION_NODE"] = "Казань"

SOURCE_NODE = os.getenv("SOURCE_NODE")  # Брест
DESTINATION_NODE = os.getenv("DESTINATION_NODE")  # Казань

graph_edges = list()
with open("data.csv", "r") as dataset:
    for line in dataset.readlines():
        e = line.split(";")
        graph_edges.append([
            e[0],
            e[1],
            int(e[2].replace("\n", ""))
        ])
print(graph_edges)

G = nx.Graph()
for e in graph_edges:
    G.add_edge(e[0], e[1], weight=e[2])

main_pos = nx.spring_layout(G, seed=23)
from draw_graph import draw_graph as dg

dg(G, main_pos, title_string="cities")


# %% bfs
bfs_edges = []
for e in nx.bfs_edges(G, source=SOURCE_NODE):
    bfs_edges.append(e)
    if e.__contains__(DESTINATION_NODE):
        break
print("all bfs edges:")
for e in nx.bfs_edges(G, source=SOURCE_NODE):
    print(e)
print("bfs edges till DESTINATION_NODE:")
for e in bfs_edges:
    print(e)

# %% bfs path on plain graph
from find_path_and_draw import find_path_and_draw as fpd
fpd(G, bfs_edges, main_pos, title_string="bfs path")

# %% bfs draw tree
from generate_tree_position import generate_tree_position as gtp
bfs_tree_ = nx.bfs_tree(G, source=SOURCE_NODE)
pos_bfs_tree = gtp(bfs_tree_)
fpd(bfs_tree_, bfs_edges, pos_bfs_tree, title_string="bfs tree", print_nodes=False)


# %% dfs
dfs_edges = list()
for e in nx.dfs_edges(G, source=SOURCE_NODE):
    dfs_edges.append(e)
    if e.__contains__(DESTINATION_NODE):
        break
print("all dfs edges:")
for e in nx.dfs_edges(G, source=SOURCE_NODE):
    print(e)
print("dfs edges till DESTINATION_NODE:")
for e in dfs_edges:
    print(e)
# %% dfs path on plain graph
from find_path_and_draw import find_path_and_draw as fpd
fpd(G, dfs_edges, main_pos, title_string="dfs path")
# %% dfs draw tree
from find_path_and_draw import find_path_and_draw as fpd
from generate_tree_position import generate_tree_position as gtp
dfs_tree_ = nx.dfs_tree(G, source=SOURCE_NODE)
pos_dfs_tree = gtp(dfs_tree_)
fpd(dfs_tree_, dfs_edges, pos_dfs_tree, title_string="dfs tree", print_nodes=False)
# %% dfs with depth limits 1-13
from generate_tree_position import generate_tree_position as gtp
from find_path_and_draw import find_path_and_draw as fpd
from draw_graph import draw_graph as dg
for L in range(1, 14):
    dfs_tree_ = nx.dfs_tree(G, source=SOURCE_NODE, depth_limit=L)
    tree_pos = gtp(dfs_tree_)
    if dfs_tree_.nodes.__contains__(DESTINATION_NODE):
        fpd(dfs_tree_, list(dfs_tree_.edges), tree_pos, title_string="path found: dfs depth limit="+str(L), mark_red=False)
        fpd(G, list(dfs_tree_.edges), main_pos, title_string="path found: plain dfs depth limit="+str(L))
    else:
        dg(dfs_tree_, tree_pos, title_string="path not found: dfs depth limit="+str(L))


# %% bidirectional
bidirectional_nodes = nx.bidirectional_shortest_path(G, SOURCE_NODE, DESTINATION_NODE)
print("bidirectional path nodes list:")
for node in bidirectional_nodes:
    print(node)

bidirectional_path = list()
for i in range(len(bidirectional_nodes) - 1):
    bidirectional_path.append((bidirectional_nodes[i], bidirectional_nodes[i + 1]))

fpd(G, bidirectional_path, main_pos, title_string="bidirectional", mark_red=False)
