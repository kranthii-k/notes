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

### 1. Arrays & Strings
*The bread and butter.*
- **Java**: `int[] arr = new int[N];`, `Arrays.sort(arr)`, `Arrays.fill(arr, -1)`
- **StringBuilder**: Always use for string concatenation in loops. `sb.append()`, `sb.reverse()`.
- **2D Arrays**: `int[][] matrix = new int[R][C];`
> [!TIP]
> **Sliding Window**: Use for contiguous subarrays.
> **Two Pointers**: Use for sorted arrays or palindrome checks.

### 2. Linked Lists
*Nodes and pointers.*
```java
class ListNode { int val; ListNode next; ListNode(int x) { val = x; } }
```
- **Dummy Node**: `ListNode dummy = new ListNode(0); dummy.next = head;` (Simplifies head edge cases).
- **Fast & Slow Pointers**: Detect cycle (`Floyd's`), Find middle `slow = head, fast = head`.

### 3. Stacks & Queues
*LIFO & FIFO.*
- **Stack**: Use `ArrayDeque<Integer> stack = new ArrayDeque<>();`. methods: `push()`, `pop()`, `peek()`.
- **Queue**: Use `ArrayDeque<Integer> queue = new ArrayDeque<>();`. methods: `offer()`, `poll()`, `peek()`.
> [!NOTE]
> `Stack` class is legacy. Use `ArrayDeque` (faster, no sync).

### 4. Heaps (Priority Queue)
*Ordering the chaos.*
- **Min-Heap** (Default): `PriorityQueue<Integer> pq = new PriorityQueue<>();`
- **Max-Heap**: `PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());`
- **Custom Object**: `new PriorityQueue<>((a, b) -> a.val - b.val);`
- **Time**: Add/Poll `O(log N)`, Peek `O(1)`.

### 5. Hash Maps & Sets
*The O(1) magic.*
- **HashMap**: `map.put(k, v)`, `map.get(k)`, `map.containsKey(k)`.
- **HashSet**: `set.add(v)`, `set.contains(v)`.
- **Tricks**:
  - `map.getOrDefault(key, 0)` -> Very useful for frequency counting.
  - `map.computeIfAbsent(key, k -> new ArrayList<>()).add(val)` -> Grouping.
  - `for (Map.Entry<K, V> entry : map.entrySet())` -> Iterating.

### 6. Trees (Binary & BST)
*Recursive structures.*
```java
class TreeNode { int val; TreeNode left, right; TreeNode(int x) { val = x; } }
```
- **Traversals**:
  - **Inorder** (Left, Root, Right): Sorted order for BST.
  - **Preorder** (Root, Left, Right): Serialization.
  - **Postorder** (Left, Right, Root): Deleting, Bottom-up logic.

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
