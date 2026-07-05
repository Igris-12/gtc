import matplotlib.pyplot as plt 
import networkx as nx 

# Added Manual Cycles Path calculation using DFS for academic purposes
# ***not to be used for larger dense graphs***
# Very very heavy in terms of Time and Space

fig, ax = plt.subplots(1, 3, figsize=(15, 5))

def create_graph():
    nodes = list(range(1, 8))
    cycle_edges = [(i, i % 7 + 1) for i in nodes]

    G1 = nx.Graph()
    G1.add_nodes_from(nodes)

    innr_ring1 = [(i, (i+1)% 7 + 1 ) for i in nodes]
    G1.add_edges_from(cycle_edges + innr_ring1)

    G2 = nx.Graph()
    G2.add_nodes_from(nodes)

    innr_ring2 = [(1,3), (1,6), (2,4), (2,6), (3,5), (4,7), (5,7)]
    G2.add_edges_from(cycle_edges + innr_ring2)

    G3 = nx.Graph()
    G3.add_nodes_from(nodes)

    innr_ring3 = [(1,4), (1,5), (2,6), (2,7), (3,5), (3,7), (4,6)]
    G3.add_edges_from(cycle_edges + innr_ring3)

    return G1, G2, G3

def plot_graph(g, idx, title):
    pos = nx.circular_layout(g);
    nx.draw(
            g,
            pos=pos,
            ax= ax[idx],
            with_labels=True,
            node_color="cyan",
            edge_color="blue"
            )
    ax[idx].set_title(title)

def deg_seq(G):
    ds = sorted([d for _, d in nx.degree(G)], reverse=True)
    return ds

def get_adj_list(G):
    vertices = list(G.nodes())
    edges = list(G.edges())

    adj = {v: [] for v in vertices}

    for e0,e1 in edges:
        adj[e0].append(e1)
        adj[e1].append(e0)

    return adj

def cycles(G):
    vertices = list(G.nodes())
    edges = list(G.edges())

    adj_list = get_adj_list(G)

    cycles_path = set()

    def dfs(cur, parent, path):
        if cur == root and len(path)>=3:
            norm_cyl = tuple(sorted(path))
            cycles_path.add(norm_cyl)
            return  

        for v in adj_list[cur]:
            if v == parent:
                continue

            if v < root:
                continue

            if vis[v] == True and v!=root:
                continue
            
            if v != root:
                vis[v] = True

            dfs(v, cur, path + [v])

            if v != root:
                vis[v] = False

    for root in vertices:
        vis = {v: False for v in vertices};
        vis[root] = True
        dfs(root, -1, [root])

    return cycles_path

def cyl_degree(G, cycles):
    cyl_deg = []
    for cyl in cycles:
        node = sorted([G.degree(n) for n in cyl])
        cyl_deg.append(node)

    return sorted(cyl_deg)

def bi_map(g1, g2):
    def solve(mapping, unmapped1, unmapped2):
        if not unmapped1:
            return mapping

        u = unmapped1[0]
        
        for v in unmapped2:
            if g1.degree(u) == g2.degree(v):
                is_consistent = True
                for u_mapped, v_mapped in mapping.items():
                    if g1.has_edge(u, u_mapped) != g2.has_edge(v, v_mapped):
                        is_consistent = False
                        break
                
                if is_consistent:
                    new_mapping = mapping.copy()
                    new_mapping[u] = v
                    solution = solve(new_mapping, unmapped1[1:], [n for n in unmapped2 if n != v])
                    if solution:
                        return solution
        return None

    nodes1 = sorted(list(g1.nodes()), key=g1.degree, reverse=True)
    nodes2 = list(g2.nodes())

    return solve(mapping={}, unmapped1=nodes1, unmapped2=nodes2)


def is_iso(g1, g2):
    v1 = nx.number_of_nodes(g1)
    v2 = nx.number_of_nodes(g2)
    if(v1 != v2):
        print("Not isomorphic (Vertex mismatch)")
        return 

    e1 = nx.number_of_edges(g1)
    e2 = nx.number_of_edges(g2)
    if(e1 != e2):
        print("Not isomorphic (Edges mismatch)")
        return

    d1 = deg_seq(g1)
    d2 = deg_seq(g2)
    if(d1 != d2):
        print("Not isomorphic (Degree Sequence mismatch)")
        return 
    
    cyl1 = cycles(g1)
    cyl2 = cycles(g2)

    if(len(cyl1) != len(cyl2)):
        print("Not isomorphic (Cycle Count mismatch)")
        return 

    cyl_deg1 = cyl_degree(g1, cyl1)
    cyl_deg2 = cyl_degree(g2, cyl2)
    if(cyl_deg1 != cyl_deg2):
        print("Not isomorphic (Cycle degree mismatch)")
        return

    mapping = bi_map(g1, g2)
    if not mapping:
        print("Graphs are not isomorphic (bijection not found).")
        return

    print("Graphs are Isomorphic")
    print(f"|v1| = {v1}     |v2| = {v2}")
    print(f"|e1| = {e1}     |e2| = {e2}")
    print(f"deg1 = {d1}     d2 = {d2}")
    print(f"Mapping: {mapping}")

def main():
    g1, g2, g3 = create_graph()

    print("\n--- For G1 n G2 ---")
    is_iso(g1, g2)
    print("\n--- For G2 n G3 ---")
    is_iso(g2, g3)
    print("\n--- For G1 n G3 ---")
    is_iso(g1, g3)

    plot_graph(g1, 0, "G1")
    plot_graph(g2, 1, "G2")
    plot_graph(g3, 2, "G3")

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
