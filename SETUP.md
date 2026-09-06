# Setup & Installation Guide

This repository contains Python learning materials and projects. Follow these steps to set up your environment.

## Prerequisites

- Python 3.9+ (check with `python --version`)
- pip package manager
- Git

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/programming-learning-portfolio.git
cd programming-learning-portfolio
```

### 2. Create a Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate it
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

## Folder Structure

```
01_python/              Core Python concepts and exercises
02_algorithms/          Algorithm implementations and analysis
03_data_analysis/       NumPy, pandas, and data visualization
04_machine_learning/    ML models and machine learning concepts
05_computer_vision/     Image processing and computer vision
supplementary/          Additional learning materials
```

## Running the Code

### Python Scripts

```bash
python 01_python/fundamentals/intro_print_statements.py
```

### Jupyter Notebooks

```bash
jupyter notebook
# Then navigate to the notebook file and open it
```

## Recommended Learning Path

Start in this order:

1. **01_python/fundamentals/** - Basic Python syntax
2. **01_python/control_flow/** - Loops and conditionals
3. **01_python/data_structures/** - Lists, dicts, sets
4. **01_python/functions/** - Function definitions
5. **01_python/oop/** - Object-oriented programming
6. **02_algorithms/** - Algorithmic thinking
7. **03_data_analysis/** - Data manipulation and visualization
8. **04_machine_learning/** - Machine learning workflows
9. **05_computer_vision/** - Computer vision basics

## Troubleshooting

### ModuleNotFoundError

Make sure your virtual environment is activated and dependencies are installed:

```bash
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

### Jupyter Notebook Not Found

Install Jupyter:

```bash
pip install jupyter
```

### Path Issues with Notebooks

All file paths should be relative to the notebook location. If you see hardcoded absolute paths, report them as issues.

## File Naming Convention

Files in this repository follow a descriptive naming pattern:

- **Python files**: `{concept}_{detail}.py`
  - Example: `binary_search_recursive.py`, `list_comprehension_example.py`
- **Notebooks**: `{topic}_{description}_{dataset}.ipynb`
  - Example: `clustering_kmeans_iris.ipynb`, `regression_house_price.ipynb`

## Questions?

See LEARNING_PATH.md for a detailed learning progression, or SKILLS.md to see what each section demonstrates.
