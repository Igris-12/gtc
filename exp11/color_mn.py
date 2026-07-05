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

def get_adj(G):
    e = list(G.edges())
    adj = {node: [] for node in G.nodes()}

    for e1, e2 in e:
        adj[e1].append(e2)
        adj[e2].append(e1)


    return adj

def color(G, colors):
    color_schm = { node: "" for node in G.nodes()} 

    adj = get_adj(G)

    for node in G.nodes():
        neighbors = {color_schm[neig] for neig in adj[node]}
        for color in colors:
            if color not in neighbors:
                color_schm[node] = color
                break

    return color_schm.values()

def main():
    G, pos = create_graph()
    fig, ax = plt.subplots(1, 2, figsize=(12, 6))
    fig.suptitle("Graph Coloring", fontsize=16)

    colors = ["red", "blue", "green", "yellow", "orange"]

    color_schm = color(G, colors)

    ax[0].set_title("Original Graph")
    nx.draw(G, pos=pos, ax=ax[0], with_labels=True, node_color='lightblue', 
            node_size=800, font_size=12, font_weight='bold', edge_color='gray')

    ax[1].set_title("Colored Graph")
    nx.draw(G, pos=pos, ax=ax[1], with_labels=True, node_color=color_schm, 
            node_size=800, font_size=12, font_weight='bold', edge_color='gray')

    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.show()


main()



