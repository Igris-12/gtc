#### **Experiment No:** 9 | **Date:** 30/04/26

# Eulerian Circuits and Fleury's Algorithm

### **Aim**

Implement an algorithm that checks for the existence of an Eulerian circuit that construct every edge exactly once

### **Theory**

An **Euler trail** is a trail that traverses every edge of a graph $G$ exactly once. If the trail is closed (starts and ends at the same vertex), it is an **Euler tour** (or circuit). Graphs permitting an Euler tour are termed **Eulerian graphs**, a concept famously established by Leonhard Euler’s resolution of the Königsberg bridge problem.

The existence of an Euler tour is governed by a strict parity invariant: a connected graph $G$ is Eulerian if and only if **every vertex has an even degree**. This is necessary because every time the traversal enters a vertex via one edge, it must exit via a distinct edge, exhausting edges in pairs. A single odd-degree vertex makes an Euler tour impossible as the traversal would eventually become trapped at that node.

### **Algorithm: Fleury's Algorithm Steps**

1. **Initialization:** Choose an arbitrary starting vertex $v_0$ from the connected graph $G$.
2. **Iterative Selection:** Suppose the trail $W_i$ has been constructed up to vertex $v_i$. Choose an edge $e_{i+1}$ from the set of untraversed edges that is incident with $v_i$ according to the following heuristic:
    *   Unless there is absolutely no other choice, do **not** select an edge that is a **cut edge** of the remaining untraversed graph.
    *   A cut edge is one whose removal increases the number of connected components; traversing it prematurely would isolate untraversed edges.
3. **Traversal:** Move across the selected edge $e_{i+1}$ to the next vertex $v_{i+1}$ and remove $e_{i+1}$ from the set of available edges.
4. **Termination:** Repeat until all edges in the original graph have been traversed. The resulting sequence forms the Eulerian circuit.

### **Conclusion**

A python program to implement an algorithm that checks for the existence of an Eulerian circuit that construct every edge exactly once was successfully implemented
