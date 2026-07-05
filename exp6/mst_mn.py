import matplotlib.pyplot as plt
import networkx as nx

def create_graph():
    G = nx.Graph()
    G.add_weighted_edges_from([
        (1, 2, 14), (1, 3, 5), (1, 4, 2), (2, 3, 9), (2, 4, 8), (2, 5, 15),
        (3, 5, 13), (3, 6, 8), (4, 5, 10), (4, 8, 11), (5, 6, 1), (5, 7, 7),
        (5, 8, 5), (6, 7, 10), (6, 9, 11), (7, 8, 0), (7, 9, 12), (8, 9, 6)
    ])
    return G

def kruskal_steps(G):
    mst = nx.Graph()
    mst.add_nodes_from(G.nodes())
    edges = sorted(G.edges(data=True), key=lambda x: x[2]['weight'])
    cost = 0
    for u, v, data in edges:
        weight = data['weight']
        components = list(nx.connected_components(mst))
        same_component = False
        for comp in components:
            if u in comp and v in comp:
                same_component = True
                break
        if not same_component:
            mst.add_edge(u, v, weight=weight)
            cost += weight
            yield weight, [(u, v)], [], mst.copy(), cost, nx.number_connected_components(mst)
        else:
            pass

def draw_graph(G, pos, title, metrics=None, **kwargs):
    plt.figure(figsize=(10, 7))
    nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=700, **kwargs)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=nx.get_edge_attributes(G, 'weight'))
    plt.title(title)
    if metrics:
        plt.text(0.02, 0.95, metrics, transform=plt.gca().transAxes, fontsize=16,
                 verticalalignment='top', fontweight='bold')

def main():
    G, pos = create_graph(), {1:(-1,0), 2:(-0.5,0), 3:(-0.5,1), 4:(-0.5,-1), 5:(0,0), 6:(0.5,1), 7:(0.5,0),
                              8:(0.5,-1), 9:(1,0)}
    draw_graph(G, pos, "Original Graph", node_color='lightblue')
    for w, acc, rej, mst, cost, comps in kruskal_steps(G):
        acc_s, rej_s = ", ".join(f"{u}-{v}" for u,v in acc), ", ".join(f"{u}-{v}" for u,v in rej)
        title = f"Step: Weight {w}\nAccepted: {acc_s}" + (f"\nRejected: {rej_s}" if rej else "")
        draw_graph(mst, pos, title, f"Cost: {cost}\nComponents: {comps}", node_color='lightgreen',
                   edge_color='red', width=2)
    plt.show()

if __name__ == "__main__":
    main()
