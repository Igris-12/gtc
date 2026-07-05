#### **Experiment No:** 4 | **Date:** 05/02/2026

# Graphical Degree Sequences

### **Aim**

To check if the given degree sequence is graphical or not graphical using Handshaking Lemma and Havel-Hakimi Theorem.

### **Theory**

A finite sequence of non-negative integers $D = (d_1, d_2, \dots, d_\nu)$ is the degree sequence of a simple graph $G$ if each $d_i$ represents the degree of a corresponding vertex. Graphicality refers to whether a simple, undirected graph (no loops or multiple edges) exists that realizes a given sequence $D$.

Before recursive verification, a sequence must satisfy several necessary conditions:
*   **Handshaking Lemma:** The sum of all vertex degrees must be even (equal to twice the edge set cardinality). An odd sum implies a non-graphic sequence.
*   **Maximum Degree Constraint:** In a simple graph of order $\nu$, the maximum possible degree is $\nu - 1$. If any $d_i \ge \nu$, the sequence is non-graphic.

The **Havel-Hakimi Theorem** provides a deterministic, recursive method for verification based on a combinatorial reduction strategy. It states that a sequence $D$ (sorted non-increasingly) is graphic if and only if the reduced sequence $D'$, formed by removing $d_1$ and decrementing the subsequent $d_1$ terms, is also graphic.

### **Algorithm: Havel-Hakimi Algorithm Steps**

1. **Sort:** Order the sequence such that terms are non-increasing: $d_1 \ge d_2 \ge \dots \ge d_\nu$.
2. **Base Case Evaluation:** If all elements in the sequence are zero, the sequence is graphical (representing a null graph).
3. **Reduction:** Excise the leading maximum term $d_1$ from the sequence.
4. **Decrement:** Subtract 1 from the subsequent $d_1$ terms in the remaining sequence. This simulates connecting the highest-degree vertex to the next $d_1$ available vertices.
5. **Validation:**
    *   If the decrement operation results in any negative integer, the initial sequence is proven **non-graphic**.
    *   If all terms remain non-negative, re-sort the reduced sequence and repeat from Step 2.

### **Conclusion**

A program to check if the given degree sequence is graphical or not graphical using Handshaking Lemma and Havel-Hakimi Theorem was successfully implemented
