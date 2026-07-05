import matplotlib.pyplot as plt
import networkx as nx 

def create_graphs():
    G1, G2 = nx.Graph(), nx.Graph()

    e1 = [(i, (i+1)%6) for i in range(6)] + [(0,2), (0,3), (1,4), (5,2)]
    e2 = [(i, (i+1)%6) for i in range(5)] + [(i,5) for i in range(1,4)] + [(4,1), (4,0), (2,0), (3,0)]
    G1.add_edges_from(e1); G2.add_edges_from(e2)

    pos1 = {0: (-1,1), 1: (1,1), 2:(2,0), 3:(1, -1), 4:(-1, -1), 5:(-2,0)}
    pos2 = {0: (0,2), 1: (1,1), 2:(1,-1), 3:(-1, -1), 4:(-1, 1), 5:(0,0)}

    return (G1, pos1), (G2, pos2)

def get_sequences(G):
    start_node = sorted(list(G.nodes()))[0]
    
    cycle_edges = nx.find_cycle(G, source=start_node, orientation='ignore')
    path = [edge[0] for edge in cycle_edges] + [cycle_edges[0][0]]
    
    cycles = nx.cycle_basis(G)
    cycles.sort(key=len)
    trail_nodes = cycles[-1] if len(cycles) > 1 else cycles[0]
    trail = trail_nodes + [trail_nodes[0]]
    
    walk = [start_node]
    curr = start_node
    for i in range(10):
        neighbors = sorted(list(G.neighbors(curr)))
        curr = neighbors[(i + 1) % len(neighbors)]
        walk.append(curr)
    
    if walk[-1] != start_node:
        back_path = nx.shortest_path(G, source=walk[-1], target=start_node)
        walk.extend(back_path[1:]) 
    
    return walk, trail, path

def draw(G, pos, ax, seq, title, color):
    nx.draw(G, pos, ax=ax, node_color='lightgrey', edge_color='lightgrey', with_labels=True)

    if seq:
        from collections import Counter
        edge_list = [tuple(sorted((seq[i], seq[i+1]))) for i in range(len(seq)-1)]
        counts = Counter(edge_list)
        
        single_edges = [e for e, c in counts.items() if c == 1]
        multi_edges = [e for e, c in counts.items() if c > 1]
        
        nx.draw_networkx_nodes(G, pos, nodelist=seq, ax=ax, node_color=color)
        
        nx.draw_networkx_edges(G, pos, edgelist=single_edges, ax=ax, edge_color=color, width=2)
        
        dark_colors = {'red': 'darkred', 'green': 'darkgreen', 'blue': 'darkblue'}
        dark_color = dark_colors.get(color, 'black')
        nx.draw_networkx_edges(G, pos, edgelist=multi_edges, ax=ax, edge_color=dark_color, width=5)
        
    ax.set_title(f"{title}\n{seq}")

def main():
    (G1, p1), (G2, p2) = create_graphs()
    
    plt.figure(1)
    ax1, ax2 = plt.subplot(121), plt.subplot(122)
    draw(G1, p1, ax1, None, "Original G1", "grey")
    draw(G2, p2, ax2, None, "Original G2", "grey")

    fig, axes = plt.subplots(2, 3, figsize=(15, 8), num=2)
    for i, (G, p, name) in enumerate([(G1, p1, "G1"), (G2, p2, "G2")]):
        walk, trail, path = get_sequences(G)
        draw(G, p, axes[i,0], walk, f"{name} Walk", "red")
        draw(G, p, axes[i,1], trail, f"{name} Trail", "green")
        draw(G, p, axes[i,2], path, f"{name} Path", "blue")
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
