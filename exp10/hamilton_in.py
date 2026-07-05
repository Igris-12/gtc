import matplotlib.pyplot as plt
import networkx as nx
import networkx.algorithms.approximation as approx

def create_graphs():
    G1 = nx.Graph()
    G1.add_nodes_from(range(0, 6))
    e1_edges = [(i, (i+1)%6) for i in range(6)] + [(0,2), (0,3), (1,4), (5,2)]
    G1.add_edges_from(e1_edges)
    
    G2 = nx.Graph()
    G2.add_nodes_from(range(0, 6))
    e2_edges = [(i, (i+1)%6) for i in range(5)] + [(i,5) for i in range(1,4)] + [(4,1), (4,0), (2,0), (3,0)]
    G2.add_edges_from(e2_edges)

    pos1 = { 0: (-1,1), 1: (1,1), 2:(2,0), 3:(1, -1), 4:(-1, -1), 5:(-2,0) }
    pos2 = { 0: (0,2), 1: (1,1), 2:(1,-1), 3:(-1, -1), 4:(-1, 1), 5:(0,0) }

    return [
        {"name": "Graph 1", "G": G1, "pos": pos1},
        {"name": "Graph 2", "G": G2, "pos": pos2}
    ]

def find_hamiltonian_nx(G):
    nodes = list(G.nodes())
    n = len(nodes)
    
    complete_G = nx.complete_graph(nodes)
    for u, v in complete_G.edges():
        complete_G[u][v]['weight'] = 1 if G.has_edge(u, v) else 1000
            
    try:
        cycle = approx.traveling_salesman_problem(complete_G, weight='weight')
        
        total_weight = sum(complete_G[cycle[i]][cycle[i+1]]['weight'] for i in range(len(cycle)-1))
        if total_weight == n:
            return cycle
    except:
        pass
    return None

def main():
    graphs = create_graphs()
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    
    for i, config in enumerate(graphs):
        G = config["G"]
        name = config["name"]
        pos = config["pos"]
        
        print(f"Finding Hamiltonian Cycle for {name} using NetworkX built-ins...")
        cycle = find_hamiltonian_nx(G)
        
        nx.draw(G, pos, ax=axes[i], with_labels=True, node_color='lightgreen', edge_color='gray')
        if cycle:
            print(f"{name}: Found {cycle}")
            edges = [(cycle[j], cycle[j+1]) for j in range(len(cycle)-1)]
            nx.draw_networkx_edges(G, pos, edgelist=edges, ax=axes[i], edge_color='red', width=3)
            axes[i].set_title(f"{name}: Hamiltonian Cycle\n{cycle}")
        else:
            print(f"{name}: No Hamiltonian Cycle found.")
            axes[i].set_title(f"{name}: No Hamiltonian Cycle")
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
