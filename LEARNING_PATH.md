# Learning Path & Progression Guide

This document outlines the recommended order for exploring this portfolio and how concepts build upon each other.

## Complete Learning Progression

### Foundation: Python Fundamentals (Weeks 1-3)

Start here to build core language skills:

```
01_python/
├── fundamentals/          Print, variables, types, basic operations
├── control_flow/          if/else, for loops, while loops, pattern exercises  
├── data_structures/       Lists, tuples, dictionaries, sets
├── functions/             Function definition, parameters, return values
├── oop/                   Classes, methods, object basics
├── files_and_databases/   File I/O, SQLite basics
└── projects/              Small applications integrating these concepts
```

**Key Skills After This Section:**
- ✅ Python syntax and core language features
- ✅ Problem-solving with loops and conditionals
- ✅ Working with data structures
- ✅ Writing reusable functions
- ✅ Object-oriented design basics
- ✅ File and database operations

**Before Moving Forward:**
Ensure you understand:
- How loops work (for, while)
- How to create and call functions
- The difference between lists, dicts, and sets
- How to create a simple class

---

### Layer 1: Algorithms & Data Structures (Weeks 4-8)

Now apply Python to solve algorithmic problems:

```
02_algorithms/
├── number_theory/         Prime numbers, factorials
├── searching/             Linear search, binary search (supplementary)
├── sorting/               Bubble, merge, quick sort (supplementary)
├── recursion/             Recursive thinking (supplementary)
├── data_structures/       Stacks, queues, linked lists (supplementary)
├── graphs/                DFS, BFS, pathfinding (supplementary)
└── complexity/            Big-O analysis (supplementary)
```

**Why algorithms matter:**
- Foundation for ALL software engineering interviews
- Required for machine learning optimization
- Teaches computational thinking
- Improves code efficiency

**Key Skills:**
- ✅ Understand algorithm complexity (Big-O)
- ✅ Implement and debug recursive solutions
- ✅ Know when to use different data structures
- ✅ Optimize code for performance

---

### Layer 2: Data Analysis (Weeks 9-12)

Now work with real data:

```
03_data_analysis/
├── numpy/                 Array operations, vectorization
├── pandas/                Data loading, cleaning, transformation
├── visualization/         Matplotlib plotting and analysis
└── notebooks/             Exploratory data analysis workflows
```

**What You Learn:**
- ✅ Load and explore datasets
- ✅ Clean messy data
- ✅ Find patterns and relationships
- ✅ Create meaningful visualizations
- ✅ Prepare data for machine learning

**Real-World Application:**
Data scientists spend 70% of time on data cleaning and exploration. This section teaches that practical skill.

---

### Layer 3: Machine Learning (Weeks 13-18)

Apply ML algorithms to solve real problems:

```
04_machine_learning/
├── fundamentals/          Intro to ML, basic workflows
├── regression/            Predicting continuous values
├── classification/        Predicting categories
├── clustering/            Unsupervised learning, grouping
├── recommender_systems/   Building recommendation engines
└── projects/              End-to-end ML projects
```

**Key Concepts:**
- ✅ Supervised vs. unsupervised learning
- ✅ Train/test split and cross-validation
- ✅ Feature engineering and preprocessing
- ✅ Model evaluation and selection
- ✅ Hyperparameter tuning

**Career Relevance:**
Machine learning is applied in almost every tech company. This section gives you practical skills.

---

### Layer 4: Computer Vision (Weeks 19+)

Specialized domain for image analysis:

```
05_computer_vision/
├── image_processing/      Basic image operations
├── notebooks/             Vision algorithms and techniques
├── work_in_progress/      Advanced techniques
└── assets/                Sample images for learning
```

**Topics Covered:**
- ✅ Image fundamentals and color spaces
- ✅ Filtering and morphological operations
- ✅ Edge detection and feature extraction
- ✅ Object detection basics

**When to Focus on This:**
- After completing ML fundamentals
- If interested in robotics, autonomous vehicles, medical imaging
- For specialized roles in computer vision

---

## Recommended Study Schedule

### For Full-Time Learning (3-4 months)

```
Months 1-2:   Python fundamentals (01_python/)
Month 2-3:    Algorithms (02_algorithms/)
Month 3-4:    Data analysis (03_data_analysis/)
Month 4-5:    Machine learning (04_machine_learning/)
Month 5+:     Computer vision (05_computer_vision/) OR
              Deep learning, advanced topics
```

### For Part-Time Learning (6-9 months)

```
Months 1-3:   Python fundamentals
Months 2-4:   Algorithms (overlapping)
Months 4-6:   Data analysis
Months 6-8:   Machine learning
Months 8-9:   Computer vision / Specialization
```

### For Job Interview Prep

Priority order for tech interviews:

1. **Python fundamentals** (01_python/) - ~1 week review
2. **Algorithms & Data Structures** (02_algorithms/) - ~2-3 weeks
3. **Coding practice** - LeetCode, HackerRank
4. **System design** - If applying for senior roles

---

## Concept Dependencies Map

```
┌─────────────────────────────────────────────┐
│ Python Fundamentals (01_python)            │
│ - Syntax, control flow, data structures    │
│ - Functions, OOP, file I/O                 │
└──────────────┬──────────────────────────────┘
               │
        ┌──────▼──────┐
        │              │
    ┌───▼────────┐  ┌─▼───────────────┐
    │ Algorithms │  │ Data Analysis   │
    │(02)        │  │ (03)            │
    └───┬────────┘  └─┬───────────────┘
        │              │
        └──────┬───────┘
               │
        ┌──────▼────────────────┐
        │ Machine Learning      │
        │ (04)                  │
        │ - Regression          │
        │ - Classification      │
        │ - Clustering          │
        └──────┬───────────────┘
               │
        ┌──────▼────────────────┐
        │ Computer Vision       │
        │ (05)                  │
        │ (Optional)            │
        └───────────────────────┘
```

---

## Key Milestones

| Milestone | What You Should Know | Approx. Time |
|-----------|----------------------|--------------|
| Python Basics | Run scripts, understand data types, loops | Week 1-2 |
| Problem Solving | Write functions, solve basic problems | Week 3-4 |
| Algorithms | Understand complexity, implement sorting | Week 8 |
| Data Skills | Load CSV, clean data, create plots | Week 12 |
| ML Workflow | Train model, split data, evaluate | Week 16 |
| Real Project | Build end-to-end solution | Week 20 |

---

## When You're Ready to Specialize

### If interested in Data Science
- Focus: 03_data_analysis, 04_machine_learning
- Add: Statistics, SQL, Tableau/PowerBI
- Build: Kaggle competitions

### If interested in ML Engineering
- Focus: 04_machine_learning fundamentals
- Add: Deep learning (TensorFlow/PyTorch)
- Build: Real-world ML systems, deployment

### If interested in Computer Vision
- Focus: 05_computer_vision, deep learning
- Add: Advanced CV techniques, YOLO, segmentation
- Build: Vision projects (object detection, etc.)

### If interested in Software Engineering
- Focus: 01_python, 02_algorithms
- Add: System design, architecture patterns, testing
- Build: Large-scale applications

---

## How to Use This Guide

1. **First time here?** Start at "Python Fundamentals"
2. **Review mode?** Jump to your current level
3. **Job prep?** Focus on algorithms and Python
4. **Building portfolio?** Complete at least one project per section

---

## Progress Tracking

Use this checklist to track your progress:

### Python Fundamentals
- [ ] Understand print, variables, and data types
- [ ] Write loops and conditionals
- [ ] Create and call functions
- [ ] Work with lists, dicts, and sets
- [ ] Create and use classes
- [ ] Read and write files
- [ ] Complete a small project

### Algorithms
- [ ] Understand Big-O complexity
- [ ] Implement sorting algorithms
- [ ] Implement searching algorithms
- [ ] Understand recursion
- [ ] Work with trees and graphs (basics)
- [ ] Solve dynamic programming problems

### Data Analysis
- [ ] Create and manipulate NumPy arrays
- [ ] Load and clean data with pandas
- [ ] Create meaningful visualizations
- [ ] Perform exploratory data analysis
- [ ] Handle missing values and outliers

### Machine Learning
- [ ] Understand train/test split
- [ ] Build regression models
- [ ] Build classification models
- [ ] Evaluate models properly
- [ ] Complete an end-to-end project

### Computer Vision (optional)
- [ ] Understand image representation
- [ ] Apply filters to images
- [ ] Detect edges and features
- [ ] Implement object detection (basic)

---

## Supplementary Materials

This repository also includes `supplementary/` folder with additional learning materials for topics not covered in the original coursework:

- Advanced Python techniques
- Additional algorithms
- Best practices
- Real-world examples

See SKILLS.md for details on what's covered and what's supplementary.
