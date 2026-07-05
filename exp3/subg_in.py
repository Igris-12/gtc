import matplotlib.pyplot as plt 
import networkx as nx

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

    plt.figure(figsize=(6, 6))
    nx.draw(G, 
            pos, 
            with_labels=True, 
            node_color='black',
            font_color='white',
            edge_color='red')
    plt.title("Graph Layout")

    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(18, 6))

    induced_nodes = [0, 1, 5, 6, 11]
    create_induced_subgraph(G, induced_nodes, ax1, pos)

    create_spanning_subgraph(G, ax2, pos)

    edges_to_delete = [(0,1), (1,2), (2,3), (3,0)]
    create_edge_deleted_subgraph(G, edges_to_delete, ax3, pos)

def create_induced_subgraph(G, nodes_to_keep, ax, pos):
    subgraph = G.subgraph(nodes_to_keep)

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
    subgraph.add_nodes_from(G.nodes())
    
    for component in nx.connected_components(G):
        root = list(component)[0]
        tree = nx.bfs_tree(G, root).to_undirected()
        subgraph.add_edges_from(tree.edges())

    nx.draw(subgraph, 
            pos, 
            ax=ax, 
            with_labels=True, 
            node_color='blue', 
            edge_color='black')

    ax.set_title("Spanning Subgraph (BFS Forest)")

def create_edge_deleted_subgraph(G, edges_to_remove, ax, pos):
    subgraph = G.copy()
    subgraph.remove_edges_from(edges_to_remove)
    
    nx.draw(subgraph,
            pos,
            ax=ax,
            with_labels=True,
            node_color='green', 
            edge_color='black')

    ax.set_title("Edge Deleted Subgraph")

def main():
    G = nx.Graph()
    create_graph(G)
    plt.show()

if __name__ == "__main__":
    main()
