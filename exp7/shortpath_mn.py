import matplotlib.pyplot as plt
import networkx as nx

def create_graph():
    G = nx.Graph()
    edges = [
        (1, 2, 6), (1, 3, 7), (2, 3, 8), (2, 4, 9), (2, 6, 14),
        (3, 4, 5), (3, 5, 4), (4, 5, 6), (4, 6, 10), (5, 7, 7),
        (6, 7, 11), (6, 8, 8), (7, 8, 6)
    ]
    G.add_weighted_edges_from(edges)
    pos = {1: (0, 0), 2: (1, 1), 3: (1, -1), 4: (2, 0), 
           5: (2, -2), 6: (3, 1), 7: (3, -1), 8: (4, 0)}
    return G, pos

def dijkstra(G, start):
    dist = {n: float('inf') for n in G.nodes()}
    dist[start] = 0
    pred = {n: None for n in G.nodes()}
    unvisited = list(G.nodes())
    visited = []
    steps = [{'sel': '-', 'dist': dist.copy(), 'visited': []}]

    while unvisited:
        curr = min(unvisited, key=lambda n: dist[n])
        if dist[curr] == float('inf'): break
        unvisited.remove(curr)
        visited.append(curr)
        
        for nbr in G.neighbors(curr):
            if nbr in unvisited:
                alt = dist[curr] + G[curr][nbr]['weight']
                if alt < dist[nbr]:
                    dist[nbr] = alt
                    pred[nbr] = curr
        steps.append({'sel': curr, 'dist': dist.copy(), 'visited': list(visited)})
    return dist, pred, steps

def print_table(nodes, steps):
    nodes = sorted(list(nodes))
    header = f"{'S':<20} " + " ".join(f"{str(n):<4}" for n in nodes) + "  u(i+1)"
    print(header)

    for s in steps:
        v_set = "{" + ",".join(map(str, sorted(s['visited']))) + "}"
        dists = [f"{str(s['dist'][n]) if s['dist'][n] != float('inf') else '∞':<4}" for n in nodes]
        print(f"{v_set:<20} " + " ".join(dists) + f"  {s['sel']}")

def visualize(G, pos, pred, start):
    plt.figure(figsize=(10, 6))
    nx.draw_networkx_nodes(G, pos, node_color='white', edgecolors='black', node_size=600)
    nx.draw_networkx_labels(G, pos)
    nx.draw_networkx_edges(G, pos, alpha=0.3, style='dashed')
    
    path_edges = [(p, n) for n, p in pred.items() if p is not None]
    nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=2)
    
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    
    plt.title(f"Shortest Path Graph from Source {start}")
    plt.axis('off')
    plt.show()

def main():
    G, pos = create_graph()
    source = 1
    dist, pred, steps = dijkstra(G, source)
    
    print(f"Dijkstra's Algorithm (Source: {source})")
    print_table(G.nodes(), steps)
    
    print("\nShortest Distances:")
    for n in sorted(dist):
        print(f"{n}: {dist[n]}")
        
    visualize(G, pos, pred, source)

if __name__ == "__main__":
    main()
