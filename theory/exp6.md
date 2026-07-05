#### **Experiment No:** 6 | **Date:** 09/04/26

# Minimum Spanning Trees (Kruskal's Algorithm)

### **Aim**

To implement finding the minimum spanning tree for a given graph using Kruskal's algorithm, ensuring all vertices are connected with the minimum possible total edge weight and without forming cycles

### **Theory**

Let $G = (V, E)$ be a connected, undirected simple graph. In applied networks, costs such as distance or transport expense are modeled using a weighted graph with a weight function $w: E \rightarrow \mathbb{R}$. A **Spanning Tree (T)** is a connected, acyclic spanning subgraph where $|E(T)| = \nu - 1$. An optimal tree, or **Minimum Spanning Tree ($T^*$)**, is a spanning tree that minimizes the total aggregate edge weight $\sum_{e \in E(T^*)} w(e)$.

The construction of an MST relies on two foundational invariants:
*   **Cut Property:** For any vertex partition $S$, the minimum weight edge incident to exactly one vertex in $S$ must be part of at least one MST.
*   **Cycle Property:** For any cycle in $G$, the edge with the strictly maximum weight cannot be part of any MST.

These properties validate the greedy heuristic, ensuring locally optimal selections lead to a globally optimal configuration.

### **Algorithm: Kruskal's Algorithm Steps**

1. **Initial Selection:** Sort all edges in the graph by weight in non-decreasing order. Choose the edge $e_1$ with the smallest possible weight.
2. **Iterative Selection:** Suppose edges $\{e_1, e_2, \dots, e_i\}$ have been chosen. Select the next edge $e_{i+1}$ from the remaining set $E \setminus \{e_1, \dots, e_i\}$ such that:
    *   The resulting subgraph $\{e_1, \dots, e_{i+1}\}$ remains acyclic (no cycles are formed).
    *   The weight $w(e_{i+1})$ is the minimum possible among all edges satisfying the acyclic condition.
3. **Termination:** Stop the procedure once it is impossible to add more edges without forming a cycle. For a connected graph, this occurs when $\nu - 1$ edges have been selected, forming the MST.

### **Conclusion**

A program finding the minimum spanning tree for a given graph using Kruskal's algorithm was successfully implemented
