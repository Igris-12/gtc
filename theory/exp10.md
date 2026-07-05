#### **Experiment No:** 10 | **Date:** 07/05/26

# Hamiltonian Cycles and Dirac's Theorem

### **Aim**

To implement a method that determines if a Graph contains a Hamiltonian Circuit i.e. a cycle that visits every vertex only once

### **Theory**

A **Hamilton path** is a spanning path in a graph $G$ that visits every vertex exactly once. When a Hamilton path is topologically closed—meaning an edge exists between its terminal and initial vertices—it forms a **Hamilton cycle**. A graph possessing such a cycle is termed **Hamiltonian**.

Unlike Eulerianity, determining Hamiltonianity is notoriously complex and classified as **NP-complete**. No simple universal set of necessary and sufficient conditions exists. Instead, theorists rely on sufficient conditions such as **Dirac's Theorem**, which states that a simple graph of order $\nu \ge 3$ is Hamiltonian if every vertex has a degree $d(v) \ge \nu/2$. 

Due to the computational intractability of exhaustive enumeration ($O(\nu!)$), applied environments often reduce the problem to the **Travelling Salesman Problem (TSP)** using a weighted proxy graph where non-native edges are heavily penalized.

### **Algorithm: TSP-Reduction Algorithm for Hamiltonian Cycles**

1. **Proxy Construction:** Construct a complete graph $K_\nu$ using the vertex set of the original graph $G$.
2. **Weight Mapping:** Define a weight function $w$ for every edge $e$ in $K_\nu$:
    *   If $e$ exists in the original graph $G$, assign it a unitary weight ($w(e) = 1$).
    *   If $e$ does not exist in $G$, assign it a massive penalty weight $M$ (where $M \gg \nu$).
3. **Optimization:** Deploy a TSP algorithm to find a spanning cycle $C^*$ that minimizes the total aggregate weight.
4. **Verification:** 
    *   If the optimal weight $w(C^*) = \nu$, then $G$ contains a valid Hamilton cycle.
    *   If $w(C^*) > \nu$, the algorithm was forced to use a penalized edge, proving a native Hamilton cycle is impossible.

### **Conclusion**

A python program to determine if a Graph contains a Hamiltonian Circuit i.e. a cycle that visits every vertex only once was successfully implemented
