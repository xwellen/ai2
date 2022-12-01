# %% inits
import os

import matplotlib.pyplot as plt
import networkx as nx
from find_path_and_draw import find_path_and_draw as fpd

SOURCE_NODE = os.getenv("SOURCE_NODE") # Брест
DESTINATION_NODE = os.getenv("DESTINATION_NODE") # Казань

# %% read data from csv and show graph
G = list()
with open("data.csv", "r") as dataset:
    for line in dataset.readlines():
        e = line.split(";")
        G.append([
            e[0],
            e[1],
            int(e[2].replace("\n", ""))
        ])
print(G)

G_ = nx.Graph()
for e_ in G:
    G_.add_edge(e_[0], e_[1], weight=e_[2])

pos = nx.spring_layout(G_, seed=23)

nx.draw_networkx_edges(G_, pos, edgelist=G_.edges)
nx.draw_networkx_nodes(G_, pos, node_size=20)
plt.axis("off")
plt.show()
# %% bfs
bfs_edges = list()
for e in nx.bfs_edges(G_, source=SOURCE_NODE):
    bfs_edges.append(e)
    if e.__contains__(DESTINATION_NODE):
        break
print("all bfs edges:")
for e in nx.bfs_edges(G_, source=SOURCE_NODE):
    print(e)
print("bfs edges till DESTINATION_NODE:")
for e in bfs_edges:
    print(e)
# %% bfs path on plain graph
fpd(G_, bfs_edges, pos, title_string="bfs path")

# %% bfs draw tree
bfs_tree_ = nx.bfs_tree(G_, source=SOURCE_NODE)
for i, layer in enumerate(nx.topological_generations(bfs_tree_)):
    for n in layer:
        bfs_tree_.nodes[n]["layer"] = i
pos_bfs_tree = nx.multipartite_layout(bfs_tree_, subset_key="layer", align="horizontal")
for k in pos_bfs_tree:
    pos_bfs_tree[k][-1] *= -1
nx.draw_networkx_edges(bfs_tree_, pos_bfs_tree, edgelist=bfs_tree_.edges)
nx.draw_networkx_edges(bfs_tree_, pos_bfs_tree, edgelist=bfs_edges, edge_color=(1, 0, 0), width=2)
nx.draw_networkx_edges(bfs_tree_, pos_bfs_tree, edgelist=bfs_path, edge_color='#ffee00', width=2)
nx.draw_networkx_nodes(bfs_tree_, pos_bfs_tree, node_size=20)
nx.draw_networkx_nodes(bfs_tree_, pos_bfs_tree, nodelist=[SOURCE_NODE, DESTINATION_NODE], node_size=20,
                       node_color='#ffee00')
plt.title("bfs tree")
plt.axis("off")
plt.show()
# %% print bfs edges
print("bfs edges:")
for edge in bfs_tree_.edges:
    print(edge)

# %% bfs draw all
nx.draw_networkx_edges(G_, pos, edgelist=G_.edges)
nx.draw_networkx_edges(G_, pos, edgelist=bfs_edges, edge_color=(1, 0, 0), width=2)
nx.draw_networkx_edges(G_, pos, edgelist=bfs_path, edge_color='#ffee00', width=2)
nx.draw_networkx_nodes(G_, pos, node_size=20)
nx.draw_networkx_nodes(G_, pos, nodelist=[SOURCE_NODE, DESTINATION_NODE], node_size=20, node_color='#ffee00')
plt.title("bfs")
plt.axis("off")
plt.show()

# %% dfs
dfs_edges = list()
for e in nx.dfs_edges(G_, source=SOURCE_NODE):
    dfs_edges.append(e)
    if e.__contains__(DESTINATION_NODE):
        break
print("all dfs edges:")
for e in nx.dfs_edges(G_, source=SOURCE_NODE):
    print(e)
print("dfs edges till DESTINATION_NODE:")
for e in dfs_edges:
    print(e)
# %% find dfs path
G__ = nx.Graph()
G__.add_edges_from(dfs_edges)
dfs_shortest_path_verts = nx.shortest_path(G__, SOURCE_NODE, DESTINATION_NODE)
dfs_path = list()
for i in range(len(dfs_shortest_path_verts) - 1):
    dfs_path.append((dfs_shortest_path_verts[i], dfs_shortest_path_verts[i + 1]))
print("dfs path:")
for e in dfs_path:
    print(e)
# %% dfs tree
dfs_tree_ = nx.dfs_tree(G_, source=SOURCE_NODE)
for i, layer in enumerate(nx.topological_generations(dfs_tree_)):
    for n in layer:
        dfs_tree_.nodes[n]["layer"] = i
pos_dfs_tree = nx.multipartite_layout(dfs_tree_, subset_key="layer", align="horizontal")
for k in pos_dfs_tree:
    pos_dfs_tree[k][-1] *= -1
nx.draw_networkx_edges(dfs_tree_, pos_dfs_tree, edgelist=dfs_tree_.edges)
nx.draw_networkx_edges(dfs_tree_, pos_dfs_tree, edgelist=dfs_edges, edge_color=(1, 0, 0), width=2)
nx.draw_networkx_edges(dfs_tree_, pos_dfs_tree, edgelist=dfs_path, edge_color='#ffee00', width=2)
nx.draw_networkx_nodes(dfs_tree_, pos_dfs_tree, node_size=20)
nx.draw_networkx_nodes(dfs_tree_, pos_dfs_tree, nodelist=[SOURCE_NODE, DESTINATION_NODE], node_size=20,
                       node_color='#ffee00')
plt.title("dfs tree")
plt.axis("off")
plt.show()

# %% dfs draw all
nx.draw_networkx_edges(G_, pos, edgelist=G_.edges)
nx.draw_networkx_edges(G_, pos, edgelist=dfs_edges, edge_color=(1, 0, 0), width=2)
nx.draw_networkx_edges(G_, pos, edgelist=dfs_path, edge_color='#ffee00', width=2)
nx.draw_networkx_nodes(G_, pos, node_size=20)
nx.draw_networkx_nodes(G_, pos, nodelist=[SOURCE_NODE, DESTINATION_NODE], node_size=20, node_color='#ffee00')
plt.title("dfs")
plt.axis("off")
plt.show()


# %% dfs with depth limits 1-11
def show_dfs_path(GRAPH):
    G__ = nx.Graph()
    G__.add_edges_from(GRAPH.edges)
    dfs_shortest_path_verts = nx.shortest_path(G__, SOURCE_NODE, DESTINATION_NODE)
    dfs_path = list()
    for i in range(len(dfs_shortest_path_verts) - 1):
        dfs_path.append((dfs_shortest_path_verts[i], dfs_shortest_path_verts[i + 1]))
    print("dfs path:")
    for e in dfs_path:
        print(e)
    return dfs_path
def show_dfs_tree_w_limit_given(GRAPH, L):
    dfs_tree_ = nx.dfs_tree(GRAPH, source=SOURCE_NODE, depth_limit=L)
    for i, layer in enumerate(nx.topological_generations(dfs_tree_)):
        for n in layer:
            dfs_tree_.nodes[n]["layer"] = i
    pos_dfs_tree = nx.multipartite_layout(dfs_tree_, subset_key="layer", align="horizontal")
    for k in pos_dfs_tree:
        pos_dfs_tree[k][-1] *= -1
    nx.draw_networkx_edges(dfs_tree_, pos_dfs_tree, edgelist=dfs_tree_.edges)
    nx.draw_networkx_nodes(dfs_tree_, pos_dfs_tree, node_size=20)
    nx.draw_networkx_nodes(dfs_tree_, pos_dfs_tree, nodelist=[SOURCE_NODE], node_color='#ffee00',
                           node_size=20)
    if dfs_tree_.nodes.__contains__(DESTINATION_NODE):
        nx.draw_networkx_nodes(dfs_tree_, pos_dfs_tree, nodelist=[DESTINATION_NODE], node_color='#ff0000',
                               node_size=20)
        nx.draw_networkx_edges(dfs_tree_, pos_dfs_tree, edgelist=show_dfs_path(dfs_tree_), edge_color='#ffee00', width=2)
    else:
        print("no path for limit=" + str(L))

    plt.title("dfs tree limit=" + str(L))
    plt.axis("off")
    plt.show()


for l in range(1, 12):
    show_dfs_tree_w_limit_given(G_, l)
# %% dfs with depth limit=8 path

dfs_tree_ = nx.dfs_tree(G_, source=SOURCE_NODE, depth_limit=8)

G__ = nx.Graph()
G__.add_edges_from(dfs_tree_.edges)
dfs_shortest_path_verts = nx.shortest_path(G__, SOURCE_NODE, DESTINATION_NODE)
dfs_path8 = list()
for i in range(len(dfs_shortest_path_verts) - 1):
    dfs_path8.append((dfs_shortest_path_verts[i], dfs_shortest_path_verts[i + 1]))
print("dfs tree limit=8 path:")
for e in dfs_path8:
    print(e)

for i, layer in enumerate(nx.topological_generations(dfs_tree_)):
    for n in layer:
        dfs_tree_.nodes[n]["layer"] = i
pos_dfs_tree = nx.multipartite_layout(dfs_tree_, subset_key="layer", align="horizontal")
for k in pos_dfs_tree:
    pos_dfs_tree[k][-1] *= -1
nx.draw_networkx_edges(dfs_tree_, pos_dfs_tree, edgelist=dfs_tree_.edges)
nx.draw_networkx_nodes(dfs_tree_, pos_dfs_tree, node_size=20)
nx.draw_networkx_nodes(dfs_tree_, pos_dfs_tree, nodelist=[SOURCE_NODE], node_color='#ffee00',
                       node_size=20)
nx.draw_networkx_nodes(dfs_tree_, pos_dfs_tree, nodelist=[DESTINATION_NODE], node_color='#ff0000',
                       node_size=20)

nx.draw_networkx_edges(dfs_tree_, pos_dfs_tree, edgelist=dfs_path8, edge_color='#ffee00', width=2)
plt.title("dfs tree limit=8 path")
plt.axis("off")
plt.show()
# %% dfs with depth limit=8 path all
nx.draw_networkx_edges(G_, pos, edgelist=G_.edges)
nx.draw_networkx_edges(G_, pos, edgelist=dfs_path8, edge_color='#ffee00', width=2)
nx.draw_networkx_nodes(G_, pos, node_size=20)
nx.draw_networkx_nodes(G_, pos, nodelist=[SOURCE_NODE, DESTINATION_NODE], node_size=20, node_color='#ffee00')
plt.title("dfs limit=8 all")
plt.axis("off")
plt.show()
# %% bidirectional
bidirectional_nodes = nx.bidirectional_shortest_path(G_, SOURCE_NODE, DESTINATION_NODE)
print("bidirectional path nodes list:")
for node in bidirectional_nodes:
    print(node)

bidirectional_path = list()
for i in range(len(bidirectional_nodes) - 1):
    bidirectional_path.append((bidirectional_nodes[i], bidirectional_nodes[i + 1]))

nx.draw_networkx_edges(G_, pos, edgelist=G_.edges)
nx.draw_networkx_nodes(G_, pos, node_size=20)
nx.draw_networkx_edges(G_, pos, edgelist=bidirectional_path, edge_color='#ffee00', width=2)
nx.draw_networkx_nodes(G_, pos, nodelist=[SOURCE_NODE, DESTINATION_NODE], node_size=20, node_color='#ffee00')
plt.title("bidirectional")
plt.axis("off")
plt.show()
