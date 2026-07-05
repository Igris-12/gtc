#### **Experiment No:** 1 | **Date:** 29/01/2026

# Fundamental Graph Structures

### **Aim**

To implement the basic graphs such as Path graph, Cycle graph, Complete graph and Complete Bi-pertite graph

### **Theory**

The structural properties of discrete relational systems are formally characterized within the framework of graph theory. A graph $G$ is defined as an ordered triple $(V(G), E(G), \psi_G)$, where $V(G)$ is a nonempty set of vertices, $E(G)$ is a set of edges, and $\psi_G$ is an incidence function that associates each edge with an unordered pair of vertices. The degree of a vertex, denoted $d_G(v)$, is the number of edges incident with $v$. Fundamental graph families are classified by their adjacency patterns:

*   **Path Graph ($P_n$):** A connected graph of order $n$ whose vertices can be arranged in a linear sequence $(v_1, v_2, \dots, v_n)$ such that the edge set is $E(P_n) = \{v_i v_{i+1} : 1 \le i < n\}$.
*   **Cycle Graph ($C_n$):** For $n \ge 3$, a cycle graph is obtained by adding the edge $v_n v_1$ to a path graph $P_n$, resulting in a 2-regular connected graph.
*   **Complete Graph ($K_n$):** A graph where every distinct pair of vertices is joined by a unique edge, satisfying $d(v) = n-1$ for all vertices.
*   **Complete Bipartite Graph ($K_{m,n}$):** A graph whose vertex set can be partitioned into two disjoint independent sets $X$ and $Y$ of sizes $m$ and $n$, where every vertex in $X$ is adjacent to every vertex in $Y$.

### **Algorithm: Algorithms for Graph Generation**

1. **Path Graph ($P_n$):**
    *   Initialize the vertex set $V = \{1, \dots, n\}$.
    *   Perform a single-pass iteration to define the edge set $E = \{(i, i+1) : 1 \le i < n\}$.
2. **Cycle Graph ($C_n$):**
    *   Follow the path graph construction steps.
    *   Establish a terminal edge $(n, 1)$ to close the sequence.
3. **Complete Graph ($K_n$):**
    *   Initialize the vertex set $V = \{1, \dots, n\}$.
    *   Use nested iterations to assign an edge $(u, v)$ for every $u, v \in V$ where $u \neq v$, resulting in $|E| = \binom{n}{2}$ edges.
4. **Complete Bipartite Graph ($K_{m,n}$):**
    *   Partition the vertex set into $X = \{x_1, \dots, x_m\}$ and $Y = \{y_1, \dots, y_n\}$.
    *   Perform a Cartesian-product-style iteration to establish edges for every pair $(u, v)$ such that $u \in X$ and $v \in Y$.

### **Conclusion**

Successfully implemented basic graphs such as Path graph (P5), Cycle graph (C5), Complete graph(K5) and Complete Bipartite graph(K23)
