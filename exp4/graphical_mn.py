import matplotlib.pyplot as plt 
import networkx as nx 

def iteration(G, deg_map):
    it = iter(deg_map)
    first = next(it)

    if deg_map[first] >= len(deg_map):
        deg_map[first] = -1
        return deg_map

    for _ in range(deg_map[first]):
        key = next(it)
        deg_map[key] -= 1

        if deg_map[key] < 0:
            return deg_map

        G.add_edge(first, key)

    del deg_map[first]
    return deg_map

def is_graphical(deg_map):
    ver = len(deg_map)
    G = nx.Graph()
    G.add_nodes_from(range(0,ver))

    sum_deg = 0
    for deg in deg_map.values():
        if deg >= ver:
            return False
        sum_deg += deg;

    if (sum_deg % 2 != 0):
        return False

    sort_deg = dict(sorted(deg_map.items(), key=lambda item: item[1], reverse=True))
    iteration_count = 1
    for _ in range(0, ver):
        if not sort_deg or all(v == 0 for v in sort_deg.values()): 
            break
            
        deg_map = iteration(G, sort_deg)

        print(f"Iteration {iteration_count}: {deg_map}")
        for deg in deg_map.values():
            if deg < 0:
                return False

        plt.figure(figsize = (6,4))
        plt.title(f"After Iteration {iteration_count}")
        nx.draw(G, with_labels=True, node_color='lightblue')

        iteration_count += 1
        sort_deg = dict(sorted(deg_map.items(), key=lambda item: item[1], reverse=True))

    return True


def main():
    deg_seq = [int(n) for n in input("Enter the Degree Sequence: ").split(',')]
    deg_seq.sort(reverse=True)

    deg_map = {}
    for i in range(0, len(deg_seq)):
        deg_map[i] = deg_seq[i]

    result = is_graphical(deg_map)

    if result:
        print("The degree sequence is Graphical")
    else:
        print("The degree sequence is Non-Graphical")

    plt.show()
  
if __name__ == "__main__":
    main()
