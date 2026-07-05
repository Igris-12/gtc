import matplotlib.pyplot as plt
import networkx as nx

def main():
    G = nx.Graph()
    edges = [
        (1, 2, 6), (1, 3, 7), (2, 3, 8), (2, 4, 9), (2, 6, 14),
        (3, 4, 5), (3, 5, 4), (4, 5, 6), (4, 6, 10), (5, 7, 7),
        (6, 7, 11), (6, 8, 8), (7, 8, 6)
    ]
    G.add_weighted_edges_from(edges)
    pos = {1: (0, 0), 2: (1, 1), 3: (1, -1), 4: (2, 0), 
           5: (2, -2), 6: (3, 1), 7: (3, -1), 8: (4, 0)}
    source = 1

    print(f"Dijkstra's Algorithm using NetworkX (Source: {source})")
    print("-" * 40)

    lengths, paths = nx.single_source_dijkstra(G, source=source)

    print(f"{'Node':<10} {'Distance':<10} {'Shortest Path'}")
    for node in sorted(lengths):
        print(f"{node:<10} {lengths[node]:<10} {paths[node]}")

    plt.figure(figsize=(10, 6))
    nx.draw_networkx_nodes(G, pos, node_color='white', edgecolors='black', node_size=600)
    nx.draw_networkx_labels(G, pos)
    nx.draw_networkx_edges(G, pos, alpha=0.3, style='dashed')
    
    path_edges = []
    for node in paths:
        path = paths[node]
        for i in range(len(path) - 1):
            path_edges.append((path[i], path[i+1]))
            
    nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='blue', width=2)
    
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    
    plt.title(f"Shortest Path Tree (Inbuilt) from Source {source}")
    plt.axis('off')
    plt.show()

if __name__ == "__main__":
    main()
