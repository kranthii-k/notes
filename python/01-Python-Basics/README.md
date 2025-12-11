# Section 1: Python Basics for ML

This section covers fundamental Python concepts essential for Machine Learning and Data Science. Each file contains comprehensive examples, practical use cases, and hands-on exercises to help you master Python fundamentals.

## 📚 Contents

> **Note**: Each file contains 10-16 detailed sections with runnable code examples!

### 1.1 Variables & Data Types (`01-variables-datatypes.py`)
- Integer, Float, String, Boolean, None types
- Type checking and conversion
- ML-specific use cases for each type
- Variable naming conventions
- **Key Topics**: Data type selection, type casting, ML configuration examples

### 1.2 Lists (`02-lists.py`) - 13 Sections
- Creating and accessing lists (indexing, slicing)
- List methods (append, extend, insert, remove, pop, sort, reverse)
- List comprehensions for efficient code
- Nested lists and multi-dimensional arrays
- Batch processing and data manipulation
- **Key Topics**: Dynamic arrays, mutable sequences, ML batch operations

### 1.3 Tuples (`03-tuples.py`) - 13 Sections
- Creating and accessing tuples
- Immutability concept and benefits
- Tuple unpacking and multiple return values
- Named tuples for readable code
- **Key Topics**: Fixed data structures, function returns, RGB values, coordinates

### 1.4 Dictionaries (`04-dictionaries.py`) - 13 Sections
- Creating and accessing dictionaries
- Dictionary methods (keys, values, items, get, update, pop)
- Nested dictionaries and complex structures
- Dictionary comprehensions
- Counter and defaultdict
- **Key Topics**: Key-value pairs, hyperparameters, model configurations, metrics

### 1.5 Sets (`05-sets.py`) - 12 Sections
- Creating sets and understanding uniqueness
- Set operations (union, intersection, difference, symmetric difference)
- Set methods (add, remove, discard, clear)
- Frozensets for immutable sets
- **Key Topics**: Unique values, fast membership testing, data validation

### 1.6 Strings (`06-strings.py`) - 16 Sections
- String creation and formatting (f-strings, format(), %)
- String methods (split, join, replace, strip, upper, lower)
- String slicing and indexing
- Regular expressions basics
- Text preprocessing for NLP
- **Key Topics**: Text manipulation, data cleaning, file paths, NLP preprocessing

## 🎯 Learning Objectives

After completing this section, you will be able to:
- ✅ Work with all basic Python data types
- ✅ Choose the appropriate data structure for different tasks
- ✅ Manipulate and transform data efficiently
- ✅ Apply these concepts to ML/Data Science problems

## 💡 Tips for Learning

1. **Run each file**: Execute each `.py` file to see the outputs
   ```bash
   python 01-variables-datatypes.py
   python 02-lists.py
   # ... and so on
   ```

2. **Experiment**: Modify the examples and observe the results
   - Change values and see what happens
   - Try breaking the code to understand error messages
   - Combine concepts from different files

3. **Practice**: Try solving small problems with each data structure
   - Create your own examples
   - Solve the exercises at the end of each file
   - Apply concepts to real datasets

4. **ML Context**: Pay attention to ML-specific use cases in comments
   - Training loops and batch processing
   - Data preprocessing and cleaning
   - Model configuration and hyperparameters
   - Feature engineering examples

5. **Take Notes**: Document your learnings
   - Add your own comments to the code
   - Create a cheat sheet of commonly used methods
   - Keep track of "aha!" moments

## 📖 Prerequisites

- Basic understanding of programming concepts
- Python 3.7+ installed
- A code editor or IDE (VS Code recommended)

## 🚀 Next Steps

After mastering these basics, you'll move to:
- **02-Control-Flow**: if/else statements, for/while loops, break/continue
- **03-Functions**: Function definition, parameters, return values, lambda functions
- **04-OOP**: Classes, objects, inheritance, encapsulation
- **05-NumPy**: Arrays, vectorization, mathematical operations
- **06-Pandas**: DataFrames, data analysis, manipulation

## 📊 What You'll Learn

By completing this section, you'll understand:
- ✅ **Lists**: Perfect for sequences, training data, predictions
- ✅ **Tuples**: Ideal for fixed configurations, coordinates, RGB values
- ✅ **Dictionaries**: Best for configurations, hyperparameters, metrics
- ✅ **Sets**: Great for unique values, validation, filtering
- ✅ **Strings**: Essential for text processing, file handling, NLP

## 🎓 Quick Reference

| Data Structure | Mutable | Ordered | Duplicates | Use Case |
|---------------|---------|---------|------------|----------|
| List | ✅ Yes | ✅ Yes | ✅ Yes | Training data, sequences |
| Tuple | ❌ No | ✅ Yes | ✅ Yes | Fixed configs, coordinates |
| Dictionary | ✅ Yes | ✅ Yes* | Keys: No, Values: Yes | Hyperparameters, metrics |
| Set | ✅ Yes | ❌ No | ❌ No | Unique labels, validation |
| String | ❌ No | ✅ Yes | ✅ Yes | Text data, file paths |

*Ordered since Python 3.7+

## 📝 Practice Exercises

Each file contains practical examples, but here are some additional challenges:

1. **Lists**: Create a function to split a dataset into train/validation/test sets
2. **Tuples**: Build a function that returns multiple model metrics
3. **Dictionaries**: Design a configuration system for ML experiments
4. **Sets**: Implement a data validation system to check for missing labels
5. **Strings**: Write a text preprocessing pipeline for NLP tasks

## 🔗 Additional Resources

- [Python Official Documentation](https://docs.python.org/3/)
- [Real Python Tutorials](https://realpython.com/)
- [Python for Data Science Handbook](https://jakevdp.github.io/PythonDataScienceHandbook/)

---

**Happy Learning! 🚀** Start with `01-variables-datatypes.py` and work your way through!