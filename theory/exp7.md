#### **Experiment No:** 7 | **Date:** 09/04/2026

# Dijkstra's Shortest Path Algorithm

### **Aim**

To implement shortest path algorithm in order to compute the shortest path from the source vertex to all the other vertices in a weighted graph

### **Theory**

In a connected, undirected weighted graph, real-world constraints are modeled via a weight function $w: E \rightarrow \mathbb{R}^+$ assigning non-negative costs to edges. The **Shortest Path Problem** seeks to identify an optimal path $P^*$ between a source $u_0$ and a destination $v$ that minimizes the total aggregate weight $\sum w(e)$, defining the distance $d(u_0, v)$.

**Dijkstra's Algorithm** is an optimal greedy paradigm that constructs a spanning tree of shortest paths radiating from the source. It maintains a partition of the vertex set $V(G)$ into:
*   **Confirmed Set ($S$):** Vertices for which the absolute minimum distance from the source has been established.
*   **Tentative Set ($\bar{S}$):** Vertices with a tentative distance label $l(v)$, serving as a current upper bound on the true shortest distance.

A critical prerequisite for Dijkstra's algorithm is the **strict non-negativity of weights**. Negative weights would violate the greedy assumption that the minimum tentative label represents a finalized shortest distance, as subsequent path extensions could further reduce the total weight.

### **Algorithm: Dijkstra's Algorithm Steps**

1. **Initialization:**
    *   Set the distance label of the source $l(u_0) = 0$.
    *   Set $l(v) = \infty$ for all other vertices $v \neq u_0$.
    *   Initialize the confirmed set $S_0 = \{u_0\}$ and set step $i = 0$.
2. **Label Update:** For each vertex $v$ in the tentative set $\bar{S}_i$, update its label using the relation: $l(v) = \min\{l(v), l(u_i) + w(u_iv)\}$.
3. **Vertex Selection:** Find the vertex $u_{i+1}$ in the tentative set $\bar{S}_i$ for which the label $l(u_{i+1})$ is minimal.
4. **Confirmation:** Move the selected vertex to the confirmed set: $S_{i+1} = S_i \cup \{u_{i+1}\}$.
5. **Iteration:** If $i < \nu - 1$, increment $i$ and return to Step 2. Otherwise, stop. The final labels $l(v)$ represent the shortest distances.

### **Conclusion**

A program implementing shortest path algorithm in order to compute the shortest path from the source vertex to all the other vertices in a weighted graph was successfully implemented
