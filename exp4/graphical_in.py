import matplotlib.pyplot as plt 
import networkx as nx 

def visualize_havel_hakimi(deg_seq):
    if not nx.is_graphical(deg_seq):
        print("The degree sequence is Non-Graphical")
        return False

    print("The degree sequence is Graphical")
    
    n = len(deg_seq)
    sequence = [[d, i] for i, d in enumerate(deg_seq)]
    G = nx.Graph()
    G.add_nodes_from(range(n))
    
    iteration_count = 1
    
    while True:
        sequence.sort(key=lambda x: x[0], reverse=True)
        
        if not sequence or sequence[0][0] == 0:
            break
            
        d, u = sequence.pop(0)
        
        for i in range(d):
            sequence[i][0] -= 1
            v = sequence[i][1]
            G.add_edge(u, v)
            
        current_deg_map = {item[1]: item[0] for item in sequence}
        print(f"Iteration {iteration_count}: {current_deg_map}")
        
        plt.figure(figsize=(6, 4))
        plt.title(f"After Iteration {iteration_count}: Node {u} connected")
        nx.draw(G, 
                with_labels=True, 
                node_color='lightblue', 
                edge_color='gray', 
                node_size=500, 
                font_weight='bold')
        
        iteration_count += 1

    return True

def main():
    try:
        user_input = input("Enter the Degree Sequence (comma separated): ")
        deg_seq = [int(n.strip()) for n in user_input.split(',')]
        deg_seq.sort(reverse=True)
        
        if visualize_havel_hakimi(deg_seq):
            plt.show()
    except ValueError:
        print("Invalid input. Please enter a sequence of integers.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
