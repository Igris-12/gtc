import matplotlib.pyplot as plt 
import networkx as nx 

def create_graph():
    G = nx.Graph()

    nodes = range(0,8)
    node = len(nodes)
    G.add_nodes_from(nodes)

    edges = [(i, (i+1)%node) for i in nodes]
    edges.extend([(i, (i+2)%node) for i in nodes])
    edges.extend([(i, (i+4)%node) for i in nodes])
    G.add_edges_from(edges)

    pos = {0: (-0.5,1), 1:(0.5,1), 2:(1, 0.5), 3:(1, -0.5), 4:(0.5, -1), 5:(-0.5,-1), 6:(-1, -0.5), 7:(-1, 0.5)}

    return G, pos


def color(G):
    colors = ["red", "blue", "green", "yellow", "orange"]

    def my_str(G , colors):
        return list(range(0,8))

    color_scheme = nx.greedy_color(G,strategy=my_str)
    node_colors = [colors[color_scheme[node]] for node in G.nodes()]

    return node_colors

def main():
    G, pos = create_graph()
    node_colors = color(G)

    fig, ax = plt.subplots(1, 2, figsize=(12, 6))
    fig.suptitle("Graph Coloring", fontsize=16)

    ax[0].set_title("Original Graph")
    nx.draw(G, pos=pos, ax=ax[0], with_labels=True, node_color='lightblue', 
            node_size=800, font_size=12, font_weight='bold', edge_color='gray')

    ax[1].set_title("Colored Graph")
    nx.draw(G, pos=pos, ax=ax[1], node_color=node_colors, with_labels=True, 
            node_size=800, font_size=12, font_weight='bold', edge_color='gray')
    
    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.show()

if __name__ == "__main__":
    main()
