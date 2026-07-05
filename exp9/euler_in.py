import matplotlib.pyplot as plt
import networkx as nx

def create_graphs():
    G1, G2 = nx.Graph(), nx.Graph()

    e1 = [(i, (i+1)%6) for i in range(6)] + [(0,2), (0,3), (1,4), (5,2)]
    e2 = [(i, (i+1)%6) for i in range(5)] + [(i,5) for i in range(1,4)] + [(4,1), (4,0), (2,0), (3,0)]
    G1.add_edges_from(e1); G2.add_edges_from(e2)

    pos1 = {0: (-1,1), 1: (1,1), 2:(2,0), 3:(1, -1), 4:(-1, -1), 5:(-2,0)}
    pos2 = {0: (0,2), 1: (1,1), 2:(1,-1), 3:(-1, -1), 4:(-1, 1), 5:(0,0)}

    return (G1, pos1, "G1"), (G2, pos2, "G2")

def process_euler(G, name):
    print(f"\n--- Checking {name} ---")

    if nx.is_eulerian(G):
        print(f"{name} has an Euler Circuit!")
        circuit_edges = list(nx.eulerian_circuit(G))
        circuit_nodes = [u for u, v in circuit_edges] + [circuit_edges[0][0]]
        
        for i, (u, v) in enumerate(circuit_edges):
            print(f"Step {i+1}: Traversed edge ({u}, {v})")
        
        print(f"Final Circuit: {circuit_nodes}")
        return circuit_nodes
    else:
        print(f"{name} does not have an Euler Circuit.")
        odd_nodes = [v for v, d in G.degree() if d % 2 != 0]
        if odd_nodes:
            print(f"Reason: Vertices {odd_nodes} have odd degrees.")
        elif not nx.is_connected(G):
            print("Reason: The graph is not connected.")

        return None

def draw_result(G, pos, circuit, name, ax):
    nx.draw(G, pos, ax=ax, node_color='lightgrey', edge_color='lightgrey', with_labels=True)

    if circuit:
        edges = [(circuit[i], circuit[i+1]) for i in range(len(circuit)-1)]
        nx.draw_networkx_nodes(G, pos, nodelist=circuit, ax=ax, node_color='green', node_size=500)
        nx.draw_networkx_edges(G, pos, edgelist=edges, ax=ax, edge_color='green', width=2)
        ax.set_title(f"{name} Euler Circuit\n{circuit}")
    else:
        ax.set_title(f"{name} (No Euler Circuit)")

def main():
    graphs = create_graphs()
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    
    for i, (G, pos, name) in enumerate(graphs):
        circuit = process_euler(G, name)
        draw_result(G, pos, circuit, name, axes[i])
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
