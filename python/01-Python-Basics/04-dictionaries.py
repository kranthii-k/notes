# ===================================================
# PROGRAM 1.4: DICTIONARIES - Key-Value Storage
# ===================================================

"""
DICTIONARIES IN PYTHON
- Unordered collection of key-value pairs (ordered from Python 3.7+)
- Mutable (can be changed after creation)
- Keys must be unique and immutable (strings, numbers, tuples)
- Values can be any type
- Extremely fast lookups O(1)
- Most versatile data structure for ML configurations
"""

# ===================================================
# 1. CREATING DICTIONARIES
# ===================================================

print("=" * 60)
print("1. CREATING DICTIONARIES")
print("=" * 60)

# Empty dictionary
empty_dict = {}
empty_dict2 = dict()
print(f"Empty dictionary: {empty_dict}")

# Dictionary with string keys
student = {
    "name": "Alice",
    "age": 25,
    "grade": "A",
    "enrolled": True
}
print(f"Student: {student}")

# Dictionary with different key types
mixed_keys = {
    "name": "Model",
    1: "first",
    (0, 0): "origin",
    42: "answer"
}
print(f"Mixed keys: {mixed_keys}")

# ML Example: Model configuration
model_config = {
    "model_name": "ResNet50",
    "layers": 50,
    "input_shape": (224, 224, 3),
    "num_classes": 1000,
    "learning_rate": 0.001,
    "batch_size": 32,
    "epochs": 100,
    "optimizer": "Adam",
    "use_gpu": True
}
print(f"\nModel Configuration:")
for key, value in model_config.items():
    print(f"  {key}: {value}")

# Using dict() constructor
person = dict(name="Bob", age=30, city="NYC")
print(f"\nUsing dict(): {person}")

# From list of tuples
pairs = [("a", 1), ("b", 2), ("c", 3)]
dict_from_pairs = dict(pairs)
print(f"From tuples: {dict_from_pairs}")

# ===================================================
# 2. ACCESSING DICTIONARY VALUES
# ===================================================

print("\n" + "=" * 60)
print("2. ACCESSING DICTIONARY VALUES")
print("=" * 60)

model = {
    "name": "CNN",
    "accuracy": 0.95,
    "layers": 10
}

# Using square brackets (raises KeyError if key doesn't exist)
print(f"Model name: {model['name']}")
print(f"Model accuracy: {model['accuracy']}")

# Using get() method (returns None if key doesn't exist)
print(f"Model layers: {model.get('layers')}")
print(f"Model epochs: {model.get('epochs')}")  # Returns None

# get() with default value
epochs = model.get("epochs", 100)  # Returns 100 if 'epochs' not found
print(f"Epochs (with default): {epochs}")

# Checking if key exists
print(f"'name' in model: {'name' in model}")
print(f"'epochs' in model: {'epochs' in model}")

# ===================================================
# 3. MODIFYING DICTIONARIES
# ===================================================

print("\n" + "=" * 60)
print("3. MODIFYING DICTIONARIES")
print("=" * 60)

config = {"learning_rate": 0.01, "batch_size": 32}
print(f"Original: {config}")

# Update existing value
config["learning_rate"] = 0.001
print(f"After update: {config}")

# Add new key-value pair
config["epochs"] = 100
print(f"After adding: {config}")

# Update multiple values at once
config.update({"batch_size": 64, "optimizer": "Adam"})
print(f"After update(): {config}")

# Remove key-value pair
removed_value = config.pop("optimizer")
print(f"Removed 'optimizer': {removed_value}")
print(f"After pop(): {config}")

# Remove last inserted item (Python 3.7+)
last_key, last_value = config.popitem()
print(f"Popped last item: {last_key}={last_value}")
print(f"After popitem(): {config}")

# Delete with del
config["temp"] = "delete_me"
del config["temp"]
print(f"After del: {config}")

# Clear all items
temp_dict = {"a": 1, "b": 2}
temp_dict.clear()
print(f"After clear(): {temp_dict}")

# ===================================================
# 4. DICTIONARY METHODS
# ===================================================

print("\n" + "=" * 60)
print("4. DICTIONARY METHODS")
print("=" * 60)

data = {
    "model": "LSTM",
    "accuracy": 0.92,
    "loss": 0.15,
    "epochs": 50
}

# keys() - Get all keys
print(f"Keys: {list(data.keys())}")

# values() - Get all values
print(f"Values: {list(data.values())}")

# items() - Get all key-value pairs as tuples
print(f"Items: {list(data.items())}")

# Iterating through dictionary
print("\nIterating through keys:")
for key in data:
    print(f"  {key}: {data[key]}")

print("\nIterating through items:")
for key, value in data.items():
    print(f"  {key} = {value}")

# Copy a dictionary
original = {"a": 1, "b": 2}
shallow_copy = original.copy()
print(f"\nOriginal: {original}")
print(f"Copy: {shallow_copy}")

# setdefault() - Get value or set default if key doesn't exist
metrics = {"accuracy": 0.95}
acc = metrics.setdefault("accuracy", 0.0)  # Key exists, returns 0.95
prec = metrics.setdefault("precision", 0.0)  # Key doesn't exist, sets and returns 0.0
print(f"\nAfter setdefault(): {metrics}")

# ===================================================
# 5. NESTED DICTIONARIES
# ===================================================

print("\n" + "=" * 60)
print("5. NESTED DICTIONARIES")
print("=" * 60)

# ML Training History
training_history = {
    "epoch_1": {
        "train_loss": 2.5,
        "train_acc": 0.65,
        "val_loss": 2.3,
        "val_acc": 0.68
    },
    "epoch_2": {
        "train_loss": 1.8,
        "train_acc": 0.78,
        "val_loss": 1.7,
        "val_acc": 0.80
    },
    "epoch_3": {
        "train_loss": 1.2,
        "train_acc": 0.85,
        "val_loss": 1.1,
        "val_acc": 0.87
    }
}

print("Training History:")
for epoch, metrics in training_history.items():
    print(f"\n{epoch}:")
    for metric, value in metrics.items():
        print(f"  {metric}: {value}")

# Accessing nested values
epoch1_train_loss = training_history["epoch_1"]["train_loss"]
print(f"\nEpoch 1 Training Loss: {epoch1_train_loss}")

# Multi-level nesting
deep_config = {
    "model": {
        "architecture": {
            "type": "CNN",
            "layers": [64, 128, 256, 512],
            "activation": "relu"
        },
        "optimizer": {
            "name": "Adam",
            "learning_rate": 0.001,
            "beta1": 0.9,
            "beta2": 0.999
        }
    }
}

print(f"\nModel type: {deep_config['model']['architecture']['type']}")
print(f"Optimizer: {deep_config['model']['optimizer']['name']}")

# ===================================================
# 6. DICTIONARY COMPREHENSIONS
# ===================================================

print("\n" + "=" * 60)
print("6. DICTIONARY COMPREHENSIONS")
print("=" * 60)

# Basic comprehension
squares = {x: x**2 for x in range(6)}
print(f"Squares: {squares}")

# With condition
even_squares = {x: x**2 for x in range(10) if x % 2 == 0}
print(f"Even squares: {even_squares}")

# From two lists
keys = ["name", "age", "city"]
values = ["Alice", 25, "NYC"]
person = {k: v for k, v in zip(keys, values)}
print(f"Person: {person}")

# Transform dictionary values
prices = {"apple": 1.0, "banana": 0.5, "cherry": 2.0}
discounted = {item: price * 0.9 for item, price in prices.items()}
print(f"Original prices: {prices}")
print(f"Discounted (10% off): {discounted}")

# ML Example: Normalize metrics
raw_metrics = {"accuracy": 95, "precision": 92, "recall": 94}
normalized = {k: v / 100 for k, v in raw_metrics.items()}
print(f"\nRaw metrics: {raw_metrics}")
print(f"Normalized (0-1): {normalized}")

# ===================================================
# 7. MERGING DICTIONARIES
# ===================================================

print("\n" + "=" * 60)
print("7. MERGING DICTIONARIES")
print("=" * 60)

dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

# Using update()
merged = dict1.copy()
merged.update(dict2)
print(f"Using update(): {merged}")

# Using ** unpacking (Python 3.5+)
merged = {**dict1, **dict2}
print(f"Using ** unpacking: {merged}")

# Using | operator (Python 3.9+)
merged = dict1 | dict2
print(f"Using | operator: {merged}")

# When keys overlap, later value wins
config1 = {"lr": 0.01, "epochs": 100}
config2 = {"lr": 0.001, "batch_size": 32}
merged_config = {**config1, **config2}
print(f"\nConfig 1: {config1}")
print(f"Config 2: {config2}")
print(f"Merged (lr updated): {merged_config}")

# ===================================================
# 8. DICTIONARY WITH DEFAULT VALUES
# ===================================================

print("\n" + "=" * 60)
print("8. DICTIONARIES WITH DEFAULT VALUES")
print("=" * 60)

from collections import defaultdict

# Regular dict requires checking
word_count = {}
words = ["cat", "dog", "cat", "bird", "dog", "cat"]

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print(f"Word count (regular dict): {word_count}")

# defaultdict automatically initializes
word_count_auto = defaultdict(int)  # Default value is 0
for word in words:
    word_count_auto[word] += 1  # No need to check!

print(f"Word count (defaultdict): {dict(word_count_auto)}")

# Default list for grouping
from collections import defaultdict

student_courses = defaultdict(list)
student_courses["Alice"].append("Math")
student_courses["Alice"].append("Physics")
student_courses["Bob"].append("Chemistry")

print(f"\nStudent courses: {dict(student_courses)}")

# ===================================================
# 9. ORDERED DICTIONARIES
# ===================================================

print("\n" + "=" * 60)
print("9. ORDERED DICTIONARIES")
print("=" * 60)

# Regular dicts maintain insertion order (Python 3.7+)
config = {}
config["first"] = 1
config["second"] = 2
config["third"] = 3

print(f"Dictionary (maintains order): {config}")

# OrderedDict for explicit ordering
from collections import OrderedDict

ordered = OrderedDict()
ordered["z"] = 26
ordered["a"] = 1
ordered["m"] = 13

print(f"OrderedDict: {ordered}")

# Move to end
ordered.move_to_end("a")
print(f"After move_to_end('a'): {ordered}")

# ===================================================
# 10. COMMON ML USE CASES
# ===================================================

print("\n" + "=" * 60)
print("10. MACHINE LEARNING USE CASES")
print("=" * 60)

# 1. Model Hyperparameters
hyperparameters = {
    "learning_rate": 0.001,
    "batch_size": 32,
    "epochs": 100,
    "dropout_rate": 0.5,
    "optimizer": "Adam",
    "loss_function": "categorical_crossentropy"
}
print("Hyperparameters:")
for param, value in hyperparameters.items():
    print(f"  {param}: {value}")

# 2. Dataset Information
dataset_info = {
    "name": "CIFAR-10",
    "num_classes": 10,
    "train_samples": 50000,
    "test_samples": 10000,
    "image_shape": (32, 32, 3),
    "classes": ["airplane", "automobile", "bird", "cat", "deer",
                "dog", "frog", "horse", "ship", "truck"]
}
print(f"\nDataset: {dataset_info['name']}")
print(f"Classes: {len(dataset_info['classes'])}")
print(f"Training samples: {dataset_info['train_samples']}")

# 3. Model Evaluation Metrics
evaluation = {
    "accuracy": 0.9567,
    "precision": 0.9423,
    "recall": 0.9381,
    "f1_score": 0.9402,
    "confusion_matrix": [[50, 2], [3, 45]]
}
print("\nModel Evaluation:")
for metric, value in evaluation.items():
    if metric != "confusion_matrix":
        print(f"  {metric}: {value:.4f}")

# 4. Class Label Mapping
label_map = {
    0: "cat",
    1: "dog",
    2: "bird",
    3: "fish",
    4: "horse"
}
# Reverse mapping
label_to_id = {v: k for k, v in label_map.items()}
print(f"\nLabel map: {label_map}")
print(f"Reverse map: {label_to_id}")

# 5. Feature Engineering
raw_data = {
    "age": 25,
    "income": 50000,
    "education_years": 16
}

# Normalize features
max_values = {"age": 100, "income": 200000, "education_years": 20}
normalized_data = {
    key: value / max_values[key] 
    for key, value in raw_data.items()
}
print(f"\nRaw data: {raw_data}")
print(f"Normalized: {normalized_data}")

# 6. Training Configuration
train_config = {
    "data": {
        "train_path": "./data/train",
        "val_path": "./data/val",
        "test_path": "./data/test",
        "augmentation": True
    },
    "model": {
        "name": "ResNet50",
        "pretrained": True,
        "freeze_layers": 40
    },
    "training": {
        "epochs": 100,
        "batch_size": 32,
        "learning_rate": 0.001,
        "early_stopping": True,
        "patience": 10
    }
}

print("\nTraining Configuration:")
for section, params in train_config.items():
    print(f"{section}:")
    for key, value in params.items():
        print(f"  {key}: {value}")

# ===================================================
# 11. COUNTER - COUNTING WITH DICTIONARIES
# ===================================================

print("\n" + "=" * 60)
print("11. COUNTER - COUNTING MADE EASY")
print("=" * 60)

from collections import Counter

# Count predictions
predictions = ["cat", "dog", "cat", "bird", "cat", "dog", "bird", "cat"]
pred_counts = Counter(predictions)
print(f"Prediction counts: {pred_counts}")

# Most common
print(f"Most common (top 2): {pred_counts.most_common(2)}")

# Count characters
text = "machine learning"
char_counts = Counter(text)
print(f"\nCharacter counts: {char_counts}")

# Counter arithmetic
counter1 = Counter(["a", "b", "c", "a"])
counter2 = Counter(["a", "b", "d"])
print(f"\nCounter 1: {counter1}")
print(f"Counter 2: {counter2}")
print(f"Combined: {counter1 + counter2}")
print(f"Difference: {counter1 - counter2}")

# ===================================================
# 12. DICTIONARY OPERATIONS & TRICKS
# ===================================================

print("\n" + "=" * 60)
print("12. USEFUL OPERATIONS & TRICKS")
print("=" * 60)

# Get dictionary length
config = {"a": 1, "b": 2, "c": 3}
print(f"Dictionary length: {len(config)}")

# Check if empty
empty = {}
print(f"Is empty dict falsy? {not empty}")
print(f"Is non-empty dict truthy? {bool(config)}")

# Dictionary from keys with same value
keys = ["accuracy", "precision", "recall"]
metrics = dict.fromkeys(keys, 0.0)
print(f"\nDict from keys: {metrics}")

# Swap keys and values
original = {"a": 1, "b": 2, "c": 3}
swapped = {v: k for k, v in original.items()}
print(f"Original: {original}")
print(f"Swapped: {swapped}")

# Filter dictionary
scores = {"Alice": 85, "Bob": 92, "Charlie": 78, "David": 95}
high_scorers = {name: score for name, score in scores.items() if score >= 90}
print(f"\nAll scores: {scores}")
print(f"High scorers (>=90): {high_scorers}")

# Sort dictionary by keys
unsorted = {"z": 1, "a": 2, "m": 3}
sorted_by_key = dict(sorted(unsorted.items()))
print(f"\nUnsorted: {unsorted}")
print(f"Sorted by key: {sorted_by_key}")

# Sort by values
sorted_by_value = dict(sorted(scores.items(), key=lambda x: x[1], reverse=True))
print(f"Scores sorted by value (descending): {sorted_by_value}")

# ===================================================
# 13. PRACTICAL EXAMPLES
# ===================================================

print("\n" + "=" * 60)
print("13. PRACTICAL EXAMPLES")
print("=" * 60)

# Example 1: Calculate accuracy per class
predictions_per_class = {
    "cat": {"correct": 45, "total": 50},
    "dog": {"correct": 48, "total": 50},
    "bird": {"correct": 42, "total": 50}
}

print("Accuracy per class:")
for class_name, stats in predictions_per_class.items():
    accuracy = stats["correct"] / stats["total"]
    print(f"  {class_name}: {accuracy:.2%} ({stats['correct']}/{stats['total']})")

# Example 2: Group data by category
data = [
    {"name": "Alice", "department": "ML", "score": 95},
    {"name": "Bob", "department": "DL", "score": 88},
    {"name": "Charlie", "department": "ML", "score": 92},
    {"name": "David", "department": "DL", "score": 90}
]

grouped = defaultdict(list)
for person in data:
    grouped[person["department"]].append(person)

print("\nGrouped by department:")
for dept, people in grouped.items():
    print(f"{dept}: {[p['name'] for p in people]}")

# Example 3: Configuration validation
required_keys = {"model_name", "learning_rate", "epochs"}
user_config = {"model_name": "CNN", "learning_rate": 0.001}

missing_keys = required_keys - user_config.keys()
if missing_keys:
    print(f"\n⚠ Missing configuration keys: {missing_keys}")
else:
    print("\n✓ Configuration complete!")

print("\n" + "=" * 60)
print("END OF DICTIONARIES TUTORIAL")
print("=" * 60)
print("\n💡 Key Takeaway: Use dictionaries for key-value mappings!")
print("   Perfect for configs, metrics, and structured data!")
