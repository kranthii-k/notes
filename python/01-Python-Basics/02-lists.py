# ===================================================
# PROGRAM 1.2: LISTS - The Most Important Data Structure
# ===================================================

"""
LISTS IN PYTHON
- Ordered collection of items
- Mutable (can be changed after creation)
- Allow duplicate elements
- Can contain mixed data types
- Most commonly used data structure in ML/DS
"""

# ===================================================
# 1. CREATING LISTS
# ===================================================

print("=" * 60)
print("1. CREATING LISTS")
print("=" * 60)

# Empty list
empty_list = []
print(f"Empty list: {empty_list}")

# List with integers (e.g., image dimensions)
image_dimensions = [224, 224, 3]  # Height, Width, Channels
print(f"Image dimensions: {image_dimensions}")

# List with floats (e.g., training losses)
training_losses = [2.45, 1.98, 1.52, 1.23, 0.95]
print(f"Training losses: {training_losses}")

# List with strings (e.g., class labels)
class_labels = ["cat", "dog", "bird", "fish"]
print(f"Class labels: {class_labels}")

# Mixed data types
model_info = ["ResNet50", 50, 0.95, True]
print(f"Model info (mixed types): {model_info}")

# Nested lists (e.g., 2D array/matrix)
confusion_matrix = [
    [50, 2, 1],
    [3, 45, 2],
    [1, 1, 48]
]
print(f"Confusion matrix:\n{confusion_matrix}")

# Using list() constructor
numbers = list(range(5))  # [0, 1, 2, 3, 4]
print(f"Numbers from range: {numbers}")

# ===================================================
# 2. ACCESSING LIST ELEMENTS (INDEXING)
# ===================================================

print("\n" + "=" * 60)
print("2. ACCESSING LIST ELEMENTS")
print("=" * 60)

fruits = ["apple", "banana", "cherry", "date", "elderberry"]

# Positive indexing (from start)
print(f"First fruit: {fruits[0]}")       # apple
print(f"Third fruit: {fruits[2]}")       # cherry

# Negative indexing (from end)
print(f"Last fruit: {fruits[-1]}")       # elderberry
print(f"Second last: {fruits[-2]}")      # date

# Accessing nested lists
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(f"Element at row 1, col 2: {matrix[1][2]}")  # 6

# ===================================================
# 3. LIST SLICING
# ===================================================

print("\n" + "=" * 60)
print("3. LIST SLICING [start:end:step]")
print("=" * 60)

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"Original list: {numbers}")

# Basic slicing
print(f"First 5 elements: {numbers[:5]}")        # [0, 1, 2, 3, 4]
print(f"Last 5 elements: {numbers[-5:]}")        # [5, 6, 7, 8, 9]
print(f"Elements 3 to 7: {numbers[3:7]}")        # [3, 4, 5, 6]

# Step slicing
print(f"Every 2nd element: {numbers[::2]}")      # [0, 2, 4, 6, 8]
print(f"Reverse list: {numbers[::-1]}")          # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

# ML Example: Train-Test Split
dataset = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
train_data = dataset[:8]   # First 80%
test_data = dataset[8:]    # Last 20%
print(f"Training data (80%): {train_data}")
print(f"Testing data (20%): {test_data}")

# ===================================================
# 4. MODIFYING LISTS
# ===================================================

print("\n" + "=" * 60)
print("4. MODIFYING LISTS")
print("=" * 60)

scores = [85, 90, 78, 92, 88]
print(f"Original scores: {scores}")

# Changing single element
scores[2] = 95
print(f"After updating index 2: {scores}")

# Changing multiple elements
scores[0:2] = [88, 93]
print(f"After updating first two: {scores}")

# ===================================================
# 5. LIST METHODS - ADDING ELEMENTS
# ===================================================

print("\n" + "=" * 60)
print("5. ADDING ELEMENTS TO LISTS")
print("=" * 60)

# append() - Add single element at end
epochs = [1, 2, 3]
print(f"Original: {epochs}")
epochs.append(4)
print(f"After append(4): {epochs}")

# extend() - Add multiple elements at end
epochs.extend([5, 6])
print(f"After extend([5, 6]): {epochs}")

# insert() - Add element at specific position
accuracies = [0.85, 0.90, 0.95]
accuracies.insert(1, 0.88)  # Insert at index 1
print(f"After insert(1, 0.88): {accuracies}")

# ===================================================
# 6. LIST METHODS - REMOVING ELEMENTS
# ===================================================

print("\n" + "=" * 60)
print("6. REMOVING ELEMENTS FROM LISTS")
print("=" * 60)

models = ["CNN", "RNN", "LSTM", "GRU", "Transformer"]
print(f"Original models: {models}")

# remove() - Remove first occurrence of value
models.remove("LSTM")
print(f"After remove('LSTM'): {models}")

# pop() - Remove and return element at index (default: last)
removed_model = models.pop()
print(f"Popped model: {removed_model}")
print(f"After pop(): {models}")

removed_model = models.pop(1)  # Remove at index 1
print(f"Popped model at index 1: {removed_model}")
print(f"After pop(1): {models}")

# clear() - Remove all elements
temp_list = [1, 2, 3]
temp_list.clear()
print(f"After clear(): {temp_list}")

# del statement - Delete by index or slice
numbers = [0, 1, 2, 3, 4, 5]
del numbers[2]  # Delete index 2
print(f"After del numbers[2]: {numbers}")

# ===================================================
# 7. LIST METHODS - SEARCHING & COUNTING
# ===================================================

print("\n" + "=" * 60)
print("7. SEARCHING AND COUNTING")
print("=" * 60)

predictions = ["cat", "dog", "cat", "bird", "cat", "dog"]

# count() - Count occurrences
cat_count = predictions.count("cat")
print(f"Number of 'cat' predictions: {cat_count}")

# index() - Find first occurrence index
first_dog_index = predictions.index("dog")
print(f"First 'dog' at index: {first_dog_index}")

# in operator - Check membership
print(f"Is 'bird' in predictions? {'bird' in predictions}")
print(f"Is 'fish' in predictions? {'fish' in predictions}")

# ===================================================
# 8. LIST METHODS - SORTING & REVERSING
# ===================================================

print("\n" + "=" * 60)
print("8. SORTING AND REVERSING")
print("=" * 60)

scores = [85, 92, 78, 95, 88, 76]
print(f"Original scores: {scores}")

# sort() - Sort in place (ascending)
scores.sort()
print(f"After sort(): {scores}")

# sort(reverse=True) - Sort descending
scores.sort(reverse=True)
print(f"After sort(reverse=True): {scores}")

# sorted() - Return new sorted list (original unchanged)
original = [3, 1, 4, 1, 5]
sorted_list = sorted(original)
print(f"Original (unchanged): {original}")
print(f"Sorted copy: {sorted_list}")

# reverse() - Reverse in place
numbers = [1, 2, 3, 4, 5]
numbers.reverse()
print(f"After reverse(): {numbers}")

# ===================================================
# 9. LIST COMPREHENSIONS
# ===================================================

print("\n" + "=" * 60)
print("9. LIST COMPREHENSIONS (Pythonic Way)")
print("=" * 60)

# Basic comprehension
squares = [x**2 for x in range(10)]
print(f"Squares: {squares}")

# With condition
even_squares = [x**2 for x in range(10) if x % 2 == 0]
print(f"Even squares: {even_squares}")

# ML Example: Normalize values to 0-1 range
raw_values = [10, 20, 30, 40, 50]
max_val = max(raw_values)
normalized = [x / max_val for x in raw_values]
print(f"Normalized values: {normalized}")

# String transformations
words = ["machine", "learning", "python"]
uppercase = [word.upper() for word in words]
print(f"Uppercase words: {uppercase}")

# Nested comprehension (create 2D array)
matrix_2d = [[i * j for j in range(3)] for i in range(3)]
print(f"2D Matrix:\n{matrix_2d}")

# ===================================================
# 10. USEFUL LIST OPERATIONS
# ===================================================

print("\n" + "=" * 60)
print("10. USEFUL LIST OPERATIONS")
print("=" * 60)

numbers = [1, 2, 3, 4, 5]

# Length
print(f"Length of list: {len(numbers)}")

# Min, Max, Sum
print(f"Minimum: {min(numbers)}")
print(f"Maximum: {max(numbers)}")
print(f"Sum: {sum(numbers)}")

# Average (mean)
average = sum(numbers) / len(numbers)
print(f"Average: {average}")

# Concatenation
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = list1 + list2
print(f"Concatenated: {combined}")

# Repetition
repeated = [0] * 5
print(f"Repeated: {repeated}")

# Copy a list (important!)
original = [1, 2, 3]
shallow_copy = original.copy()  # or original[:]
print(f"Shallow copy: {shallow_copy}")

# ===================================================
# 11. COMMON ML USE CASES
# ===================================================

print("\n" + "=" * 60)
print("11. MACHINE LEARNING USE CASES")
print("=" * 60)

# Storing training history
training_history = {
    "epochs": [1, 2, 3, 4, 5],
    "loss": [2.5, 1.8, 1.2, 0.9, 0.7],
    "accuracy": [0.65, 0.78, 0.85, 0.90, 0.93]
}
print("Training History:")
for epoch, loss, acc in zip(
    training_history["epochs"],
    training_history["loss"],
    training_history["accuracy"]
):
    print(f"  Epoch {epoch}: Loss={loss:.2f}, Accuracy={acc:.2%}")

# Batch processing
all_samples = list(range(100))  # 100 samples
batch_size = 10
num_batches = len(all_samples) // batch_size

print(f"\nBatch Processing: {len(all_samples)} samples, batch size {batch_size}")
for i in range(num_batches):
    start = i * batch_size
    end = start + batch_size
    batch = all_samples[start:end]
    print(f"  Batch {i + 1}: samples {start} to {end - 1}")

# Feature scaling example
features = [10, 50, 30, 70, 90]
min_val = min(features)
max_val = max(features)
scaled_features = [(x - min_val) / (max_val - min_val) for x in features]
print(f"\nOriginal features: {features}")
print(f"Min-Max scaled (0-1): {[f'{x:.2f}' for x in scaled_features]}")

# ===================================================
# 12. LIST PERFORMANCE TIPS
# ===================================================

print("\n" + "=" * 60)
print("12. PERFORMANCE TIPS")
print("=" * 60)

print("""
✅ FAST Operations:
   - Accessing by index: O(1)
   - Appending: O(1)
   - Popping from end: O(1)
   - Slicing: O(k) where k is slice size

❌ SLOW Operations:
   - Inserting at beginning: O(n)
   - Searching for value: O(n)
   - Removing by value: O(n)

💡 Tips:
   - Use list comprehensions instead of loops (faster)
   - Pre-allocate size if known: [0] * n
   - Use deque from collections for frequent insertions
   - For large datasets, consider NumPy arrays
""")

# ===================================================
# 13. PRACTICE EXERCISES
# ===================================================

print("\n" + "=" * 60)
print("13. QUICK PRACTICE")
print("=" * 60)

# Exercise 1: Filter and transform
temperatures_celsius = [0, 10, 20, 30, 40]
temperatures_fahrenheit = [c * 9/5 + 32 for c in temperatures_celsius]
print(f"Celsius: {temperatures_celsius}")
print(f"Fahrenheit: {temperatures_fahrenheit}")

# Exercise 2: Remove outliers (values > 2 std devs from mean)
import statistics
data = [10, 12, 11, 13, 100, 14, 12, 13, 11]
mean = statistics.mean(data)
std_dev = statistics.stdev(data)
filtered_data = [x for x in data if abs(x - mean) <= 2 * std_dev]
print(f"\nOriginal data: {data}")
print(f"After removing outliers: {filtered_data}")

# Exercise 3: Create pairs (useful for coordinate systems)
x_coords = [1, 2, 3]
y_coords = [4, 5, 6]
coordinates = list(zip(x_coords, y_coords))
print(f"\nCoordinates: {coordinates}")

print("\n" + "=" * 60)
print("END OF LISTS TUTORIAL")
print("=" * 60)
