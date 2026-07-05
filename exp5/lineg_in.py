import matplotlib.pyplot as plt 
import networkx as nx 

def get_adj():
    nv = int(input("Vertices: "))
    v = range(nv)

    print("\nAdjacency Matrix: ")
    adj = []
    for i in v:
        row = tuple(int(e) for e in input(f"Row{i}: ").split(" "))
        
        if len(row) != nv:
            print("Invalid Entry")
            break

        adj.append(row)

    e = set()
    for i in range(nv):
        for j in range(nv):
            if adj[i][j] == 1:
                e.add((i,j) if i<j else (j,i))

    return v, e
 
def visualize(G, L_G):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    nx.draw(G, ax=ax1, with_labels=True, node_color='lightblue')
    ax1.set_title("Original G")

    nx.draw(L_G, ax=ax2, with_labels=True, node_color='lightcoral')
    ax2.set_title("Line Graph L(G)")
    plt.show()


def main():
    v, e = get_adj()

    G = nx.Graph()
    G.add_nodes_from(v)
    G.add_edges_from(e)

    LG = nx.line_graph(G)

    visualize(G, LG)

if __name__ == "__main__":
    main()
