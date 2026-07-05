import matplotlib.pyplot as plt
import networkx as nx

fig, ax = plt.subplots(2,2)

def set_border(axis, color , width):
    axis.set_axis_on()
    axis.tick_params(left=False, bottom=False, labelleft=False, labelbottom=False)
    for spine in axis.spines.values():
        spine.set_edgecolor(color)
        spine.set_linewidth(width)
        spine.set_visible(True)

# P5
p5 = nx.Graph()
p5.add_nodes_from(range(1,6))
for i in range(1,5):
    p5.add_edge(i,i+1)

pos_p5 = nx.spring_layout(p5)

nx.draw(
        p5,
        ax = ax[0,0],
        pos = pos_p5,
        with_labels=True,
        node_color="orange",
        edge_color="red"
        )
ax[0,0].set_title("Path Graph (P5)")
set_border(ax[0,0], "red", 1.2)

# K23
k23 = nx.Graph()
k23.add_nodes_from(range(1,6))
for i in [1,2]:
    for j in [3,4,5]:
        k23.add_edge(i,j)

pos_k23 = {1:[1,2], 2:[3,2], 3:[0,0], 4:[2,0], 5:[4,0]}
nx.draw(
        k23,
        ax = ax[0,1],
        pos = pos_k23,
        with_labels=True,
        node_color="cyan",
        edge_color="blue"
        )
ax[0,1].set_title("Complete Bipartite Graph (K23)")
set_border(ax[0,1], "blue", 1.2)

# C5
c5 = nx.Graph()
c5.add_nodes_from(range(1,6))
for i in range(1,5):
    c5.add_edge(i, i+1)
c5.add_edge(5,1)

pos_c5 = nx.circular_layout(c5);
nx.draw(
        c5,
        ax = ax[1,0],
        pos = pos_c5,
        with_labels=True,
        node_color="lime",
        edge_color="green"
        )
ax[1,0].set_title("Cyclic Graph (C5)")
set_border(ax[1,0], "green", 1.2)

# K5
k5 = nx.Graph()
k5.add_nodes_from(range(1,6))
for i in range (1,6):
    for j in [n for n in range(1,6) if n!=i]:
        k5.add_edge(i,j)

pos_k5 = nx.circular_layout(k5)
nx.draw(
        k5,
        ax = ax[1,1],
        pos = pos_k5,
        with_labels=True,
        node_color="violet",
        edge_color="purple"
        )
ax[1,1].set_title("Complete Graph (K5)")
set_border(ax[1,1], "purple", 1.2)

plt.tight_layout()
plt.show()
