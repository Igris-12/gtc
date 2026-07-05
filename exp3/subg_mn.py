import matplotlib.pyplot as plt 
import networkx as nx
from collections import deque

def create_graph(G):
    G.add_nodes_from(range(12)) 
    G.add_edges_from([(0,1), (1,2), (2,3), (3,0),
                  (0,5), (1,6), (2,7), (3,4),
                  (5,11), (6,11), (8,10), (9,10), (10,11),
                  (5,7), (7,8), (8,9), (9,4), (4,6)])

    pos = {
        0: (-2, 2),    
        1: (2, 2),     
        2: (2, -2),    
        3: (-2, -2),   
        
        4: (-1.5, -0.5), 
        5: (-1, 1),      
        6: (1, 1),       
        7: (1.5, -0.5),  
        
        8: (0.5, -1.5),  
        9: (-0.5, -1.5),
        
        10: (0, -1),     
        11: (0, 0)       
    }

    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(18, 6))
    plt.figure(figsize=(6, 6))
    nx.draw(G, 
            pos, 
            with_labels=True, 
            node_color='black',
            font_color='white',
            edge_color='red')
    
    plt.title("Graph Layout")

    induced_nodes = [0, 1, 5, 6, 11]
    create_induced_subgraph(G, induced_nodes, ax1, pos)

    create_spanning_subgraph(G, ax2, pos)

    edges_to_delete = [(0,1), (1,2), (2,3), (3,0)]
    create_edge_deleted_subgraph(G, edges_to_delete, ax3, pos)

def get_adj(G):
    ver = list(G.nodes())
    edges = list(G.edges())

    adj = [[] for _ in ver]

    for e1, e2 in edges:
        adj[e1].append(e2)
        adj[e2].append(e1)

    return adj

def create_induced_subgraph(G, nodes_to_keep, ax, pos):
    subgraph = nx.Graph()
    subgraph.add_nodes_from(nodes_to_keep)

    adj = get_adj(G)
    for node in nodes_to_keep:
        subgraph.add_edges_from((node, nb) for nb in adj[node] if nb in nodes_to_keep)

    nx.draw(subgraph,
            pos,
            ax=ax,
            with_labels=True,
            node_color='red', 
            font_color='white',
            edge_color='black')

    ax.set_title("Induced Subgraph")

def create_spanning_subgraph(G, ax, pos):
    subgraph = nx.Graph()
    ver = list(G.nodes())
    subgraph.add_nodes_from(ver)

    adj = get_adj(G)
    visited = [0] * len(ver)

    for root in ver: 
        if (visited[root] != 0):
            continue

        visited[root] = 1
        q = deque([root])

        while q:
            cur = q.popleft()
            
            for node in adj[cur]:
                if visited[node] == 1:
                    continue

                subgraph.add_edge(cur, node)
                q.append(node)
                visited[node] = 1

    nx.draw(subgraph, 
            pos, 
            ax=ax, 
            with_labels=True, 
            node_color='blue', 
            edge_color='black')

    ax.set_title("Spanning Subgraph")

def create_edge_deleted_subgraph(G, edges_to_remove, ax, pos):
    subgraph = G.copy()
    subgraph.remove_edges_from(edges_to_remove)
    nx.draw(subgraph,
            pos,
            ax=ax,
            with_labels=True,
            node_color='green', 
            edge_color='black')

    ax.set_title(f"Edge Deleted Subgraph")

def main():
    G = nx.Graph()
    create_graph(G);

    plt.show()


if __name__ == "__main__":
    main()
