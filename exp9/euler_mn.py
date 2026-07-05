import matplotlib.pyplot as plt 
import networkx as nx 

def create_graph():
    G1 = nx.Graph()
    G2 = nx.Graph()

    G1.add_nodes_from(range(0,6))
    G2.add_nodes_from(range(0,6))

    e1_edges = [ (i, (i+1)%6) for i in range(6)]
    e1_edges.extend([(0,2), (0,3), (1,4), (5,2)])
    G1.add_edges_from(e1_edges)
    labels1 = {edge: f"e{i+1}" for i, edge in enumerate(G1.edges())}

    e2_edges = [(i, (i+1)%6) for i in range(5)]
    e2_edges.extend([(i,5) for i in range(1,4)])
    e2_edges.extend([(4,1), (4,0), (2,0), (3,0)])
    G2.add_edges_from(e2_edges)
    labels2 = {edge: f"e{i+1}" for i, edge in enumerate(G2.edges())}

    pos1 = { 0: (-1,1), 1: (1,1), 2:(2,0), 3:(1, -1), 4:(-1, -1), 5:(-2,0) }
    pos2 = { 0: (0,2), 1: (1,1), 2:(1,-1), 3:(-1, -1), 4:(-1, 1), 5:(0,0) }

    return G1, pos1, G2, pos2, labels1, labels2

def get_adj(G):
    nodes = list(G.nodes())
    edges = list(G.edges())

    adj = {i: [] for i in nodes}

    for e1,e2 in edges:
        adj[e1].append(e2)
        adj[e2].append(e1)

    return adj

def is_cut(G, e):
    u, v = e

    G_e = G.copy()
    G_e.remove_edge(u, v)
    
    visited = set()
    path_exist = False
    adj = get_adj(G_e)

    def dfs(root):
        nonlocal path_exist

        if path_exist: 
            return

        visited.add(root)

        if root == v:
            path_exist = True
            return

        for node in adj.get(root, []):
            if node not in visited:
                dfs(node)

    dfs(u)

    return not path_exist


def is_euler(G):
    if not nx.is_connected(G):
        return False
    
    for node in G.nodes():
        if G.degree(node) % 2 != 0:
            return False

    return True

def find_euler(G, pos=None, name="Graph", edge_labels=None):
    if not is_euler(G):
        print(f"{name}: Eulerian circuit does not exist")
        return None

    curr = list(G.nodes())[0]
    trail = [curr]
    traversed_labels = []
    G_temp = G.copy()
    step = 1

    while G_temp.number_of_edges() > 0:
        edges = list(G_temp.edges(curr))
        if len(edges) == 1:
            u, v = edges[0]
        else:
            for u, v in edges:
                if not is_cut(G_temp, (u, v)):
                    break
            else:
                u, v = edges[0]
        
        e_label = ""
        if edge_labels:
            e_label = edge_labels.get((u, v), edge_labels.get((v, u), ""))
        
        traversed_labels.append(e_label)

        display_items = []
        for i in range(len(trail)):
            display_items.append(str(trail[i]))
            display_items.append(traversed_labels[i])
        display_items.append(str(v))
        display_trail_str = ", ".join(display_items)

        if pos is not None:
            plt.figure(figsize=(10, 7))
            nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='whitesmoke', style='dashed')
            
            if len(trail) > 1:
                past_edges = [(trail[i], trail[i+1]) for i in range(len(trail)-1)]
                nx.draw_networkx_edges(G, pos, edgelist=past_edges, edge_color='blue', width=2, alpha=0.4)

            nx.draw_networkx_edges(G_temp, pos, edge_color='black', width=1)
            nx.draw_networkx_edges(G_temp, pos, edgelist=[(u, v)], edge_color='red', width=4)
            
            if edge_labels:
                nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
            
            plt.title(f"Step {step}: Removing edge {e_label} ({u}, {v})")
            plt.figtext(0.5, 0.02, f"Trail: {display_trail_str}", ha="center", fontsize=9, bbox={"facecolor":"orange", "alpha":0.2, "pad":5})
            
            print(f"Step {step}: Removing edge {e_label} ({u}, {v})")
            print(f"Trail so far: {display_trail_str}")
            plt.subplots_adjust(bottom=0.15)
            plt.show()
        
        G_temp.remove_edge(u, v)
        curr = v
        trail.append(curr)
        step += 1
    
    if pos is not None:
        plt.figure(figsize=(10, 7))
        nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray')
        edges_trail = [(trail[i], trail[i+1]) for i in range(len(trail)-1)]
        nx.draw_networkx_edges(G, pos, edgelist=edges_trail, edge_color='blue', width=2)
        if edge_labels:
            nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
        
        final_items = []
        for i in range(len(trail)-1):
            final_items.append(str(trail[i]))
            final_items.append(traversed_labels[i])
        final_items.append(str(trail[-1]))
        final_trail_str = ", ".join(final_items)
        
        plt.title(f"{name} - Final Eulerian Circuit")
        plt.figtext(0.5, 0.02, f"Final Trail: {final_trail_str}", ha="center", fontsize=9, bbox={"facecolor":"green", "alpha":0.2, "pad":5})
        plt.subplots_adjust(bottom=0.15)
        plt.show()

    return trail


def main():
    G1, pos1, G2, pos2, labels1, labels2 = create_graph()
    
    print("Graph 1:")
    circuit1 = find_euler(G1, pos1, "Graph 1", labels1)
    if circuit1:
        print("Final Eulerian Circuit (G1):", circuit1)
    
    print("\nGraph 2:")
    circuit2 = find_euler(G2, pos2, "Graph 2", labels2)
    if circuit2:
        print("Final Eulerian Circuit (G2):", circuit2)

if __name__ == "__main__":
    main()
