import matplotlib.pyplot as plt 
import networkx as nx 

fig, ax = plt.subplots(1, 3, figsize=(15, 5))

def create_graph():
    nodes = list(range(1, 8))
    cycle_edges = [(i, i % 7 + 1) for i in nodes]

    G1 = nx.Graph()
    G1.add_nodes_from(nodes)
    innr_ring1 = [(i, (i+1)% 7 + 1 ) for i in nodes]
    G1.add_edges_from(cycle_edges + innr_ring1)

    G2 = nx.Graph()
    G2.add_nodes_from(nodes)
    innr_ring2 = [(1,3), (1,6), (2,4), (2,6), (3,5), (4,7), (5,7)]
    G2.add_edges_from(cycle_edges + innr_ring2)

    G3 = nx.Graph()
    G3.add_nodes_from(nodes)
    innr_ring3 = [(1,4), (1,5), (2,6), (2,7), (3,5), (3,7), (4,6)]
    G3.add_edges_from(cycle_edges + innr_ring3)

    return G1, G2, G3

def plot_graph(g, idx, title):
    pos = nx.circular_layout(g)
    nx.draw(
            g,
            pos=pos,
            ax=ax[idx],
            with_labels=True,
            node_color="cyan",
            edge_color="blue"
            )
    ax[idx].set_title(title)

def is_iso(g1, g2):
    GM = nx.isomorphism.GraphMatcher(g1, g2)
    if GM.is_isomorphic():
        print("Graphs are Isomorphic")
        print(f"|v| = {g1.number_of_nodes()}   |e| = {g1.number_of_edges()}")
        print(f"Mapping: {GM.mapping}")
    else:
        print("Graphs are NOT Isomorphic")

def main():
    g1, g2, g3 = create_graph()

    print("\n--- For G1 n G2 ---")
    is_iso(g1, g2)
    print("\n--- For G2 n G3 ---")
    is_iso(g2, g3)
    print("\n--- For G1 n G3 ---")
    is_iso(g1, g3)

    plot_graph(g1, 0, "G1")
    plot_graph(g2, 1, "G2")
    plot_graph(g3, 2, "G3")

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
