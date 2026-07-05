#### **Experiment No:** 5 | **Date:** 12/03/2026

# Line Graph Transformation

### **Aim**

To implement conversion of a given graph into line graph where each vertex represents an edge of the original graph, and adjacency reflects shared endpoints

### **Theory**

The line graph of a simple graph $G$, denoted $L(G)$, is a transformation where edges are treated as vertices. The vertex set $V(L(G))$ has a bijective correspondence with the edge set $E(G)$, meaning the order of the line graph equals the size of the original graph ($|V(L(G))| = |E(G)|$).

Adjacency in $L(G)$ is defined by incidence in $G$: two vertices in $L(G)$ are adjacent if and only if their corresponding edges in $G$ share at least one common endpoint. The degree of a vertex in $L(G)$ representing edge $e=uv$ is calculated by $d_{L(G)}(e) = d_G(u) + d_G(v) - 2$.

**Whitney's Isomorphism Theorem** establishes that for connected graphs of order $\nu > 4$, structural equivalence of line graphs guarantees isomorphism between the primary graphs. A notable anomaly occurs for $K_3$ and $K_{1,3}$, which have isomorphic line graphs ($K_3$) despite being non-isomorphic themselves. Line graphs are useful for solving edge-centric problems (like edge matching or edge coloring) using standard vertex-centric frameworks (like independent sets or vertex coloring).

### **Algorithm: Algorithm for Line Graph Construction**

1. **Edge Identification:** Extract the complete edge set $E(G)$ from the original graph $G$.
2. **Vertex Initialization:** Create a new graph $L(G)$ where each node represents a unique edge from $E(G)$.
3. **Incidence Check:** Iterate through every distinct pair of representative vertices in $L(G)$.
4. **Edge Establishment:**
    *   For each pair of edges $e_i, e_j$ from $G$, check if they share a common vertex.
    *   If they are incident to the same vertex, add an edge between their corresponding vertices in $L(G)$.
5. **Finalization:** The resulting graph $L(G)$ captures the edge-adjacency structure of $G$.

### **Conclusion**

A program converting a given graph into its corresponding line graph was successfully implemented
