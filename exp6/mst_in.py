import matplotlib.pyplot as plt
import networkx as nx

def create_graph():
    G = nx.Graph()
    v = range(1, 10)
    G.add_nodes_from(v)
    
    e = [
        (1, 2, 14), (1, 3, 5), (1, 4, 2), (2, 3, 9), (2, 4, 8),
        (2, 5, 15), (3, 5, 13), (3, 6, 8), (4, 5, 10), (4, 8, 11),
        (5, 6, 1), (5, 7, 7), (5, 8, 5), (6, 7, 10), (6, 9, 11),
        (7, 8, 0), (7, 9, 12), (8, 9, 6)
    ]
    G.add_weighted_edges_from(e)
    return G

def create_mst(G):
    mst = nx.minimum_spanning_tree(G)
    return mst

def main():
    G = create_graph()
    mst = create_mst(G)
    total_cost = mst.size(weight='weight')
    
    fig, ax = plt.subplots(2, figsize=(8, 10))
    pos = {
        1: (-1, 0), 2: (-0.5, 0), 3: (-0.5, 1), 4: (-0.5, -1),
        5: (0, 0), 6: (0.5, 1), 7: (0.5, 0), 8: (0.5, -1), 9: (1, 0),
    }
    
    nx.draw(G, ax=ax[0], pos=pos, with_labels=True, node_color='lightblue')
    edge_labels_G = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels_G, ax=ax[0])
    ax[0].set_title("Original Graph")
    
    nx.draw(mst, ax=ax[1], pos=pos, with_labels=True, node_color='lightgreen')
    edge_labels_mst = nx.get_edge_attributes(mst, "weight")
    nx.draw_networkx_edge_labels(mst, pos, edge_labels=edge_labels_mst, ax=ax[1])
    ax[1].set_title(f"Minimum Spanning Tree (Total Cost: {total_cost})")
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
