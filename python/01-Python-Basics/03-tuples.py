# ===================================================
# PROGRAM 1.3: TUPLES - Immutable Data Structures
# ===================================================

"""
TUPLES IN PYTHON
- Ordered collection of items
- Immutable (cannot be changed after creation)
- Allow duplicate elements
- Faster than lists (due to immutability)
- Use less memory than lists
- Used for fixed data that shouldn't change
"""

# ===================================================
# 1. CREATING TUPLES
# ===================================================

print("=" * 60)
print("1. CREATING TUPLES")
print("=" * 60)

# Empty tuple
empty_tuple = ()
print(f"Empty tuple: {empty_tuple}")

# Tuple with parentheses
coordinates = (10, 20)
print(f"Coordinates: {coordinates}")

# Tuple without parentheses (tuple packing)
dimensions = 224, 224, 3
print(f"Dimensions: {dimensions}, Type: {type(dimensions)}")

# Single element tuple (note the comma!)
single = (42,)  # Comma is required!
not_tuple = (42)  # This is just an integer
print(f"Single element tuple: {single}, Type: {type(single)}")
print(f"Not a tuple: {not_tuple}, Type: {type(not_tuple)}")

# Tuple with mixed data types
model_config = ("ResNet50", 50, True, 0.001)
print(f"Model config: {model_config}")

# Nested tuples
rgb_colors = ((255, 0, 0), (0, 255, 0), (0, 0, 255))
print(f"RGB colors: {rgb_colors}")

# Using tuple() constructor
numbers = tuple([1, 2, 3, 4, 5])
print(f"From list: {numbers}")

chars = tuple("hello")
print(f"From string: {chars}")

# ===================================================
# 2. ACCESSING TUPLE ELEMENTS
# ===================================================

print("\n" + "=" * 60)
print("2. ACCESSING TUPLE ELEMENTS")
print("=" * 60)

point = (10, 20, 30)

# Positive indexing
print(f"First element: {point[0]}")
print(f"Second element: {point[1]}")

# Negative indexing
print(f"Last element: {point[-1]}")
print(f"Second last: {point[-2]}")

# Nested tuple access
image_data = ("image.jpg", (1920, 1080), (255, 255, 255))
filename, resolution, bg_color = image_data
print(f"Filename: {filename}")
print(f"Resolution: {resolution}")
print(f"Width: {resolution[0]}, Height: {resolution[1]}")

# ===================================================
# 3. TUPLE SLICING
# ===================================================

print("\n" + "=" * 60)
print("3. TUPLE SLICING [start:end:step]")
print("=" * 60)

numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
print(f"Original tuple: {numbers}")

# Basic slicing
print(f"First 5: {numbers[:5]}")
print(f"Last 5: {numbers[-5:]}")
print(f"Middle elements: {numbers[3:7]}")

# Step slicing
print(f"Every 2nd element: {numbers[::2]}")
print(f"Reverse: {numbers[::-1]}")

# ML Example: RGB to individual channels
rgb_image = (255, 128, 64)
red = rgb_image[0:1]
green = rgb_image[1:2]
blue = rgb_image[2:3]
print(f"RGB: {rgb_image} -> R: {red}, G: {green}, B: {blue}")

# ===================================================
# 4. TUPLE UNPACKING
# ===================================================

print("\n" + "=" * 60)
print("4. TUPLE UNPACKING (Very Powerful!)")
print("=" * 60)

# Basic unpacking
coordinates = (10, 20, 30)
x, y, z = coordinates
print(f"x={x}, y={y}, z={z}")

# Unpacking with * (extended unpacking)
numbers = (1, 2, 3, 4, 5)
first, *middle, last = numbers
print(f"First: {first}")
print(f"Middle: {middle}")  # This becomes a list!
print(f"Last: {last}")

# Swapping variables (elegant use of tuples)
a = 10
b = 20
print(f"Before swap: a={a}, b={b}")
a, b = b, a  # Swap using tuple unpacking
print(f"After swap: a={a}, b={b}")

# Multiple return values from function
def get_model_metrics():
    accuracy = 0.95
    precision = 0.93
    recall = 0.94
    return accuracy, precision, recall  # Returns a tuple

acc, prec, rec = get_model_metrics()
print(f"\nModel Metrics:")
print(f"  Accuracy: {acc}")
print(f"  Precision: {prec}")
print(f"  Recall: {rec}")

# Unpacking in loops
data_points = [(1, 2), (3, 4), (5, 6)]
print("\nIterating with unpacking:")
for x, y in data_points:
    print(f"  Point: x={x}, y={y}")

# ===================================================
# 5. TUPLE METHODS (Limited due to immutability)
# ===================================================

print("\n" + "=" * 60)
print("5. TUPLE METHODS")
print("=" * 60)

predictions = ("cat", "dog", "cat", "bird", "cat", "dog")

# count() - Count occurrences
cat_count = predictions.count("cat")
print(f"Number of 'cat' predictions: {cat_count}")

# index() - Find first occurrence
dog_index = predictions.index("dog")
print(f"First 'dog' at index: {dog_index}")

# in operator - Membership check
print(f"Is 'bird' in predictions? {'bird' in predictions}")
print(f"Is 'fish' in predictions? {'fish' in predictions}")

# ===================================================
# 6. IMMUTABILITY DEMONSTRATION
# ===================================================

print("\n" + "=" * 60)
print("6. IMMUTABILITY (Cannot Change Tuples)")
print("=" * 60)

my_tuple = (1, 2, 3, 4, 5)
print(f"Original tuple: {my_tuple}")

# This will cause an error (uncomment to see):
# my_tuple[0] = 10  # TypeError: 'tuple' object does not support item assignment

print("✗ Cannot modify: my_tuple[0] = 10")
print("✗ Cannot append: my_tuple.append(6)")
print("✗ Cannot remove: my_tuple.remove(3)")

# However, you can create a new tuple
new_tuple = my_tuple + (6, 7)
print(f"✓ Can create new tuple: {new_tuple}")

# Concatenation creates new tuple
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
combined = tuple1 + tuple2
print(f"Combined tuple: {combined}")

# Repetition creates new tuple
repeated = (0,) * 5
print(f"Repeated tuple: {repeated}")

# ===================================================
# 7. TUPLES VS LISTS
# ===================================================

print("\n" + "=" * 60)
print("7. TUPLES VS LISTS - When to Use What?")
print("=" * 60)

print("""
USE TUPLES WHEN:
  ✓ Data should NOT change (image dimensions, RGB values)
  ✓ Need faster performance (tuples are faster)
  ✓ Want to use as dictionary keys (tuples are hashable)
  ✓ Returning multiple values from a function
  ✓ Storing heterogeneous data (different types)

USE LISTS WHEN:
  ✓ Data needs to change (training losses, predictions)
  ✓ Need to add/remove elements frequently
  ✓ All elements are of the same type
  ✓ Order matters and modifications are expected

PERFORMANCE COMPARISON:
""")

import sys

my_list = [1, 2, 3, 4, 5]
my_tuple = (1, 2, 3, 4, 5)

print(f"  List memory: {sys.getsizeof(my_list)} bytes")
print(f"  Tuple memory: {sys.getsizeof(my_tuple)} bytes")
print(f"  Tuple is smaller: {sys.getsizeof(my_list) > sys.getsizeof(my_tuple)}")

# ===================================================
# 8. TUPLES AS DICTIONARY KEYS
# ===================================================

print("\n" + "=" * 60)
print("8. TUPLES AS DICTIONARY KEYS")
print("=" * 60)

# Tuples can be dictionary keys (lists cannot!)
coordinates_values = {
    (0, 0): "origin",
    (1, 0): "right",
    (0, 1): "up",
    (1, 1): "diagonal"
}

print("Coordinate mapping:")
for coord, label in coordinates_values.items():
    print(f"  {coord} -> {label}")

# ML Example: Store results by hyperparameters
experiment_results = {
    ("SGD", 0.01): 0.85,
    ("SGD", 0.001): 0.89,
    ("Adam", 0.01): 0.92,
    ("Adam", 0.001): 0.94
}

print("\nExperiment Results (optimizer, learning_rate): accuracy")
for (optimizer, lr), accuracy in experiment_results.items():
    print(f"  ({optimizer}, {lr}): {accuracy:.2%}")

# ===================================================
# 9. NAMED TUPLES (More Readable)
# ===================================================

print("\n" + "=" * 60)
print("9. NAMED TUPLES (collections.namedtuple)")
print("=" * 60)

from collections import namedtuple

# Create a named tuple class
Point = namedtuple("Point", ["x", "y", "z"])

# Create instances
p1 = Point(10, 20, 30)
p2 = Point(x=5, y=15, z=25)

print(f"Point 1: {p1}")
print(f"Access by name: x={p1.x}, y={p1.y}, z={p1.z}")
print(f"Access by index: {p1[0]}, {p1[1]}, {p1[2]}")

# ML Example: Model Configuration
ModelConfig = namedtuple("ModelConfig", [
    "name", "layers", "learning_rate", "batch_size"
])

config = ModelConfig(
    name="ResNet50",
    layers=50,
    learning_rate=0.001,
    batch_size=32
)

print(f"\nModel Configuration:")
print(f"  Name: {config.name}")
print(f"  Layers: {config.layers}")
print(f"  Learning Rate: {config.learning_rate}")
print(f"  Batch Size: {config.batch_size}")

# Convert to dictionary
config_dict = config._asdict()
print(f"\nAs dictionary: {config_dict}")

# ===================================================
# 10. COMMON ML USE CASES
# ===================================================

print("\n" + "=" * 60)
print("10. MACHINE LEARNING USE CASES")
print("=" * 60)

# 1. Image dimensions (shouldn't change)
IMAGE_SIZE = (224, 224, 3)  # Height, Width, Channels
print(f"Standard image size: {IMAGE_SIZE}")

# 2. RGB color values
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
print(f"Color palette: RED={RED}, GREEN={GREEN}, BLUE={BLUE}")

# 3. Model architecture (fixed configuration)
RESNET_CONFIG = (
    "ResNet50",      # Model name
    50,              # Number of layers
    (224, 224, 3),   # Input shape
    1000             # Output classes
)
print(f"ResNet Config: {RESNET_CONFIG}")

# 4. Bounding box coordinates (x1, y1, x2, y2)
bounding_boxes = [
    (10, 10, 100, 100),   # Box 1
    (150, 50, 250, 150),  # Box 2
    (300, 200, 400, 300)  # Box 3
]
print(f"\nBounding boxes:")
for i, (x1, y1, x2, y2) in enumerate(bounding_boxes, 1):
    print(f"  Box {i}: ({x1}, {y1}) to ({x2}, {y2})")

# 5. Data split ratios
SPLIT_RATIOS = (0.7, 0.15, 0.15)  # Train, Validation, Test
train_ratio, val_ratio, test_ratio = SPLIT_RATIOS
print(f"\nDataset split: Train={train_ratio:.0%}, Val={val_ratio:.0%}, Test={test_ratio:.0%}")

# 6. Coordinate transformations
def transform_point(point, offset):
    """Add offset to a point (returns new tuple)"""
    return tuple(p + o for p, o in zip(point, offset))

original_point = (10, 20, 30)
offset = (5, 5, 5)
new_point = transform_point(original_point, offset)
print(f"\nPoint transformation:")
print(f"  Original: {original_point}")
print(f"  Offset: {offset}")
print(f"  Result: {new_point}")

# ===================================================
# 11. TUPLE OPERATIONS
# ===================================================

print("\n" + "=" * 60)
print("11. USEFUL TUPLE OPERATIONS")
print("=" * 60)

numbers = (3, 1, 4, 1, 5, 9, 2, 6)

# Length
print(f"Length: {len(numbers)}")

# Min, Max, Sum
print(f"Minimum: {min(numbers)}")
print(f"Maximum: {max(numbers)}")
print(f"Sum: {sum(numbers)}")

# Sorting (returns a list)
sorted_numbers = sorted(numbers)
print(f"Sorted (as list): {sorted_numbers}")

# Convert back to tuple if needed
sorted_tuple = tuple(sorted_numbers)
print(f"Sorted (as tuple): {sorted_tuple}")

# Concatenation
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
combined = tuple1 + tuple2
print(f"Concatenation: {tuple1} + {tuple2} = {combined}")

# Repetition
repeated = (0,) * 5
print(f"Repetition: {repeated}")

# Comparison (lexicographic order)
print(f"(1, 2) < (1, 3): {(1, 2) < (1, 3)}")
print(f"(2, 1) > (1, 9): {(2, 1) > (1, 9)}")

# ===================================================
# 12. CONVERTING BETWEEN TUPLES AND LISTS
# ===================================================

print("\n" + "=" * 60)
print("12. CONVERTING BETWEEN TUPLES AND LISTS")
print("=" * 60)

# List to tuple
my_list = [1, 2, 3, 4, 5]
my_tuple = tuple(my_list)
print(f"List to tuple: {my_list} -> {my_tuple}")

# Tuple to list
my_tuple = (10, 20, 30)
my_list = list(my_tuple)
print(f"Tuple to list: {my_tuple} -> {my_list}")

# When you need to modify a tuple
original_tuple = (1, 2, 3, 4, 5)
temp_list = list(original_tuple)
temp_list.append(6)
temp_list[0] = 10
modified_tuple = tuple(temp_list)
print(f"Original tuple: {original_tuple}")
print(f"Modified tuple: {modified_tuple}")

# ===================================================
# 13. PRACTICAL EXAMPLES
# ===================================================

print("\n" + "=" * 60)
print("13. PRACTICAL EXAMPLES")
print("=" * 60)

# Example 1: Function returning multiple values
def calculate_statistics(numbers):
    """Calculate mean, median, and std deviation"""
    mean = sum(numbers) / len(numbers)
    sorted_nums = sorted(numbers)
    median = sorted_nums[len(sorted_nums) // 2]
    variance = sum((x - mean) ** 2 for x in numbers) / len(numbers)
    std_dev = variance ** 0.5
    return mean, median, std_dev  # Returns tuple

data = [10, 20, 30, 40, 50]
mean, median, std = calculate_statistics(data)
print(f"Statistics for {data}:")
print(f"  Mean: {mean:.2f}")
print(f"  Median: {median:.2f}")
print(f"  Std Dev: {std:.2f}")

# Example 2: Enumerate with unpacking
labels = ["cat", "dog", "bird"]
print("\nEnumerate with unpacking:")
for index, label in enumerate(labels):
    print(f"  Index {index}: {label}")

# Example 3: Zip multiple lists
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
scores = [85, 90, 95]

print("\nZipping multiple lists:")
for name, age, score in zip(names, ages, scores):
    print(f"  {name} (age {age}): score {score}")

# Example 4: Dictionary items as tuples
model_params = {"learning_rate": 0.001, "epochs": 100, "batch_size": 32}
print("\nDictionary items (as tuples):")
for key, value in model_params.items():
    print(f"  {key}: {value}")

print("\n" + "=" * 60)
print("END OF TUPLES TUTORIAL")
print("=" * 60)
print("\n💡 Key Takeaway: Use tuples for immutable, fixed data!")
