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

### 7. Graphs (Deep Dive)
**Nodes (V) and Edges (E)**.
#### 🛠️ Representations
-   **Adjacency List** (`O(V+E)` Space): `List<List<Integer>> graph = new ArrayList<>();`
-   **Adjacency Matrix** (`O(V^2)` Space): `int[][] graph = new int[V][V];` (Fast lookups, heavy space).

#### ⚡ Essential Traversals
1.  **DFS (Stack/Recursion)**:
    -   *Use Case*: Reachability, Cycle Detection, Topological Sort.
    ```java
    void dfs(int u, boolean[] visited, List<List<Integer>> adj) {
        visited[u] = true;
        for (int v : adj.get(u)) {
            if (!visited[v]) dfs(v, visited, adj);
        }
    }
    ```
2.  **BFS (Queue)**:
    -   *Use Case*: Shortest Path in Unweighted Graph.
    ```java
    void bfs(int start, List<List<Integer>> adj) {
        boolean[] visited = new boolean[V];
        Queue<Integer> q = new LinkedList<>(); // LinkedList OK for BFS queue
        q.offer(start); visited[start] = true;
        while (!q.isEmpty()) {
            int u = q.poll();
            for (int v : adj.get(u)) {
                if (!visited[v]) {
                    visited[v] = true;
                    q.offer(v);
                }
            }
        }
    }
    ```

3.  **Cycle Detection (Directed)**:
    -   Use 3 states: `0` (Unvisited), `1` (Visiting/Recursion Stack), `2` (Visited).
    -   If you hit a `1`, cycle found.

---

### 8. Advanced Data Structures (Deep Dive)
<details>
<summary><b>Trie (Prefix Tree) implementation</b></summary>

```java
class Trie {
    class TrieNode {
        TrieNode[] children = new TrieNode[26];
        boolean isEnd;
    }
    TrieNode root = new TrieNode();

    public void insert(String word) {
        TrieNode node = root;
        for (char c : word.toCharArray()) {
            if (node.children[c - 'a'] == null)
                node.children[c - 'a'] = new TrieNode();
            node = node.children[c - 'a'];
        }
        node.isEnd = true;
    }

    public boolean search(String word) {
        TrieNode node = root;
        for (char c : word.toCharArray()) {
            if (node.children[c - 'a'] == null) return false;
            node = node.children[c - 'a'];
        }
        return node.isEnd;
    }
}
```
</details>

<details>
<summary><b>Disjoint Set (Union-Find) Optimized</b></summary>

-   **Path Compression**: Point nodes directly to root during `find`.
-   **Union by Rank**: Attach smaller tree to larger tree.
-   **Time**: `O(α(N))` (Inverse Ackermann function) ≈ Constant.

```java
class UnionFind {
    int[] parent, rank;
    public UnionFind(int n) {
        parent = new int[n];
        rank = new int[n];
        for (int i=0; i<n; i++) parent[i] = i;
    }
    public int find(int x) {
        if (parent[x] != x) parent[x] = find(parent[x]); // Path Compression
        return parent[x];
    }
    public boolean union(int x, int y) {
        int rootX = find(x), rootY = find(y);
        if (rootX == rootY) return false; // Cycle detected / Already stored
        // Union by Rank
        if (rank[rootX] > rank[rootY]) parent[rootY] = rootX;
        else if (rank[rootX] < rank[rootY]) parent[rootX] = rootY;
        else {
            parent[rootY] = rootX;
            rank[rootX]++;
        }
        return true;
    }
}
```
</details>

<details>
<summary><b>Segment Tree (Range Sum Query)</b></summary>
Used for Range Queries `O(log N)` and Point Updates `O(log N)`.

```java
int[] tree; // Size 4*N
void build(int[] arr, int node, int start, int end) {
    if (start == end) tree[node] = arr[start];
    else {
        int mid = (start + end) / 2;
        build(arr, 2*node, start, mid);
        build(arr, 2*node+1, mid+1, end);
        tree[node] = tree[2*node] + tree[2*node+1];
    }
}
```
</details>

---

## ⚡ Algorithms

### 1. Sorting & Searching (Deep Dive)
#### ⚔️ Sorting Algorithms
1.  **Merge Sort** (`O(N log N)` Stable):
    -   *Divide*: Split array in half. *Conquer*: Recursively sort. *Combine*: Merge sorted halves.
    ```java
    void mergeSort(int[] arr, int l, int r) {
        if (l < r) {
            int m = l + (r - l) / 2;
            mergeSort(arr, l, m);
            mergeSort(arr, m + 1, r);
            merge(arr, l, m, r);
        }
    }
    // Merge logic: Use temp array, copy back.
    ```
2.  **Quick Sort** (`O(N log N)` Unstable):
    -   *Partition*: Pick pivot, move smaller to left, larger to right.
    ```java
    void quickSort(int[] arr, int low, int high) {
        if (low < high) {
            int pivotIndex = partition(arr, low, high);
            quickSort(arr, low, pivotIndex - 1);
            quickSort(arr, pivotIndex + 1, high);
        }
    }
    int partition(int[] arr, int low, int high) {
        int pivot = arr[high];
        int i = (low - 1);
        for (int j = low; j < high; j++) {
            if (arr[j] < pivot) {
                i++;
                swap(arr, i, j);
            }
        }
        swap(arr, i + 1, high);
        return i + 1;
    }
    ```

#### 🔎 Binary Search (Templates)
**Pre-condition**: Array MUST be sorted.
**Template 1: Standard (Find Exact)**
```java
int search(int[] nums, int target) {
    int lo = 0, hi = nums.length - 1;
    while (lo <= hi) {
        int mid = lo + (hi - lo) / 2;
        if (nums[mid] == target) return mid;
        else if (nums[mid] < target) lo = mid + 1;
        else hi = mid - 1;
    }
    return -1;
}
```
**Template 2: Lower Bound (First value >= target)**
```java
int lowerBound(int[] nums, int target) {
    int lo = 0, hi = nums.length;
    while (lo < hi) {
        int mid = lo + (hi - lo) / 2;
        if (nums[mid] >= target) hi = mid;
        else lo = mid + 1;
    }
    return lo; // Returns index of first element >= target
}
```
**Template 3: Upper Bound (First value > target)**
```java
int upperBound(int[] nums, int target) {
    int lo = 0, hi = nums.length;
    while (lo < hi) {
        int mid = lo + (hi - lo) / 2;
        if (nums[mid] > target) hi = mid;
        else lo = mid + 1;
    }
    return lo;
}
```

### 2. Graph Algorithms (Deep Dive)
<details>
<summary><b>Dijkstra's Algorithm (Shortest Path)</b></summary>
*Weighted, Non-negative Graphs.* `O(E log V)`.

```java
public int[] dijkstra(int n, List<List<int[]>> adj, int src) {
    int[] dist = new int[n];
    Arrays.fill(dist, Integer.MAX_VALUE);
    dist[src] = 0;
    
    // Min-Heap: [node, distance]
    PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> a[1] - b[1]);
    pq.offer(new int[]{src, 0});
    
    while (!pq.isEmpty()) {
        int[] curr = pq.poll();
        int u = curr[0], d = curr[1];
        
        if (d > dist[u]) continue; // Optimization: Skip stale nodes
        
        for (int[] edge : adj.get(u)) {
            int v = edge[0], weight = edge[1];
            if (dist[u] + weight < dist[v]) {
                dist[v] = dist[u] + weight;
                pq.offer(new int[]{v, dist[v]});
            }
        }
    }
    return dist;
}
```
</details>

<details>
<summary><b>Topological Sort (Kahn's Algo)</b></summary>
*DAGs Only. Course Schedule.* `O(V + E)`.

```java
public int[] topoSort(int k, int[][] edges) {
    List<List<Integer>> adj = new ArrayList<>();
    int[] inDegree = new int[k + 1];
    // Build Graph & In-Degree
    for (int[] e : edges) {
        adj.get(e[1]).add(e[0]);
        inDegree[e[0]]++;
    }
    
    Queue<Integer> q = new LinkedList<>();
    for (int i = 1; i <= k; i++) 
        if (inDegree[i] == 0) q.offer(i);
        
    int[] res = new int[k];
    int idx = 0;
    while (!q.isEmpty()) {
        int u = q.poll();
        res[idx++] = u;
        for (int v : adj.get(u)) {
            inDegree[v]--;
            if (inDegree[v] == 0) q.offer(v);
        }
    }
    return idx == k ? res : new int[0]; // Cycle detected if idx != k
}
```
</details>

<details>
<summary><b>Minimum Spanning Tree (Prim's vs Kruskal)</b></summary>
- **Prim's**: Like Dijkstra. Grow tree from source. Best for *Dense* graphs.
- **Kruskal's**: Sort edges by weight. Union-Find to add if no cycle. Best for *Sparse* graphs.
</details>

### 3. Dynamic Programming (Deep Dive)
**Memoization (Top-Down) vs Tabulation (Bottom-Up)**.
State Definition is everything.

#### ⚔️ Common Patterns
1.  **0/1 Knapsack (Include/Exclude)**:
    ```java
    // dp[i][w] = Max value using first 'i' items with capacity 'w'
    for (int i = 1; i <= n; i++) {
        for (int w = 0; w <= capacity; w++) {
            if (weights[i-1] <= w) 
                dp[i][w] = Math.max(dp[i-1][w], values[i-1] + dp[i-1][w-weights[i-1]]);
            else 
                dp[i][w] = dp[i-1][w];
        }
    }
    ```
2.  **Longest Common Subsequence (LCS)**:
    ```java
    // dp[i][j] = LCS of text1[0..i] and text2[0..j]
    if (text1.charAt(i-1) == text2.charAt(j-1))
        dp[i][j] = 1 + dp[i-1][j-1];
    else
        dp[i][j] = Math.max(dp[i-1][j], dp[i][j-1]);
    ```
3.  **Unbounded Knapsack (Coin Change)**:
    -   Iterate `dp` array. Inner loop iterates coins.
    ```java
    Arrays.fill(dp, amount + 1); dp[0] = 0;
    for (int i = 1; i <= amount; i++) {
        for (int coin : coins) {
            if (coin <= i) dp[i] = Math.min(dp[i], dp[i - coin] + 1);
        }
    }
    ```

### 4. Backtracking (Deep Dive)
**Visualizing the Decision Tree**.
#### 🧩 Template & N-Queens Example
```java
void solveNQueens(int row, char[][] board, List<List<String>> res) {
    if (row == board.length) {
        res.add(construct(board));
        return;
    }
    for (int col = 0; col < board.length; col++) {
        if (isValid(board, row, col)) {
            board[row][col] = 'Q';
            solveNQueens(row + 1, board, res);
            board[row][col] = '.'; // Backtrack
        }
    }
}
```

### 5. Greedy & Maths (Deep Dive)
#### 🧠 Greedy Logic
-   **Structure**: Sort data -> Iterate -> make locally optimal choice.
-   **Interval Scheduling**: Sort by **End Time**. Pick first, then pick next valid.
-   **Merge Intervals**: Sort by **Start Time**.

#### 🔢 Math Cheatsheet
-   **GCD (Euclidean)**: `return b == 0 ? a : gcd(b, a % b);`
-   **LCM**: `(a * b) / gcd(a, b)`
-   **Prime Sieve (Sieve of Eratosthenes)**:
    ```java
    boolean[] isPrime = new boolean[n + 1];
    Arrays.fill(isPrime, true);
    for (int p = 2; p * p <= n; p++) {
        if (isPrime[p]) {
            for (int i = p * p; i <= n; i += p)
                isPrime[i] = false;
        }
    }
    ```
-   **Modular Arithmetic** (Prevent Overflow):
    -   `(a + b) % M`
    -   `(a * b) % M`
    -   **(a - b)**: `((a - b) % M + M) % M` (Java's `%` can be negative!)


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
