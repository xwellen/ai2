

def maximum_branching_factor(G):
    branches = []
    for node in G.nodes:
        b_now_count = 0
        for edge in G.edges:
            if edge[0] == node:
                b_now_count += 1
        branches.append(b_now_count)
    b = max(branches)
    return b
