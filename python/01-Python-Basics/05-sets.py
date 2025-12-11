# ===================================================
# PROGRAM 1.5: SETS - Unique Collections
# ===================================================

"""
SETS IN PYTHON
- Unordered collection of unique elements
- Mutable (can add/remove elements)
- No duplicate values allowed
- Elements must be immutable (strings, numbers, tuples)
- Very fast membership testing O(1)
- Useful for mathematical set operations
- Perfect for finding unique values, removing duplicates
"""

# ===================================================
# 1. CREATING SETS
# ===================================================

print("=" * 60)
print("1. CREATING SETS")
print("=" * 60)

# Empty set (must use set(), not {})
empty_set = set()
print(f"Empty set: {empty_set}, Type: {type(empty_set)}")

# Note: {} creates an empty dictionary, not a set!
empty_dict = {}
print(f"Empty dict: {empty_dict}, Type: {type(empty_dict)}")

# Set with curly braces
fruits = {"apple", "banana", "cherry"}
print(f"Fruits set: {fruits}")

# Set with duplicates (automatically removed)
numbers = {1, 2, 3, 2, 1, 4, 3, 5}
print(f"Numbers (duplicates removed): {numbers}")

# Set from list
list_data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
unique_numbers = set(list_data)
print(f"From list: {list_data}")
print(f"Unique values: {unique_numbers}")

# Set from string
text = "hello"
char_set = set(text)
print(f"Characters in '{text}': {char_set}")

# ML Example: Unique class labels
predictions = ["cat", "dog", "cat", "bird", "dog", "cat", "fish"]
unique_classes = set(predictions)
print(f"\nPredictions: {predictions}")
print(f"Unique classes: {unique_classes}")
print(f"Number of unique classes: {len(unique_classes)}")

# ===================================================
# 2. ADDING AND REMOVING ELEMENTS
# ===================================================

print("\n" + "=" * 60)
print("2. ADDING AND REMOVING ELEMENTS")
print("=" * 60)

# add() - Add single element
tags = {"python", "machine-learning"}
print(f"Original tags: {tags}")
tags.add("deep-learning")
print(f"After add('deep-learning'): {tags}")

# Adding duplicate (no effect)
tags.add("python")
print(f"After add('python') again: {tags}")

# update() - Add multiple elements
tags.update(["ai", "neural-networks"])
print(f"After update(['ai', 'neural-networks']): {tags}")

# remove() - Remove element (raises KeyError if not found)
tags.remove("ai")
print(f"After remove('ai'): {tags}")

# discard() - Remove element (no error if not found)
tags.discard("nonexistent")  # No error
print(f"After discard('nonexistent'): {tags}")

# pop() - Remove and return arbitrary element
removed = tags.pop()
print(f"Popped element: {removed}")
print(f"After pop(): {tags}")

# clear() - Remove all elements
temp_set = {1, 2, 3}
temp_set.clear()
print(f"After clear(): {temp_set}")

# ===================================================
# 3. SET OPERATIONS - MATHEMATICAL OPERATIONS
# ===================================================

print("\n" + "=" * 60)
print("3. SET OPERATIONS (The Power of Sets!)")
print("=" * 60)

# Sample sets
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

print(f"Set A: {set_a}")
print(f"Set B: {set_b}")

# UNION - All unique elements from both sets
union1 = set_a | set_b
union2 = set_a.union(set_b)
print(f"\nUnion (A | B): {union1}")
print(f"Union (A.union(B)): {union2}")

# INTERSECTION - Common elements in both sets
intersection1 = set_a & set_b
intersection2 = set_a.intersection(set_b)
print(f"\nIntersection (A & B): {intersection1}")
print(f"Intersection (A.intersection(B)): {intersection2}")

# DIFFERENCE - Elements in A but not in B
difference1 = set_a - set_b
difference2 = set_a.difference(set_b)
print(f"\nDifference (A - B): {difference1}")
print(f"Difference (A.difference(B)): {difference2}")
print(f"Difference (B - A): {set_b - set_a}")

# SYMMETRIC DIFFERENCE - Elements in either A or B but not both
sym_diff1 = set_a ^ set_b
sym_diff2 = set_a.symmetric_difference(set_b)
print(f"\nSymmetric Difference (A ^ B): {sym_diff1}")
print(f"Symmetric Difference (A.symmetric_difference(B)): {sym_diff2}")

# ===================================================
# 4. SET COMPARISON OPERATIONS
# ===================================================

print("\n" + "=" * 60)
print("4. SET COMPARISON OPERATIONS")
print("=" * 60)

set1 = {1, 2, 3}
set2 = {1, 2, 3, 4, 5}
set3 = {1, 2, 3}
set4 = {4, 5, 6}

# Subset - All elements of A are in B
print(f"Set1: {set1}")
print(f"Set2: {set2}")
print(f"Is set1 subset of set2? {set1.issubset(set2)}")
print(f"Is set1 <= set2? {set1 <= set2}")

# Superset - All elements of B are in A
print(f"\nIs set2 superset of set1? {set2.issuperset(set1)}")
print(f"Is set2 >= set1? {set2 >= set1}")

# Disjoint - No common elements
print(f"\nSet1: {set1}, Set4: {set4}")
print(f"Are set1 and set4 disjoint? {set1.isdisjoint(set4)}")

# Equality
print(f"\nSet1: {set1}, Set3: {set3}")
print(f"Are set1 and set3 equal? {set1 == set3}")

# ===================================================
# 5. SET MEMBERSHIP TESTING
# ===================================================

print("\n" + "=" * 60)
print("5. MEMBERSHIP TESTING (Very Fast!)")
print("=" * 60)

valid_labels = {"cat", "dog", "bird", "fish", "horse"}

# Check membership - O(1) average time complexity
print(f"Valid labels: {valid_labels}")
print(f"Is 'cat' valid? {'cat' in valid_labels}")
print(f"Is 'elephant' valid? {'elephant' in valid_labels}")
print(f"Is 'dog' NOT valid? {'dog' not in valid_labels}")

# Performance comparison: list vs set
print("\n💡 Performance: Sets are much faster for membership testing!")
print("   List: O(n) - checks each element")
print("   Set: O(1) - direct lookup")

# ===================================================
# 6. SET COMPREHENSIONS
# ===================================================

print("\n" + "=" * 60)
print("6. SET COMPREHENSIONS")
print("=" * 60)

# Basic comprehension
squares = {x**2 for x in range(10)}
print(f"Squares: {squares}")

# With condition
even_squares = {x**2 for x in range(10) if x % 2 == 0}
print(f"Even squares: {even_squares}")

# From string (unique characters)
text = "machine learning"
unique_chars = {char for char in text if char != ' '}
print(f"Unique characters in '{text}': {unique_chars}")

# ML Example: Extract unique file extensions
files = ["model.py", "data.csv", "test.py", "config.json", "utils.py"]
extensions = {file.split('.')[-1] for file in files}
print(f"\nFiles: {files}")
print(f"Unique extensions: {extensions}")

# ===================================================
# 7. FROZENSETS (Immutable Sets)
# ===================================================

print("\n" + "=" * 60)
print("7. FROZENSETS - Immutable Sets")
print("=" * 60)

# Frozenset - immutable version of set
frozen = frozenset([1, 2, 3, 4, 5])
print(f"Frozenset: {frozen}")

# Can't modify frozenset
# frozen.add(6)  # AttributeError: 'frozenset' object has no attribute 'add'

# Can use frozensets as dictionary keys or set elements
set_of_sets = {
    frozenset([1, 2, 3]),
    frozenset([4, 5, 6]),
    frozenset([7, 8, 9])
}
print(f"Set of frozensets: {set_of_sets}")

# Dictionary with frozenset keys
config_results = {
    frozenset(["SGD", "0.01"]): 0.85,
    frozenset(["Adam", "0.001"]): 0.92
}
print(f"Config results: {config_results}")

# ===================================================
# 8. COMMON ML USE CASES
# ===================================================

print("\n" + "=" * 60)
print("8. MACHINE LEARNING USE CASES")
print("=" * 60)

# 1. Find unique values in dataset
print("Use Case 1: Finding Unique Values")
predictions = ["cat", "dog", "cat", "bird", "dog", "cat", "fish", "bird"]
unique_predictions = set(predictions)
print(f"Predictions: {predictions}")
print(f"Unique classes: {unique_predictions}")
print(f"Number of unique classes: {len(unique_predictions)}")

# 2. Remove duplicate samples
print("\nUse Case 2: Removing Duplicates")
sample_ids = [101, 102, 103, 102, 104, 101, 105, 103]
unique_ids = list(set(sample_ids))
print(f"Original IDs: {sample_ids}")
print(f"Unique IDs: {unique_ids}")

# 3. Find common features between models
print("\nUse Case 3: Finding Common Features")
model1_features = {"age", "income", "education", "occupation"}
model2_features = {"age", "income", "location", "credit_score"}
common_features = model1_features & model2_features
print(f"Model 1 features: {model1_features}")
print(f"Model 2 features: {model2_features}")
print(f"Common features: {common_features}")

# 4. Find missing labels
print("\nUse Case 4: Finding Missing Labels")
expected_labels = {"cat", "dog", "bird", "fish", "horse"}
predicted_labels = {"cat", "dog", "bird"}
missing_labels = expected_labels - predicted_labels
print(f"Expected: {expected_labels}")
print(f"Predicted: {predicted_labels}")
print(f"Missing: {missing_labels}")

# 5. Validate data consistency
print("\nUse Case 5: Data Validation")
train_classes = {"class_A", "class_B", "class_C"}
test_classes = {"class_A", "class_B", "class_D"}

# Find classes in test but not in train (potential issue!)
unknown_classes = test_classes - train_classes
if unknown_classes:
    print(f"⚠ WARNING: Unknown classes in test set: {unknown_classes}")

# Find classes in train but not in test
unused_classes = train_classes - test_classes
if unused_classes:
    print(f"ℹ INFO: Classes not in test set: {unused_classes}")

# 6. Feature selection - Union of important features
print("\nUse Case 6: Feature Selection")
features_model1 = {"age", "income", "education"}
features_model2 = {"income", "credit_score", "location"}
features_model3 = {"age", "income", "employment_years"}

# Union: All features used by any model
all_features = features_model1 | features_model2 | features_model3
print(f"All features across models: {all_features}")

# Intersection: Core features used by all models
core_features = features_model1 & features_model2 & features_model3
print(f"Core features (used by all): {core_features}")

# 7. Track processed samples
print("\nUse Case 7: Tracking Processed Samples")
all_samples = {f"sample_{i}" for i in range(1, 11)}
processed_samples = set()

# Simulate processing
for sample in ["sample_1", "sample_3", "sample_5"]:
    processed_samples.add(sample)
    print(f"Processing: {sample}")

remaining = all_samples - processed_samples
print(f"Remaining to process: {remaining}")
print(f"Progress: {len(processed_samples)}/{len(all_samples)}")

# ===================================================
# 9. SET OPERATIONS WITH MULTIPLE SETS
# ===================================================

print("\n" + "=" * 60)
print("9. OPERATIONS WITH MULTIPLE SETS")
print("=" * 60)

# Union of multiple sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set3 = {5, 6, 7}

union_all = set1 | set2 | set3
print(f"Union of all: {union_all}")

# Intersection of multiple sets
set_a = {1, 2, 3, 4, 5}
set_b = {2, 3, 4, 5, 6}
set_c = {3, 4, 5, 6, 7}

intersection_all = set_a & set_b & set_c
print(f"Intersection of all: {intersection_all}")

# Chain operations
result = (set1 | set2) - set3
print(f"(set1 | set2) - set3: {result}")

# ===================================================
# 10. PRACTICAL EXAMPLES
# ===================================================

print("\n" + "=" * 60)
print("10. PRACTICAL EXAMPLES")
print("=" * 60)

# Example 1: Find duplicate values in list
print("Example 1: Find Duplicates")
data = [1, 2, 3, 2, 4, 5, 3, 6, 4]
seen = set()
duplicates = set()

for item in data:
    if item in seen:
        duplicates.add(item)
    else:
        seen.add(item)

print(f"Data: {data}")
print(f"Duplicates: {duplicates}")

# Example 2: Find unique words in text
print("\nExample 2: Unique Words")
text = "machine learning is fun and machine learning is powerful"
words = text.lower().split()
unique_words = set(words)
print(f"Text: {text}")
print(f"Unique words: {unique_words}")
print(f"Total words: {len(words)}, Unique: {len(unique_words)}")

# Example 3: Compare two models' predictions
print("\nExample 3: Compare Model Predictions")
model1_correct = {1, 2, 3, 5, 7, 8, 10}
model2_correct = {1, 2, 4, 5, 6, 9, 10}

both_correct = model1_correct & model2_correct
only_model1 = model1_correct - model2_correct
only_model2 = model2_correct - model1_correct

print(f"Both models correct: {both_correct}")
print(f"Only model 1 correct: {only_model1}")
print(f"Only model 2 correct: {only_model2}")

# Example 4: Filter valid samples
print("\nExample 4: Filter Valid Samples")
all_samples = {f"sample_{i}" for i in range(1, 21)}
corrupted = {"sample_3", "sample_7", "sample_15"}
missing_labels = {"sample_4", "sample_12"}

invalid = corrupted | missing_labels
valid_samples = all_samples - invalid

print(f"Total samples: {len(all_samples)}")
print(f"Invalid samples: {len(invalid)}")
print(f"Valid samples: {len(valid_samples)}")

# Example 5: Tag-based filtering
print("\nExample 5: Tag-based Filtering")
image_tags = {
    "img1": {"outdoor", "sunny", "landscape"},
    "img2": {"indoor", "portrait", "studio"},
    "img3": {"outdoor", "cloudy", "landscape"},
    "img4": {"outdoor", "sunny", "portrait"}
}

# Find images with specific tags
required_tags = {"outdoor", "sunny"}
matching_images = []

for img, tags in image_tags.items():
    if required_tags.issubset(tags):
        matching_images.append(img)

print(f"Required tags: {required_tags}")
print(f"Matching images: {matching_images}")

# ===================================================
# 11. PERFORMANCE TIPS
# ===================================================

print("\n" + "=" * 60)
print("11. PERFORMANCE TIPS")
print("=" * 60)

print("""
✅ FAST Operations (O(1) average):
   - Membership testing: x in set
   - Adding element: set.add(x)
   - Removing element: set.remove(x)
   - Set operations: union, intersection, difference

❌ NOT IDEAL for:
   - Accessing elements by index (sets are unordered)
   - Maintaining insertion order (use list or OrderedDict)
   - Storing duplicate values (use list)
   - Storing mutable objects (use list)

💡 When to Use Sets:
   ✓ Need unique values only
   ✓ Frequent membership testing
   ✓ Mathematical set operations
   ✓ Removing duplicates from lists
   ✓ Finding common/different elements

💡 When NOT to Use Sets:
   ✗ Need to maintain order
   ✗ Need to access by index
   ✗ Need to store duplicates
   ✗ Need mutable elements
""")

# ===================================================
# 12. CONVERTING BETWEEN DATA STRUCTURES
# ===================================================

print("\n" + "=" * 60)
print("12. CONVERTING BETWEEN DATA STRUCTURES")
print("=" * 60)

# List to Set (remove duplicates)
my_list = [1, 2, 2, 3, 3, 3, 4, 4, 5]
my_set = set(my_list)
print(f"List to Set: {my_list} -> {my_set}")

# Set to List (if you need indexing)
back_to_list = list(my_set)
print(f"Set to List: {my_set} -> {back_to_list}")

# Tuple to Set
my_tuple = (1, 2, 2, 3, 3)
tuple_set = set(my_tuple)
print(f"Tuple to Set: {my_tuple} -> {tuple_set}")

# Set from dictionary keys
my_dict = {"a": 1, "b": 2, "c": 3}
key_set = set(my_dict.keys())
print(f"Dict keys to Set: {key_set}")

# String to Set (unique characters)
text = "hello world"
char_set = set(text)
print(f"String to Set: '{text}' -> {char_set}")

print("\n" + "=" * 60)
print("END OF SETS TUTORIAL")
print("=" * 60)
print("\n💡 Key Takeaway: Use sets for unique values and fast lookups!")
print("   Perfect for removing duplicates and set operations!")
