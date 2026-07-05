#### **Experiment No:** 8 | **Date:** 30/04/2026

# Graph Traversals: Walks, Trails, and Paths

### **Aim**

Implement generation of close walks, trail and path in a connected graph

### **Theory**

Graph traversals characterize the dynamic connectivity of a network through sequential movements. The most general form is a **walk**, an alternating sequence of vertices and edges where both can repeat. A walk is **closed** if it starts and ends at the same vertex, forming the basis for analyzing stochastic processes like random walks.

By imposing constraints on repetition, specialized traversals are derived:
*   **Trail:** A walk with no repeated edges. An **Eulerian trail** traverses every edge exactly once. A closed trail is called a **circuit**.
*   **Path:** A walk with no repeated vertices (and consequently no repeated edges). Paths are used to determine **geodesic distances** (the shortest distance between two vertices).
*   **Cycle:** A closed path of length $k \ge 3$ where all internal vertices are distinct. Cycles are fundamental to the concept of **cycle spaces**, where any closed trail can be reconstructed from a basis of independent cycles.

### **Algorithm: Algorithms for Traversal Generation**

1. **Walk Construction:**
    *   Select a starting vertex $v_0$.
    *   Iteratively select any incident edge to move to an adjacent vertex.
    *   Continue for $k$ steps, allowing both vertex and edge repetition.
2. **Trail Construction:**
    *   Initialize an empty set of "visited edges."
    *   From the current vertex, select an incident edge not present in the visited set.
    *   Add the edge to the visited set and move to the next vertex. Repeat until no untraversed edges are available.
3. **Path Construction:**
    *   Initialize an empty set of "visited vertices."
    *   From the current vertex, move to an adjacent vertex only if it has not been visited before.
    *   Add the new vertex to the visited set.
4. **Cycle Detection (DFS-based):**
    *   Perform a Depth-First Search (DFS) starting from an arbitrary root.
    *   Keep track of the "ancestor" path in the recursion stack.
    *   If an edge points to a vertex already in the current recursion stack (a back-edge), a cycle is verified.

### **Conclusion**

A python program for generation of close walks, trail and path in a connected graph was successfully implemented
