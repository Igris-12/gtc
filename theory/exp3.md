#### **Experiment No:** 3 | **Date:** 05/02/2026

# Subgraph Generation and Classification

### **Aim**

To implement generation of various subgraphs such induced subgraphs, spanning subgraphs and edge deleted subgraphs

### **Theory**

A graph $H$ is defined as a subgraph of $G$ ($H \subseteq G$) if $V(H) \subseteq V(G)$ and $E(H) \subseteq E(G)$, with the requirement that every edge in $E(H)$ exclusively links vertices within $V(H)$. Subgraphs allow for the analysis of localized properties within complex networks.

*   **Induced Subgraphs:** For a subset $S \subseteq V(G)$, the induced subgraph $G[S]$ has vertex set $S$ and includes all edges from $G$ that have both endpoints in $S$. This preserves the localized adjacency of the original graph.
*   **Spanning Subgraphs:** A subgraph that contains all vertices of the original graph ($V(H) = V(G)$). A primary example is the **Spanning Tree**, which is a connected, acyclic spanning subgraph that ensures universal reachability with minimum edges.
*   **Edge-Deleted Subgraphs:** For an edge $e \in E(G)$, the subgraph $G-e$ is formed by removing $e$ while keeping the vertex set invariant. If removing $e$ increases the number of connected components, $e$ is classified as a **cut edge**.

### **Algorithm: Algorithms for Subgraph Generation**

1. **Induced Subgraph ($G[S]$):**
    *   Specify a subset of vertices $S$ to be preserved.
    *   Iterate through the adjacency structure of $G$.
    *   Retain only those edges where both endpoints belong to $S$.
2. **Spanning Subgraph (BFS/DFS Approach):**
    *   Initialize a new graph with the full vertex set $V(G)$.
    *   Perform a graph traversal (Breadth-First Search or Depth-First Search) starting from an arbitrary root.
    *   Add edges to the new graph as they are discovered, provided they do not form a cycle (in the case of a spanning tree).
3. **Edge-Deleted Subgraph ($G-e$):**
    *   Initialize a copy of the original graph $G$.
    *   Identify the specific edge or set of edges $E_{deleted}$ to be removed.
    *   Excise these edges from the adjacency list while maintaining the original vertex set.

### **Conclusion**

A program generating various subgraphs such induced subgraphs, spanning subgraphs and edge deleted subgraphs was successfully implemented
