#### **Experiment No:** 11 | **Date:** 14/05/26

# Greedy Graph Coloring and Chromatic Numbers

### **Aim**

To implement greedy graph coloring algorithm that assigns colors to the vertices such as that no two adjacent vertices share the same color with the minimal chromatic number

### **Theory**

A **strictly proper vertex coloring** of a graph $G$ is a surjective mapping $c: V(G) \rightarrow S$, where $S$ is a finite set of colors, such that adjacent vertices receive distinct colors. For any edge $uv \in E(G)$, the condition $c(u) \neq c(v)$ must hold. A proper $k$-coloring partitions the vertex set into $k$ disjoint **independent sets** (color classes).

The primary objective is to determine the **chromatic number $\chi(G)$**, the absolute minimum $k$ for which $G$ is $k$-colorable. Since calculating $\chi(G)$ is computationally intractable (NP-hard) for arbitrary networks, researchers rely on the **greedy coloring algorithm** to establish valid structural upper bounds. This locally optimized sequential paradigm ensures a valid coloring while attempting to minimize the color palette index.

### **Algorithm: Greedy Coloring Algorithm Steps**

1. **Ordering:** Impose an arbitrary but fixed ordering on the vertices: $v_1, v_2, \dots, v_\nu$.
2. **Color Palette:** Initialize an ordered set of available colors $S = \{1, 2, 3, \dots\}$.
3. **Sequential Assignment:** For each vertex $v_i$ in the sequence:
    *   Examine the colors already assigned to the neighbors of $v_i$ that precede it in the ordering.
    *   Identify the set of used neighbor colors.
    *   Assign to $v_i$ the smallest-indexed color from $S$ that has **not** been used by any of its adjacent neighbors.
4. **Completion:** Repeat until every vertex in $V(G)$ has been assigned a color. The maximum index used represents the upper bound for the chromatic number provided by this specific vertex ordering.

### **Conclusion**

A python program to implement greedy graph coloring algorithm that assigns colors to the vertices such as that no two adjacent vertices share the same color with the minimal chromatic number was successfully implemented
