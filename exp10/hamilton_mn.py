import matplotlib.pyplot as plt
import networkx as nx

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

def find_hamiltonian_cycle(G):
    nodes = list(G.nodes())
    n = len(nodes)
    if n == 0: return None
    
    start_node = nodes[0]
    path = [start_node]
    
    def backtrack(curr):
        if len(path) == n:
            if G.has_edge(path[-1], start_node):
                return path + [start_node]
            return None
        
        for neighbor in G.neighbors(curr):
            if neighbor not in path:
                path.append(neighbor)
                result = backtrack(neighbor)
                if result:
                    return result
                path.pop()
        return None

    return backtrack(start_node)

def draw_cycle(G, pos, cycle, name, ax):
    nx.draw(G, pos, ax=ax, with_labels=True, node_color='lightblue', edge_color='gray', node_size=500)
    if cycle:
        edges = [(cycle[i], cycle[i+1]) for i in range(len(cycle)-1)]
        nx.draw_networkx_edges(G, pos, edgelist=edges, ax=ax, edge_color='red', width=3)
        ax.set_title(f"{name}: Hamiltonian Cycle Found\n{cycle}")
    else:
        ax.set_title(f"{name}: No Hamiltonian Cycle Found")

def main():
    graphs = create_graphs()
    fig, axes = plt.subplots(1, 2, figsize=(12, 6))
    
    for i, config in enumerate(graphs):
        G = config["G"]
        name = config["name"]
        pos = config["pos"]
        
        print(f"Finding Hamiltonian Cycle for {name}...")
        cycle = find_hamiltonian_cycle(G)
        
        if cycle:
            print(f"Found Cycle: {cycle}")
        else:
            print("No Hamiltonian Cycle exists.")
            
        draw_cycle(G, pos, cycle, name, axes[i])
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
