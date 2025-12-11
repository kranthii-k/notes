# ===================================================
# PROGRAM 1.6: STRINGS - Text Manipulation
# ===================================================

"""
STRINGS IN PYTHON
- Sequence of characters enclosed in quotes
- Immutable (cannot be changed in place)
- Can use single (''), double (""), or triple quotes (''' or """)
- Support indexing and slicing
- Extensive built-in methods for text processing
- Essential for NLP, data cleaning, file handling
"""

# ===================================================
# 1. CREATING STRINGS
# ===================================================

print("=" * 60)
print("1. CREATING STRINGS")
print("=" * 60)

# Single quotes
text1 = 'Hello World'
print(f"Single quotes: {text1}")

# Double quotes
text2 = "Python Programming"
print(f"Double quotes: {text2}")

# Triple quotes (multi-line strings)
text3 = """This is a
multi-line
string"""
print(f"Triple quotes:\n{text3}")

# Triple quotes for docstrings
def example_function():
    """
    This is a docstring.
    Used to document functions.
    """
    pass

# Escape characters
escaped = "Line 1\nLine 2\tTabbed\n\"Quoted\""
print(f"\nEscaped characters:\n{escaped}")

# Raw strings (ignore escape characters)
raw_string = r"C:\Users\name\folder"
print(f"\nRaw string: {raw_string}")

# String with quotes inside
quote1 = "He said, 'Hello!'"
quote2 = 'She replied, "Hi!"'
print(f"{quote1}")
print(f"{quote2}")

# ===================================================
# 2. STRING INDEXING AND SLICING
# ===================================================

print("\n" + "=" * 60)
print("2. STRING INDEXING AND SLICING")
print("=" * 60)

text = "Python"
print(f"Text: {text}")

# Positive indexing
print(f"First character: {text[0]}")
print(f"Third character: {text[2]}")

# Negative indexing
print(f"Last character: {text[-1]}")
print(f"Second last: {text[-2]}")

# Slicing [start:end:step]
sentence = "Machine Learning is Amazing"
print(f"\nSentence: {sentence}")
print(f"First 7 chars: {sentence[:7]}")
print(f"Last 7 chars: {sentence[-7:]}")
print(f"Characters 8-16: {sentence[8:16]}")
print(f"Every 2nd character: {sentence[::2]}")
print(f"Reverse string: {sentence[::-1]}")

# ===================================================
# 3. STRING CONCATENATION AND REPETITION
# ===================================================

print("\n" + "=" * 60)
print("3. CONCATENATION AND REPETITION")
print("=" * 60)

# Concatenation with +
first = "Machine"
second = "Learning"
combined = first + " " + second
print(f"Concatenation: {combined}")

# Repetition with *
separator = "-" * 40
print(f"Repetition: {separator}")

# Join multiple strings
words = ["Deep", "Learning", "AI"]
sentence = " ".join(words)
print(f"Joined: {sentence}")

# ===================================================
# 4. STRING METHODS - CASE CONVERSION
# ===================================================

print("\n" + "=" * 60)
print("4. CASE CONVERSION METHODS")
print("=" * 60)

text = "Machine Learning"
print(f"Original: {text}")

# Case conversion
print(f"upper(): {text.upper()}")
print(f"lower(): {text.lower()}")
print(f"title(): {text.title()}")
print(f"capitalize(): {text.capitalize()}")
print(f"swapcase(): {text.swapcase()}")

# Case checking
print(f"\nisupper(): {text.isupper()}")
print(f"islower(): {text.islower()}")
print(f"istitle(): {text.istitle()}")

# ML Example: Normalize labels
labels = ["Cat", "DOG", "BiRd", "FISH"]
normalized = [label.lower() for label in labels]
print(f"\nOriginal labels: {labels}")
print(f"Normalized: {normalized}")

# ===================================================
# 5. STRING METHODS - SEARCHING
# ===================================================

print("\n" + "=" * 60)
print("5. SEARCHING IN STRINGS")
print("=" * 60)

text = "Python is great and Python is powerful"
print(f"Text: {text}")

# Find substring
print(f"\nfind('Python'): {text.find('Python')}")  # Returns first index
print(f"find('Python', 10): {text.find('Python', 10)}")  # Start from index 10
print(f"find('Java'): {text.find('Java')}")  # Returns -1 if not found

# Index (like find but raises error if not found)
print(f"\nindex('Python'): {text.index('Python')}")

# Count occurrences
print(f"\ncount('Python'): {text.count('Python')}")
print(f"count('is'): {text.count('is')}")

# Check if substring exists
print(f"\n'Python' in text: {'Python' in text}")
print(f"'Java' in text: {'Java' in text}")

# Start and end checking
filename = "model_weights.h5"
print(f"\nFilename: {filename}")
print(f"startswith('model'): {filename.startswith('model')}")
print(f"endswith('.h5'): {filename.endswith('.h5')}")

# ===================================================
# 6. STRING METHODS - SPLITTING AND JOINING
# ===================================================

print("\n" + "=" * 60)
print("6. SPLITTING AND JOINING")
print("=" * 60)

# split() - Split string into list
sentence = "Machine Learning is fun"
words = sentence.split()  # Split by whitespace
print(f"Sentence: {sentence}")
print(f"Words: {words}")

# Split by specific delimiter
csv_data = "name,age,score"
fields = csv_data.split(',')
print(f"\nCSV: {csv_data}")
print(f"Fields: {fields}")

# Split with limit
text = "a-b-c-d-e"
parts = text.split('-', 2)  # Split at most 2 times
print(f"\nText: {text}")
print(f"Split (maxsplit=2): {parts}")

# rsplit() - Split from right
path = "folder/subfolder/file.txt"
parts = path.rsplit('/', 1)  # Split from right, once
print(f"\nPath: {path}")
print(f"rsplit('/', 1): {parts}")

# splitlines() - Split by line breaks
multiline = "Line 1\nLine 2\nLine 3"
lines = multiline.splitlines()
print(f"\nMultiline text lines: {lines}")

# join() - Join list into string
words = ["Deep", "Learning"]
sentence = " ".join(words)
print(f"\nWords: {words}")
print(f"Joined: {sentence}")

# Join with different separator
csv_line = ",".join(["Alice", "25", "95"])
print(f"CSV line: {csv_line}")

# ===================================================
# 7. STRING METHODS - TRIMMING
# ===================================================

print("\n" + "=" * 60)
print("7. TRIMMING WHITESPACE")
print("=" * 60)

# strip() - Remove leading and trailing whitespace
text = "   Hello World   "
print(f"Original: '{text}'")
print(f"strip(): '{text.strip()}'")
print(f"lstrip(): '{text.lstrip()}'")  # Left strip
print(f"rstrip(): '{text.rstrip()}'")  # Right strip

# Strip specific characters
text = "###Hello###"
print(f"\nOriginal: '{text}'")
print(f"strip('#'): '{text.strip('#')}'")

# ML Example: Clean user input
user_inputs = ["  cat  ", " dog\n", "\tbird  "]
cleaned = [inp.strip() for inp in user_inputs]
print(f"\nUser inputs: {user_inputs}")
print(f"Cleaned: {cleaned}")

# ===================================================
# 8. STRING METHODS - REPLACING
# ===================================================

print("\n" + "=" * 60)
print("8. REPLACING SUBSTRINGS")
print("=" * 60)

text = "I love Java and Java is great"
print(f"Original: {text}")

# replace() - Replace all occurrences
new_text = text.replace("Java", "Python")
print(f"replace('Java', 'Python'): {new_text}")

# Replace with count limit
new_text = text.replace("Java", "Python", 1)  # Replace only first
print(f"replace('Java', 'Python', 1): {new_text}")

# ML Example: Clean text data
dirty_text = "User@123 said: This is great!!!"
clean_text = dirty_text.replace("@", "").replace("!", "").replace(":", "")
print(f"\nDirty: {dirty_text}")
print(f"Clean: {clean_text}")

# ===================================================
# 9. STRING FORMATTING
# ===================================================

print("\n" + "=" * 60)
print("9. STRING FORMATTING")
print("=" * 60)

# Old style (% formatting)
name = "Alice"
age = 25
print("Old style: %s is %d years old" % (name, age))

# str.format() method
print("\nformat(): {} is {} years old".format(name, age))
print("format() with index: {1} is {0} years old".format(age, name))
print("format() with names: {n} is {a} years old".format(n=name, a=age))

# f-strings (Python 3.6+) - BEST METHOD!
print(f"\nf-string: {name} is {age} years old")

# f-strings with expressions
x = 10
y = 20
print(f"f-string with math: {x} + {y} = {x + y}")

# f-strings with formatting
pi = 3.14159265359
print(f"Pi to 2 decimals: {pi:.2f}")
print(f"Pi to 4 decimals: {pi:.4f}")

# ML Example: Training progress
epoch = 5
loss = 0.234567
accuracy = 0.9543
print(f"\nEpoch {epoch:03d}: Loss={loss:.4f}, Accuracy={accuracy:.2%}")

# Number formatting
value = 1234567.89
print(f"\nWith commas: {value:,.2f}")
print(f"With underscores: {value:_.2f}")
print(f"Scientific: {value:.2e}")

# Alignment and padding
name = "Model"
print(f"\nLeft aligned: '{name:<20}'")
print(f"Right aligned: '{name:>20}'")
print(f"Center aligned: '{name:^20}'")

# ===================================================
# 10. STRING VALIDATION METHODS
# ===================================================

print("\n" + "=" * 60)
print("10. STRING VALIDATION METHODS")
print("=" * 60)

# Type checking
print("Type Checking:")
print(f"'123'.isdigit(): {'123'.isdigit()}")
print(f"'abc'.isalpha(): {'abc'.isalpha()}")
print(f"'abc123'.isalnum(): {'abc123'.isalnum()}")
print(f"'   '.isspace(): {'   '.isspace()}")

# Case checking
print(f"\n'HELLO'.isupper(): {'HELLO'.isupper()}")
print(f"'hello'.islower(): {'hello'.islower()}")
print(f"'Hello World'.istitle(): {'Hello World'.istitle()}")

# Identifier checking
print(f"\n'variable_name'.isidentifier(): {'variable_name'.isidentifier()}")
print(f"'123abc'.isidentifier(): {'123abc'.isidentifier()}")

# ML Example: Validate file extensions
filenames = ["data.csv", "model.h5", "image.jpg", "readme.txt"]
print("\nValidating file extensions:")
for filename in filenames:
    if filename.endswith(('.csv', '.h5')):
        print(f"  ✓ {filename} - Valid data file")
    else:
        print(f"  ✗ {filename} - Not a data file")

# ===================================================
# 11. WORKING WITH SUBSTRINGS
# ===================================================

print("\n" + "=" * 60)
print("11. WORKING WITH SUBSTRINGS")
print("=" * 60)

# Extract file name and extension
filepath = "models/trained/resnet50_weights.h5"
print(f"Filepath: {filepath}")

# Get filename
filename = filepath.split('/')[-1]
print(f"Filename: {filename}")

# Get extension
name, extension = filename.rsplit('.', 1)
print(f"Name: {name}, Extension: {extension}")

# Extract using slicing
url = "https://example.com/data/file.csv"
protocol = url[:url.index("://")]
domain = url[url.index("://") + 3:url.index("/", 8)]
print(f"\nURL: {url}")
print(f"Protocol: {protocol}")
print(f"Domain: {domain}")

# ===================================================
# 12. STRING IMMUTABILITY
# ===================================================

print("\n" + "=" * 60)
print("12. STRING IMMUTABILITY")
print("=" * 60)

text = "Hello"
print(f"Original: {text}")

# Cannot modify string in place
# text[0] = 'h'  # TypeError: 'str' object does not support item assignment

# Must create new string
new_text = 'h' + text[1:]
print(f"Modified (new string): {new_text}")

# Use list for character manipulation if needed
char_list = list(text)
char_list[0] = 'h'
modified = ''.join(char_list)
print(f"Using list: {modified}")

# ===================================================
# 13. COMMON ML/NLP USE CASES
# ===================================================

print("\n" + "=" * 60)
print("13. MACHINE LEARNING / NLP USE CASES")
print("=" * 60)

# 1. Text Preprocessing for NLP
print("Use Case 1: Text Preprocessing")
text = "  Machine Learning is AMAZING!!! Visit https://example.com  "
print(f"Original: '{text}'")

# Clean and normalize
cleaned = text.strip().lower()
cleaned = cleaned.replace("!", "").replace("https://example.com", "")
words = cleaned.split()
print(f"Cleaned words: {words}")

# 2. Remove punctuation
print("\nUse Case 2: Remove Punctuation")
import string
text_with_punct = "Hello, World! How are you?"
translator = str.maketrans('', '', string.punctuation)
no_punct = text_with_punct.translate(translator)
print(f"Original: {text_with_punct}")
print(f"No punctuation: {no_punct}")

# 3. Tokenization (basic)
print("\nUse Case 3: Basic Tokenization")
sentence = "Natural Language Processing is fascinating"
tokens = sentence.lower().split()
print(f"Sentence: {sentence}")
print(f"Tokens: {tokens}")

# 4. Stop word removal (simplified example)
print("\nUse Case 4: Stop Word Removal")
stop_words = {"is", "the", "a", "an", "and", "or", "but"}
sentence = "This is a sample sentence for NLP"
words = sentence.lower().split()
filtered = [word for word in words if word not in stop_words]
print(f"Original: {sentence}")
print(f"Filtered: {filtered}")

# 5. File path manipulation
print("\nUse Case 5: File Path Manipulation")
paths = [
    "data/train/images/img001.jpg",
    "data/train/images/img002.jpg",
    "data/test/images/img003.jpg"
]
print("Extracting image IDs:")
for path in paths:
    img_id = path.split('/')[-1].replace('.jpg', '')
    print(f"  {path} -> {img_id}")

# 6. Create file names
print("\nUse Case 6: Generate File Names")
model_name = "ResNet50"
epoch = 42
accuracy = 0.9567
filename = f"{model_name}_epoch{epoch:03d}_acc{accuracy:.4f}.h5"
print(f"Generated filename: {filename}")

# 7. Parse configuration strings
print("\nUse Case 7: Parse Configuration")
config_str = "lr=0.001,batch=32,epochs=100"
config_dict = {}
for pair in config_str.split(','):
    key, value = pair.split('=')
    config_dict[key] = value
print(f"Config string: {config_str}")
print(f"Parsed config: {config_dict}")

# 8. Text similarity (simple character-based)
print("\nUse Case 8: Simple Text Similarity")
text1 = "machine learning"
text2 = "machine learning is fun"
common_chars = set(text1) & set(text2)
similarity = len(common_chars) / len(set(text1 + text2))
print(f"Text 1: {text1}")
print(f"Text 2: {text2}")
print(f"Character-based similarity: {similarity:.2%}")

# ===================================================
# 14. REGULAR EXPRESSIONS (REGEX) BASICS
# ===================================================

print("\n" + "=" * 60)
print("14. REGULAR EXPRESSIONS BASICS")
print("=" * 60)

import re

# Find pattern
text = "My email is user@example.com and phone is 123-456-7890"
print(f"Text: {text}")

# Find email
email = re.search(r'\S+@\S+', text)
if email:
    print(f"Email found: {email.group()}")

# Find phone
phone = re.search(r'\d{3}-\d{3}-\d{4}', text)
if phone:
    print(f"Phone found: {phone.group()}")

# Find all numbers
numbers = re.findall(r'\d+', "I have 10 apples and 20 oranges")
print(f"\nNumbers found: {numbers}")

# Replace pattern
text = "Visit website1.com or website2.com"
cleaned = re.sub(r'website\d+\.com', '[WEBSITE]', text)
print(f"\nOriginal: {text}")
print(f"Cleaned: {cleaned}")

# Split by pattern
text = "apple,banana;cherry:date"
fruits = re.split(r'[,;:]', text)
print(f"\nText: {text}")
print(f"Split by multiple delimiters: {fruits}")

# ===================================================
# 15. STRING PERFORMANCE TIPS
# ===================================================

print("\n" + "=" * 60)
print("15. PERFORMANCE TIPS")
print("=" * 60)

print("""
✅ EFFICIENT String Operations:
   - Use f-strings for formatting (fastest)
   - Use str.join() for concatenating many strings
   - Use ''.join(list) instead of += in loops
   - Use str.replace() for simple substitutions

❌ AVOID:
   - Using + in loops for concatenation (slow)
   - Multiple replace() calls (use regex or dict)
   - Converting large strings unnecessarily

💡 Best Practices:
   ✓ Pre-compile regex patterns if using multiple times
   ✓ Use string methods instead of regex when possible
   ✓ Use list comprehensions for string transformations
   ✓ Cache commonly used string results
""")

# Example: Efficient string building
# SLOW (don't do this with many strings)
# result = ""
# for i in range(1000):
#     result += str(i) + ","

# FAST (do this instead)
result = ",".join(str(i) for i in range(10))
print(f"\nEfficient join: {result}")

# ===================================================
# 16. PRACTICAL EXAMPLES
# ===================================================

print("\n" + "=" * 60)
print("16. PRACTICAL EXAMPLES")
print("=" * 60)

# Example 1: Parse CSV line
print("Example 1: Parse CSV")
csv_line = "Alice,25,Engineer,95000"
name, age, job, salary = csv_line.split(',')
print(f"Name: {name}, Age: {age}, Job: {job}, Salary: ${salary}")

# Example 2: Create progress bar
print("\nExample 2: Progress Bar")
def progress_bar(progress, total, length=40):
    percent = progress / total
    filled = int(length * percent)
    bar = '█' * filled + '-' * (length - filled)
    return f"[{bar}] {percent:.1%}"

for i in range(0, 101, 20):
    print(progress_bar(i, 100))

# Example 3: Validate and extract data
print("\nExample 3: Validate Model Name")
model_files = [
    "resnet50_v1.h5",
    "vgg16_final.h5",
    "mobilenet.txt",
    "lstm_model_v2.h5"
]

valid_models = []
for filename in model_files:
    if filename.endswith('.h5'):
        model_name = filename.replace('.h5', '')
        valid_models.append(model_name)
        print(f"  ✓ Valid: {model_name}")
    else:
        print(f"  ✗ Invalid: {filename}")

# Example 4: Create formatted table
print("\nExample 4: Formatted Table")
data = [
    ("Model", "Accuracy", "Loss"),
    ("ResNet", 0.95, 0.15),
    ("VGG", 0.92, 0.18),
    ("MobileNet", 0.89, 0.22)
]

for row in data:
    if isinstance(row[1], str):  # Header
        print(f"{row[0]:<15} {row[1]:<15} {row[2]:<10}")
    else:  # Data
        print(f"{row[0]:<15} {row[1]:<15.2%} {row[2]:<10.4f}")

print("\n" + "=" * 60)
print("END OF STRINGS TUTORIAL")
print("=" * 60)
print("\n💡 Key Takeaway: Master string manipulation for data cleaning!")
print("   Essential for NLP, file handling, and data preprocessing!")
