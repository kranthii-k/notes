# ===================================================
# PROGRAM 1.1: Understanding Data Types in ML
# ===================================================

# This program shows how different data types are used in ML

# INTEGER EXAMPLES (whole numbers)
# Used for:  counts, sizes, discrete values
number_of_images = 1000          # How many training images
batch_size = 32                   # How many samples per batch
number_of_epochs = 100            # How many times to train
number_of_classes = 10            # How many categories (e.g., digits 0-9)

# FLOAT EXAMPLES (decimal numbers)
# Used for: measurements, probabilities, rates
learning_rate = 0.001             # How fast the model learns
model_accuracy = 0.9567           # Model performance (95. 67%)
training_loss = 2.345             # Error value
confidence_score = 0.87           # How confident is the prediction (87%)

# STRING EXAMPLES (text)
# Used for: names, paths, labels
model_name = "ResNet50"           # Name of the model architecture
dataset_path = "data/images/"     # Where the data is stored
predicted_class = "cat"           # What the model predicted

# BOOLEAN EXAMPLES (True/False)
# Used for: conditions, flags, switches
is_training = True                # Are we in training mode?
use_gpu = True                    # Should we use GPU?
model_converged = False           # Has training finished?

# NONE EXAMPLE (absence of value)
# Used for: uninitialized values
best_model_weights = None         # We don't have best weights yet
early_stopping_patience = None    # Not set yet

# PRINTING WITH FORMATTING
print("=" * 50)
print("MACHINE LEARNING CONFIGURATION")
print("=" * 50)
print(f"Model Name: {model_name}")
print(f"Training Samples: {number_of_images}")
print(f"Batch Size: {batch_size}")
print(f"Epochs: {number_of_epochs}")
print(f"Learning Rate: {learning_rate}")
print(f"Current Accuracy: {model_accuracy * 100:.2f}%")  # Convert to percentage
print(f"Using GPU: {use_gpu}")
print(f"Training Mode: {is_training}")

# CHECKING TYPES
print("\n" + "=" * 50)
print("CHECKING DATA TYPES")
print("=" * 50)
print(f"Type of number_of_images: {type(number_of_images)}")      # <class 'int'>
print(f"Type of learning_rate: {type(learning_rate)}")            # <class 'float'>
print(f"Type of model_name: {type(model_name)}")                  # <class 'str'>
print(f"Type of use_gpu: {type(use_gpu)}")                        # <class 'bool'>
print(f"Type of best_model_weights: {type(best_model_weights)}")  # <class 'NoneType'>