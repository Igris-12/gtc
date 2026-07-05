#### **Experiment No:** 2 | **Date:** 05/02/2026

# Graph Isomorphism Verification

### **Aim**

To implement graph isomorphism verification inorder to compare structural equivalence of the 2 graphs.

### **Theory**

Two finite, undirected simple graphs $G$ and $H$ are isomorphic, denoted $G \cong H$, if there exists a bijective mapping $\theta: V(G) \rightarrow V(H)$ that preserves the adjacency relation. This means an edge $uv \in E(G)$ exists if and only if the corresponding edge $\theta(u)\theta(v) \in E(H)$. Isomorphic graphs possess identical structural topologies and are indistinguishable from a graph-theoretic perspective, differing only in vertex labeling.

Verification of isomorphism relies on evaluating structural invariants—properties preserved under any isomorphic mapping. Essential necessary conditions include:
*   **Fundamental Metrics:** Identical order (number of vertices) and size (number of edges).
*   **Degree Sequence:** The monotonically non-increasing ordered list of vertex degrees must be identical.
*   **Cyclic Properties:** The girth (length of the shortest cycle) and the presence of cycles of specific lengths must be preserved.
*   **Advanced Invariants:** Clique number, chromatic number, and vertex/edge connectivity.

While these invariants are necessary, they are often insufficient for confirmation. Exact verification typically requires a state-space search to find the bijective mapping.

### **Algorithm: State-Space Search Algorithm for Isomorphism**

1. **Initial Filter:** Compare fundamental invariants (order and size). If they differ, the graphs are non-isomorphic.
2. **Degree Filter:** Compare the degree sequences. If they are not identical, the graphs are non-isomorphic.
3. **Recursive Mapping (Backtracking):**
    *   Iteratively attempt to map a candidate vertex $u \in V(G)$ to a vertex $v \in V(H)$ such that $d_G(u) = d_H(v)$.
    *   Continuously verify that the local adjacency of the partial mapping remains intact: if $u$ is adjacent to a previously mapped vertex $w$ in $G$, then $v$ must be adjacent to $\theta(w)$ in $H$.
    *   If a structural conflict occurs, discard the current partial mapping and backtrack to an earlier state.
4. **Termination:** The algorithm succeeds if a complete bijection is established for all vertices, otherwise it confirms non-isomorphism once all branches are exhausted.

### **Conclusion**

A program checking graph isomorphism verification inorder to compare structural equivalence of the 2 graphs was successfully implemented
