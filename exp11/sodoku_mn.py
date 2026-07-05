import matplotlib.pyplot as plt
import networkx as nx

def create_sudoku_graph():
    G = nx.Graph()
    size = 4
    box_size = 2
    nodes = [(r, c) for r in range(size) for c in range(size)]
    G.add_nodes_from(nodes)
    
    row_edges = []
    col_edges = []
    box_edges = []
    
    for r1, c1 in nodes:
        for r2, c2 in nodes:
            if (r1, c1) >= (r2, c2):
                continue
            if r1 == r2:
                G.add_edge((r1, c1), (r2, c2))
                row_edges.append(((r1, c1), (r2, c2)))
            elif c1 == c2:
                G.add_edge((r1, c1), (r2, c2))
                col_edges.append(((r1, c1), (r2, c2)))
            elif (r1 // box_size == r2 // box_size) and (c1 // box_size == c2 // box_size):
                G.add_edge((r1, c1), (r2, c2))
                box_edges.append(((r1, c1), (r2, c2)))
                
    pos = {(r, c): (c, -r) for r, c in nodes}
    return G, pos, row_edges, col_edges, box_edges

def is_safe(G, node, color, color_schm):
    for neighbor in G.neighbors(node):
        if color_schm[neighbor] == color:
            return False
    return True

def solve(G, nodes, index, color_schm):
    if index == len(nodes):
        return True
    node = nodes[index]
    if color_schm[node] != 0:
        return solve(G, nodes, index + 1, color_schm)
        
    for color in range(1, 5):
        if is_safe(G, node, color, color_schm):
            color_schm[node] = color
            if solve(G, nodes, index + 1, color_schm):
                return True
            color_schm[node] = 0
    return False

def main():
    G, pos, row_e, col_e, box_e = create_sudoku_graph()
    puzzle = {
        (0, 0): 0, (0, 1): 0, (0, 2): 0, (0, 3): 2,
        (1, 0): 0, (1, 1): 4, (1, 2): 0, (1, 3): 0,
        (2, 0): 1, (2, 1): 0, (2, 2): 0, (2, 3): 0,
        (3, 0): 0, (3, 1): 0, (3, 2): 0, (3, 3): 0
    }
    
    initial_nodes = [node for node, val in puzzle.items() if val != 0]
    solved_nodes = [node for node, val in puzzle.items() if val == 0]
    color_schm = puzzle.copy()
    nodes_list = list(G.nodes())
    
    solve(G, nodes_list, 0, color_schm)
    
    color_map = {1: '#ff9999', 2: '#9999ff', 3: '#99ff99', 4: '#ffff99'}
    plt.figure(figsize=(14, 12))
    plt.title("4x4 Sudoku Graph", fontsize=16)
    
    def draw_curved_edges(edges, color, is_row):
        for u, v in edges:
            dist = abs(u[1] - v[1]) if is_row else abs(u[0] - v[0])
            rad = 0.0 if dist == 1 else (0.2 if dist == 2 else 0.4)
            nx.draw_networkx_edges(G, pos, edgelist=[(u, v)],
                                   edge_color=color, alpha=0.4, width=2,
                                   arrows=True, arrowstyle='-',
                                   connectionstyle=f"arc3,rad={rad}")
                                   
    draw_curved_edges(row_e, 'blue', True)
    draw_curved_edges(col_e, 'red', False)
    
    nx.draw_networkx_edges(G, pos, edgelist=box_e, edge_color='green',
                           alpha=0.6, width=2, label='Box Arcs')
    nx.draw_networkx_nodes(G, pos, nodelist=solved_nodes,
                           node_color=[color_map[color_schm[n]] for n in solved_nodes],
                           node_size=1200, edgecolors='gray', linewidths=1)
    nx.draw_networkx_nodes(G, pos, nodelist=initial_nodes,
                           node_color=[color_map[color_schm[n]] for n in initial_nodes],
                           node_size=1500, edgecolors='black', linewidths=5)
                           
    labels = {n: color_schm[n] for n in G.nodes()}
    nx.draw_networkx_labels(G, pos, labels=labels, font_size=18, font_weight='bold')
    
    plt.axis('off')
    print("Sudoku Solved! Curves ensure all 7 edges per node are visible.")
    plt.show()

if __name__ == "__main__":
    main()
