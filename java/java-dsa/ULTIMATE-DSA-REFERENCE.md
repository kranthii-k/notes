# 🚀 ULTIMATE DSA REFERENCE SHEET & JAVA CHEATSHEET 🚀

> **"The One Sheet To Rule Them All"**
> *A comprehensive, God-tier reference for Data Structures, Algorithms, and Java Implementation Patterns.*

---

## 📜 Table of Contents

- [⚡ Quick Reference (Complexity & Decision Tree)](#-quick-reference)
- [🎯 Data Structures](#-data-structures)
- [⚡ Algorithms](#-algorithms)
- [💻 Java Syntax & Tricks](#-java-syntax--tricks)
- [🧠 Patterns & Meta-Skills](#-patterns--meta-skills)
- [🎤 Interview Strategy](#-interview-strategy)

---

## ⚡ Quick Reference

### 1. Time & Space Complexity Cheat Sheet

| Data Structure | Access | Search | Insertion | Deletion | Space |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Array** | `O(1)` | `O(N)` | `O(N)` | `O(N)` | `O(N)` |
| **Stack/Queue** | `O(N)` | `O(N)` | `O(1)` | `O(1)` | `O(N)` |
| **HashMap/Set** | `O(1)`* | `O(1)`* | `O(1)`* | `O(1)`* | `O(N)` |
| **B-Tree (BST)** | `O(log N)` | `O(log N)` | `O(log N)` | `O(log N)` | `O(N)` |
| **Heap (Min/Max)** | `O(1)` (peek) | `O(N)` | `O(log N)` | `O(log N)` | `O(N)` |
| **Union-Find** | N/A | `O(α(N))` | `O(α(N))` | N/A | `O(N)` |

> *Amortized time. Worst case `O(N)` for HashMaps with bad collisions.*

### 2. Decision Tree: "What Data Structure to Use?"

| If you need to... | Use this Data Structure |
| :--- | :--- |
| Store key-value pairs | **HashMap** (Unordered), **TreeMap** (Sorted), **LinkedHashMap** (Insertion Order) |
| Store unique elements | **HashSet**, **TreeSet**, **LinkedHashSet** |
| Access elements by index | **ArrayList** |
| Fast insertion/removal at ends | **ArrayDeque** (Stack/Queue behavior) |
| Process tasks by priority | **PriorityQueue** (Heap) |
| Find connected components | **Disjoint Set (Union-Find)** or **DFS/BFS** |
| Range queries (Sum, Min, Max) | **Segment Tree** or **Fenwick Tree** |
| Check prefix existence | **Trie** |
| Detect cycles in graph | **DFS** (Directed) or **Union-Find** (Undirected) |
| Shortest Path | **BFS** (Unweighted), **Dijkstra** (Weighted > 0), **Bellman-Ford** (Negative weights) |

### 3. Common Constraints & Complexity Guidelines

| N (Input Size) | Expected Time Complexity | Algorithm Examples |
| :--- | :--- | :--- |
| `N <= 10` | `O(N!)` or `O(N^6)` | Permutations, Brute force |
| `N <= 20` | `O(2^N)` | Subsets, Backtracking |
| `N <= 100` | `O(N^4)` | Floyd-Warshall, DP (3D) |
| `N <= 500` | `O(N^3)` | Matrix Multiplication, DP (2D) |
| `N <= 2000` | `O(N^2)` | Bubble Sort, 2-Nested Loops, DP (2D heavy) |
| `N <= 10^5` | `O(N log N)` | Merge Sort, Heap Sort, TreeMap Ops |
| `N <= 10^6` | `O(N)` | Hash Maps, Two Pointers, Sliding Window |
| `N > 10^9` | `O(log N)` or `O(1)` | Binary Search, Math formulas |

---

## 🎯 Data Structures

## 🎯 Data Structures (The Arsenal)

### 1. Arrays & Strings (Deep Dive)
**Under the Hood**: Contiguous memory blocks. Random access `O(1)`. Fixed size.
- **Memory Layout**: `[Header | Length | Element 0 | Element 1 | ...]`
- **Cache Locality**: Excellent (CPU prefetching works best here).

#### 🛠️ Java `ArrayList<E>` Internals
- **Dynamic Resizing**: When full, creates new array of size `oldCapacity + (oldCapacity >> 1)` (approx 1.5x interaction).
- **Time Complexity**:
  - `get(i)`: `O(1)` - Direct memory offset.
  - `add(e)`: `O(1)` amortized. Worst case `O(N)` when resizing.
  - `remove(i)`: `O(N)` - Must shift subsequent elements.

#### 🔑 Key Methods & Tricks
```java
// Arrays Utility
int[] arr = {5, 1, 9, 3};
Arrays.sort(arr); // Dual-Pivot Quicksort O(N log N)
Arrays.fill(arr, -1); // Initialize DP arrays
// Copying (Native/Fastest)
int[] copy = new int[arr.length];
System.arraycopy(arr, 0, copy, 0, arr.length); 

// Strings (Immutable)
String s = "hello";
char[] chars = s.toCharArray(); // Mutable char array
// String Pool: s1 = "hi", s2 = "hi" -> s1 == s2 (true)
// New Object: s1 = new String("hi") -> s1 == s2 (false)

// StringBuilder (Mutable - Not Thread Safe but Faster)
StringBuilder sb = new StringBuilder();
sb.append("a").append("b"); // O(1) amortized
sb.setCharAt(0, 'z');
sb.reverse(); // In-place O(N)
```

> [!IMPORTANT]
> **String Concatenation**: Never use `s += "c"` in a loop! It creates `O(N^2)` garbage. Always use `StringBuilder`.

---

### 2. Linked Lists (Deep Dive)
**Under the Hood**: Nodes scattered in memory. `O(N)` access.
- **Java `LinkedList<E>`**: Doubly-linked list. Holds references to `prev` and `next`.
- **Memory Overhead**: High (Node object + 2 references + data). ~24 bytes overhead per element (64-bit JVM).

#### 🛠️ Internal Implementation (Doubly Linked)
```java
class ListNode {
    int val;
    ListNode next, prev;
    ListNode(int x) { val = x; }
}
```

#### ⚡ Essential Patterns
1.  **Runner Technique (Fast & Slow)**:
    -   *Cycle Detection*: `slow` moves 1 step, `fast` moves 2. If they meet, cycle exists.
    -   *Middle Element*: When `fast` reaches end, `slow` is at middle.
2.  **Dummy Pointer**:
    -   Use `dummy.next` to handle edge cases where `head` might change (e.g., deleting head, merging lists).
    ```java
    ListNode dummy = new ListNode(0);
    ListNode curr = dummy;
    // ... operations ...
    return dummy.next;
    ```
3.  **Reversing a List (Iterative)**:
    ```java
    public ListNode reverseList(ListNode head) {
        ListNode prev = null;
        ListNode curr = head;
        while (curr != null) {
            ListNode nextTemp = curr.next; // Save next
            curr.next = prev;              // Reverse pointer
            prev = curr;                   // Advance prev
            curr = nextTemp;               // Advance curr
        }
        return prev; // New head
    }
    ```

### 3. Stacks & Queues (Deep Dive)
**LIFO (Last-In-First-Out) & FIFO (First-In-First-Out)**.

#### 🛠️ Java `ArrayDeque<E>` (Recommended)
- **Why not `Stack`?** `Stack` extends `Vector` and is `synchronized` (slow).
- **Why not `LinkedList`?** `LinkedList` creates objects for every node -> heavy GC pressure. `ArrayDeque` uses a circular array buffer.
- **Internals**: Circular array. Doubles capacity when full. `head` and `tail` pointers.
- **Methods**:
  - **Stack**: `push()`, `pop()`, `peek()`.
  - **Queue**: `offer()`, `poll()`, `peek()`.

#### ⚡ Essential Patterns
1.  **Monotonic Stack** (Find Next Greater Element):
    ```java
    // Stores indices, keeping values in decreasing order
    Deque<Integer> stack = new ArrayDeque<>();
    for (int i = 0; i < nums.length; i++) {
        while (!stack.isEmpty() && nums[stack.peek()] < nums[i]) {
            int index = stack.pop();
            result[index] = nums[i]; // nums[i] is Next Greater for nums[index]
        }
        stack.push(i);
    }
    ```
2.  **BFS Queue (Level Order)**:
    ```java
    Deque<TreeNode> q = new ArrayDeque<>();
    q.offer(root);
    while (!q.isEmpty()) {
        int size = q.size(); // Capture size for level processing
        for (int i = 0; i < size; i++) {
            TreeNode node = q.poll();
            if (node.left != null) q.offer(node.left);
            if (node.right != null) q.offer(node.right);
        }
    }
    ```

---

### 4. Heaps (Priority Queue) (Deep Dive)
**Under the Hood**: Complete Binary Tree backed by an array.
- **Index Math**: For node at `i`:
  - `Left Child`: `2*i + 1`
  - `Right Child`: `2*i + 2`
  - `Parent`: `(i - 1) / 2`
- **Time Complexity**:
  - `offer()` (Sift Up): `O(log N)`
  - `poll()` (Sift Down): `O(log N)`
  - `peek()`: `O(1)`
  - **Build Heap**: `O(N)` (using siftDown from bottom-up), NOT `O(N log N)`.

#### 🛠️ Java `PriorityQueue<E>`
`PriorityQueue<Integer> minPQ = new PriorityQueue<>();` (Default Min-Heap)
`PriorityQueue<Integer> maxPQ = new PriorityQueue<>((a, b) -> b - a);` (Max-Heap)

#### ⚡ Essential Patterns
1.  **Top K Elements**:
    -   Keep a Min-Heap of size K.
    -   If `nums[i] > pq.peek()`, `poll()` and `offer(nums[i])`.
    -   At the end, Heap has the K largest elements.
2.  **Median Finder**:
    -   Use two heaps: `maxPQ` (lower half) and `minPQ` (upper half).
    -   Keep sizes balanced. Median is `maxPQ.peek()` or `(maxPQ.peek() + minPQ.peek()) / 2.0`.

### 5. Hash Maps & Sets
*The O(1) magic.*
- **HashMap**: `map.put(k, v)`, `map.get(k)`, `map.containsKey(k)`.
- **HashSet**: `set.add(v)`, `set.contains(v)`.
- **Tricks**:
  - `map.getOrDefault(key, 0)` -> Very useful for frequency counting.
  - `map.computeIfAbsent(key, k -> new ArrayList<>()).add(val)` -> Grouping.
  - `for (Map.Entry<K, V> entry : map.entrySet())` -> Iterating.

### 5. Hash Maps & Sets (Deep Dive)
**The O(1) Magic**. Key-Value definitions.
#### 🛠️ Internal Implementation (Java `HashMap`)
-   **Concept**: Array of "Buckets" (Nodes). Index = `(n - 1) & hash`.
-   **Collision Resolution**: **Separate Chaining** (LinkedList).
-   **Java 8+ Optimization**: When a bucket has > 8 nodes, it converts from LinkedList to **Red-Black Tree** (`O(N)` -> `O(log N)`).
-   **Load Factor**: Default `0.75`. Resizes (doubles) when `size > capacity * 0.75`. Rehashes all keys.

#### 🔑 Key Methods
```java
// Grouping Anagrams
Map<String, List<String>> map = new HashMap<>();
// computeIfAbsent: "If key missing, put new ArrayList, then return it"
map.computeIfAbsent(sortedKey, k -> new ArrayList<>()).add(originalString);

// Frequency Count
Map<Integer, Integer> counts = new HashMap<>();
// getOrDefault: "Get count or 0"
counts.put(num, counts.getOrDefault(num, 0) + 1);

// Iterating Efficiently
for (Map.Entry<Integer, Integer> entry : counts.entrySet()) {
    int key = entry.getKey();
    int val = entry.getValue();
}
```

---

### 6. Trees (Binary, BST, AVL) (Deep Dive)
**Hierarchical Data**.
-   **Binary Search Tree (BST)**: Left < Root < Right.
-   **Balanced Trees**: AVL, Red-Black (Java `TreeMap`/`TreeSet`).

#### 🛠️ Traversals (The Holy Trinity)
1.  **Level Order (BFS)**: Use Queue.
2.  **Depth First Search (DFS)**:
    ```java
    // 1. Recursive
    void dfs(TreeNode root) {
        if (root == null) return;
        // Preorder: process(root)
        dfs(root.left);
        // Inorder: process(root) -> Sorted for BST
        dfs(root.right);
        // Postorder: process(root) -> Delete/Bottom-up
    }

    // 2. Iterative Inorder (Stack)
    public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> res = new ArrayList<>();
        Deque<TreeNode> stack = new ArrayDeque<>();
        TreeNode curr = root;
        while (curr != null || !stack.isEmpty()) {
            while (curr != null) { // Go Left
                stack.push(curr);
                curr = curr.left;
            }
            curr = stack.pop(); // Process Node
            res.add(curr.val);
            curr = curr.right; // Go Right
        }
        return res;
    }
    ```

#### ⚡ Essential Patterns
-   **Validate BST**: Keep `min` and `max` boundaries.
    ```java
    boolean isValid(TreeNode node, long min, long max) {
        if (node == null) return true;
        if (node.val <= min || node.val >= max) return false;
        return isValid(node.left, min, node.val) && isValid(node.right, node.val, max);
    }
    ```
-   **Lowest Common Ancestor (LCA)**:
    -   *BST*: If both < root, go left. If both > root, go right. Else root is split point.
    -   *Binary Tree*: Look left, look right. If both return non-null, root is LCA.

### 7. Graphs
*Nodes and edges.*
- **Representation**:
  - **Adjacency List** (Most common): `List<List<Integer>> adj = new ArrayList<>();`
  - **Adjacency Matrix** (Dense graphs): `int[][] adj = new int[N][N];`
- **Traversals**:
  - **DFS**: Stack/Recursion. Exhausts one path.
  - **BFS**: Queue. Shortest path in unweighted graph.

### 8. Advanced Data Structures
<details>
<summary>Click to expand Trie & Union-Find</summary>

#### Trie (Prefix Tree)
Used for string search, prefix counting.
```java
class TrieNode {
    TrieNode[] children = new TrieNode[26];
    boolean isEnd;
}
```

#### Disjoint Set (Union-Find)
Used for connected components, cycle detection.
```java
class UnionFind {
    int[] parent;
    public UnionFind(int n) {
        parent = new int[n];
        for (int i=0; i<n; i++) parent[i] = i;
    }
    public int find(int x) {
        if (parent[x] != x) parent[x] = find(parent[x]); // Path compression
        return parent[x];
    }
    public void union(int x, int y) {
        parent[find(x)] = find(y);
    }
}
```
</details>

---

## ⚡ Algorithms

### 1. Sorting & Searching
- **Sorting**: `O(N log N)` best.
  - **Quick Sort**: Unstable, avg `O(N log N)`.
  - **Merge Sort**: Stable, `O(N log N)`, `O(N)` space.
  - **Java**: `Arrays.sort(primitive)` = Dual-Pivot Quicksort. `Collections.sort(obj)` = Timsort (Merge+Insertion).
- **Binary Search**: Sorted arrays/monotonic functions.
```java
int binarySearch(int[] nums, int target) {
    int left = 0, right = nums.length - 1;
    while (left <= right) {
        int mid = left + (right - left) / 2; // Prevent overflow
        if (nums[mid] == target) return mid;
        else if (nums[mid] < target) left = mid + 1;
        else right = mid - 1;
    }
    return -1;
}
```

### 2. Graph Algorithms
<details>
<summary>Click to expand Dijkstra, Topo Sort, etc.</summary>

#### Shortest Path (Dijkstra)
For weighted, non-negative graphs.
```java
// PQ stores [node, dist] sorted by dist
PriorityQueue<int[]> pq = new PriorityQueue<>((a,b) -> a[1] - b[1]);
pq.offer(new int[]{start, 0});
// Use dist[] array initialized to MAX_VALUE
```

#### Topological Sort (Kahn's Algorithm)
For course schedule / dependency resolution (DAG).
1. Compute in-degree for all nodes.
2. Add nodes with `0` in-degree to Queue.
3. Poll, reduce in-degree of neighbors. If neighbor becomes `0`, add to Queue.
</details>

### 3. Dynamic Programming (DP)
*Break it down.*
- **Top-Down (Memoization)**: Recursion + Cache (`Map` or `Array`).
- **Bottom-Up (Tabulation)**: Iteration + Array.
- **Common Patterns**:
  - **1D**: Climbing Stairs, House Robber (`dp[i] = max(dp[i-1], dp[i-2] + nums[i])`).
  - **2D**: LCS, Edit Distance, Knapsack (`dp[i][w]`).
  - **Knapsack 0/1**: `dp[i][w] = max(dp[i-1][w], val[i] + dp[i-1][w-wt[i]])`.
  - **Unbounded Knapsack**: Iterate items inner loop, capacity outer.

### 4. Backtracking
*Try everything.*
**Template**:
```java
void backtrack(path, options) {
    if (goal reached) { result.add(path); return; }
    for (choice : options) {
        if (isValid(choice)) {
            make(choice);
            backtrack(newPath, options);
            undo(choice); // Backtrack
        }
    }
}
```
**Examples**: N-Queens, Sudoku, Subsets, Permutations.

### 5. Greedy & Maths
- **Greedy**: Interval Scheduling (Sort by end time), Huffman Coding.
- **Math**:
  - **GCD**: `return b == 0 ? a : gcd(b, a % b);`
  - **Sieve of Eratosthenes**: Find primes up to N.
  - **Modulo**: `(a + b) % M`, `(a * b) % M`.


---

## 💻 Java Syntax & Tricks

### 1. Collections Framework
- **List**: `ArrayList` (Resizeable), `LinkedList` (Nodes).
- **Set**: `HashSet` (Unordered), `TreeSet` (Sorted), `LinkedHashSet` (Order).
- **Map**: `HashMap` (Unordered), `TreeMap` (Sorted Keys), `LinkedHashMap` (Order).
- **Queue**: `LinkedList` or `PriorityQueue`.
- **Deque**: `ArrayDeque` (Stack/Queue).

### 2. Essential Methods
- **String**: `.length()`, `.charAt(i)`, `.substring(i, j)`, `.indexOf(s)`, `.toCharArray()`, `.trim()`, `.split(regex)`.
- **Arrays**: `Arrays.sort()`, `Arrays.fill()`, `Arrays.equals()`, `Arrays.copyOf()`.
- **Collections**: `Collections.sort()`, `Collections.reverse()`, `Collections.max()`.
- **Math**: `Math.max(a, b)`, `Math.abs()`, `Math.pow()`, `Math.sqrt()`, `Math.floor()`.

### 3. Stream API Wizardry
```java
// Filter & Map
List<String> result = list.stream()
    .filter(s -> s.startsWith("A"))
    .map(String::toUpperCase)
    .collect(Collectors.toList());

// Array to IntStream
int sum = Arrays.stream(nums).sum();
```

### 4. BigNumbers
- **BigInteger**: `new BigInteger("123")`, `.add()`, `.multiply()`.
- **BigDecimal**: Precision money math.


---

## 🧠 Patterns & Meta-Skills

### 1. Sliding Window
- **Fixed Size**: Slide window, add right, remove left.
- **Variable Size**: Expand `right`, shrink `left` while condition met (`while (invalid) left++`).

### 2. Two Pointers
- **Converging**: `left = 0, right = n-1`. (e.g., 2Sum Sorted, Palindrome).
- **Parallel**: `p1, p2` from start. (e.g., Merge Sorted Arrays).

### 3. Fast & Slow Pointers (Tortoise & Hare)
- **Cycle Detection**: Linked List cycle.
- **Middle of List**: Slow moves 1, Fast moves 2.

### 4. Monotonic Stack
- **Next Greater Element**: Keep stack decreasing.
- **Daily Temperatures**: Store indices.

### 5. Top 'K' Elements
- **Heap**: Use Min-Heap of size K to find Top K Largest.
- **QuickSelect**: Average `O(N)` find Kth element.

### 6. Merge Intervals
- **Sort**: Always sort by `start` time first.
- **Iterate**: If `curr.start <= prev.end`, merge. Else add new.


---
## 🎤 Interview Strategy

### 🛡️ The 4-Step Framework
1.  **Understand & Clarify**: "What is the range of N?", "Can inputs be negative?", "Duplicates allowed?"
2.  **Plan (Brute Force -> Optimize)**: Start with $O(N^2)$? Can we do $O(N \log N)$ or $O(N)$?
3.  **Code (Clean & Modular)**: Use helper functions! Write readable variable names.
4.  **Test (Dry Run)**:
    -   Happy Path
    -   Edge Cases (Null, Empty, Single element, Max/Min Integers)

### 🚨 Common Pitfalls
> [!WARNING]
> -   **Integer Overflow**: Use `long`? `Math.addExact()`?
> -   **Concurrent Modification**: Don't remove from a list while iterating (use `Iterator.remove()`).
> -   **Map Keys**: Mutable objects as keys = disaster.
> -   **Stack/Queue Empty**: Always check `!isEmpty()` before `pop()`/`poll()`.

---
*Created by the Anti-Gravity Code Chef Supreme for the ultimate coding warrior.* 🛡️⚔️
