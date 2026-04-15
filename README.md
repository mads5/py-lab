# 🐍 py-lab: Master Python from Basics to Advanced

A structured repository for mastering Python fundamentals, problem-solving, and interview preparation.

> **Your complete learning companion** - From Python basics to advanced algorithms, data structures, and professional testing practices.

---

## 📑 Table of Contents

- [Overview](#overview)
- [Learning Paths](#learning-paths)
- [Getting Started](#getting-started)
- [How to Use](#how-to-use)
- [Features](#features)
- [Contributing](#contributing)
- [License](#license)

---

## 🎯 Overview

**py-lab** is a comprehensive Python learning repository designed for:
- 👨‍💻 Beginners starting their Python journey
- 🎓 Students preparing for coding interviews
- 📊 Data science enthusiasts learning data manipulation
- 🧪 Developers mastering testing practices
- 🚀 Professionals seeking to deepen their Python expertise

This repository contains **100% Python** content organized into progressive learning modules, covering everything from basic syntax to advanced algorithms and real-world applications.

---

## 🛣️ Learning Paths

Choose the path that best matches your goals:

### **Path 1: Complete Beginner → Advanced (8-12 weeks)**
*Perfect for: Complete beginners wanting comprehensive Python mastery*

| Week | Focus Area | Modules |
|------|-----------|---------|
| 1-2 | Python Fundamentals | Learning basics: Levels 1-2 |
| 3-4 | Control & Functions | Learning basics: Levels 2-3 |
| 5-6 | OOP & Advanced Concepts | Learning basics: Levels 4-5 |
| 7-8 | Functional Programming | Learning basics: Levels 6-7 |
| 9-10 | Data Structures | Data Structures Algorithms |
| 11-12 | Data Science Intro | Numpy + Pandas basics |

**Milestone:** Build a project combining all concepts learned

---

### **Path 2: Interview Preparation (4-8 weeks)**
*Perfect for: Job seekers preparing for coding interviews*

| Week | Focus Area | Modules |
|------|-----------|---------|
| 1-2 | Core Concepts | Learning basics: Levels 1-4 |
| 2-3 | Problem Solving | Data Structures Algorithms |
| 3-4 | Advanced Patterns | Learning basics: Levels 6-7 |
| 4 | Testing & Quality | pytest folder |

**Milestone:** Solve LeetCode/HackerRank problems using learned concepts

---

### **Path 3: Data Science Focus (6-10 weeks)**
*Perfect for: Data enthusiasts and aspiring data scientists*

| Week | Focus Area | Modules |
|------|-----------|---------|
| 1-2 | Python Basics | Learning basics: Levels 1-3 |
| 3-4 | Advanced Python | Learning basics: Levels 4-5 |
| 5-6 | NumPy Fundamentals | Numpy folder |
| 7-9 | Pandas Mastery | Pandas folder |
| 10 | Data Analysis Project | Combine Numpy + Pandas |

**Milestone:** Complete a data analysis project

---

## 🚀 Getting Started

### **Prerequisites**
- ✅ Python 3.8 or higher installed
- ✅ A code editor (VS Code, PyCharm, Sublime Text, etc.)
- ✅ Basic computer literacy
- ✅ 30 minutes to set up (one time only)

### **Installation Steps**

#### 1. Clone the Repository
```bash
git clone https://github.com/saurangi-1/py-lab.git
cd py-lab
```
#### 2. Create a Virtual Environment
```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

#### 3. Install Dependencies
``` bash
pip install numpy pandas pytest
```

#### 4. Verify Installation
``` bash
python --version
pip list
```

#### 5. Run Your First Script
```bash
cd "Learning basics"
python 1BasicSyntax.py
```

# 📚 Folder Descriptions & 💡 How to Use Guide

---

## 📚 Folder Descriptions

### **1. 📚 Learning basics/** - Foundation & Core Concepts

**Purpose:** Master Python from ground zero

**What You'll Learn:**
- Python syntax and data types
- Control flow and functions
- Object-Oriented Programming (OOP)
- Decorators and advanced patterns
- File I/O and data manipulation
- Regular expressions

**Best For:**
- Complete beginners
- Students needing comprehensive Python foundation
- Interview preparation

**Time to Complete:** 8-12 weeks

**Key Files:**
- Start with: `1BasicSyntax.py` → `1DataTypes.py`
- Progress through levels 2-7 sequentially
- Each file builds on previous concepts


**Learning Sequence:**
1. **Start Here:** `1BasicSyntax.py` & `1DataTypes.py`
2. **Move to:** Levels 2-3 for control structures
3. **Advance to:** Levels 4-5 for OOP and advanced data handling
4. **Master:** Levels 6-7 for functional programming and patterns

**Example Topics by Level:**
- **Level 1:** print(), variables, int/float/str, lists, dictionaries
- **Level 2:** if statements, for/while loops, function definition
- **Level 3:** nested loops, enumerate, logging module
- **Level 4:** class definition, inheritance, exception handling
- **Level 5:** [x for x in list], generators, file operations
- **Level 6:** @decorator, lambda, regular expressions
- **Level 7:** @classmethod, map/filter/reduce, scope rules

**Common Interview Questions Covered:**
- Difference between `==` and `is`
- Mutable vs immutable objects
- `*args` and `**kwargs`
- Generator vs list comprehension
- Decorator implementation
- Copy vs deep copy

---

### **2. 🔢 Data Structures Algorithms/** - Essential Algorithms & DSA

**Purpose:** Master algorithmic thinking and common data structures

**What You'll Learn:**
- Binary search and binary search trees
- Sorting algorithms (QuickSort, Counting Sort)
- Queue and linked list implementations
- Tree traversal and operations
- Algorithm complexity analysis
- Problem-solving strategies

**Best For:**
- Interview preparation
- Competitive programming
- Understanding algorithmic efficiency

**Time to Complete:** 4-6 weeks (after fundamentals)


**Key Concepts:**

| File | Topic | Complexity | Use Cases |
|------|-------|-----------|-----------|
| BinarySearch.py | Searching | O(log n) | Finding elements in sorted data |
| BinarySearchTree.py | Balanced Search | O(log n) avg | Sorted data with frequent access |
| CountingSort.py | Sorting | O(n+k) | Small range integers |
| Queue.py | FIFO Structure | O(1) | Job queues, BFS |
| QuickSort.py | Sorting | O(n log n) avg | General purpose sorting |
| SinglyLinkedList.py | Linked List | O(n) | Dynamic size, frequent insertions |
| Trees.py | Tree Traversal | O(n) | Hierarchical data, graphs |

**Algorithm Complexity Guide:**
- **Best Case:** Fastest possible scenario
- **Average Case:** Typical performance
- **Worst Case:** Slowest possible scenario
- **Space:** Extra memory needed

**Common Interview Problems:**
- Search in rotated sorted array
- Validate binary search tree
- Merge intervals
- Reverse linked list
- Inorder/preorder/postorder traversal
- Top K frequent elements

---

### **3. 📊 Numpy/** - Numerical Computing

**Purpose:** Master numerical operations and scientific computing

**What You'll Learn:**
- NumPy array creation and manipulation
- Mathematical operations
- Linear algebra basics
- Array reshaping and indexing
- File I/O with binary formats
- Performance optimization

**Best For:**
- Data science beginners
- Scientific computing enthusiasts
- Machine learning preparation

**Time to Complete:** 2-3 weeks (can learn in parallel)

**Key Topics Covered:**

| Topic | What You Learn |
|-------|----------------|
| **Array Creation** | np.array(), np.zeros(), np.ones(), np.linspace(), np.arange() |
| **Indexing** | Single/multiple indexing, slicing, fancy indexing |
| **Operations** | Element-wise operations, broadcasting |
| **Linear Algebra** | Dot product, matrix multiplication, transpose |
| **Mathematical Functions** | sum(), mean(), std(), min(), max() |
| **Shape Manipulation** | reshape(), flatten(), transpose() |
| **File I/O** | np.save(), np.load() for .npy files |
| **Performance** | Vectorization vs loops, memory efficiency |

**Common NumPy Operations:**
```python
# Array creation
arr = np.array([1, 2, 3])
zeros = np.zeros((3, 3))
ones = np.ones(5)

# Indexing & slicing
arr[0]              # First element
arr[1:3]            # Slice
arr[::2]            # Every second element

# Operations
arr + 5             # Broadcasting
arr.sum()           # Aggregation
np.dot(arr1, arr2)  # Matrix multiplication

# Shape operations
arr.reshape(3, 1)   # Reshape
arr.T               # Transpose
```

### 4. 🐼 Pandas/ - Data Manipulation & Analysis

**Purpose:** Learn data manipulation and analysis tools

**What You'll Learn:**
- DataFrame and Series concepts
- Data loading and saving
- Data cleaning and preprocessing
- Data transformation and reshaping
- Exploratory data analysis
- Aggregation and grouping

**Best For:**
- Data analysts and scientists
- Business intelligence professionals
- Anyone working with tabular data

**Time to Complete:** 3-4 weeks (after NumPy)

### 5. 🧪 pytest/ - Testing & Quality Assurance

**Purpose:** Write professional, testable Python code

**What You'll Learn:**
- Unit testing fundamentals
- pytest framework and fixtures
- Test organization and configuration
- Mocking and test isolation
- Continuous integration ready tests
- Best practices in testing

**Best For:**
- Professional developers
- Code quality enthusiasts
- Anyone building production code

**Time to Complete:** 2-3 weeks (can learn anytime)

# ⭐ Features

✅ **Well-Organized** - Logically structured learning progression

The repository is organized into clear, sequential modules that build upon each other. Each folder represents a specific topic or skill level, making it easy to navigate and follow a structured learning path. The progression from basics to advanced concepts ensures you don't miss any foundational knowledge.

✅ **Comprehensive** - Covers basics to advanced Python concepts

From fundamental syntax and data types to advanced decorators, generators, and algorithms, this repository covers the entire Python learning spectrum. Whether you're starting from scratch or looking to deepen your expertise, you'll find content that matches your level.

**Topics Covered:**
- Python Fundamentals (Levels 1-3)
- Object-Oriented Programming (Level 4)
- Advanced Python Techniques (Levels 5-7)
- Data Structures and Algorithms
- Scientific Computing (NumPy)
- Data Analysis (Pandas)
- Testing and Quality Assurance (pytest)

✅ **Practical Examples** - Real-world use cases in every module

Every concept is accompanied by practical, working code examples that demonstrate real-world applications. Rather than just theoretical explanations, you'll see how concepts are actually used in practice.

**Example:**
```python
# Real-world example of decorators
@timing_decorator
def process_large_dataset():
    # Process millions of records
    pass

# Decorator logs execution time
def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Execution time: {end - start} seconds")
        return result
    return wrapper
```

# 🤝 Contributing

We welcome contributions from the community! py-lab is built by and for learners like you. Your contributions help make this resource better for everyone.

## Ways You Can Help

### 1. Found a Bug?

If you discover an error in the code or documentation:

**How to Report:**
1. Check if the issue already exists
2. Open a new GitHub issue with:
   - Clear title describing the bug
   - Step-by-step reproduction instructions
   - Expected vs actual behavior
   - Your Python version and OS
   - Code snippet (if applicable)


### 2. Have an Idea?

Got a suggestion for improvement or new content?

**How to Suggest:**
1. Check GitHub discussions first
2. Start a discussion or open an issue with:
   - Clear description of your idea
   - Why it would be valuable
   - How it fits with existing content
   - Example use case (if applicable)

# 📝 License

py-lab is licensed under the MIT License, one of the most permissive and widely-used open-source licenses.

Copyright (c) 2026 py-lab Contributors
