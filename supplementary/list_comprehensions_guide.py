"""
List Comprehension Fundamentals

Supplementary material - not original class code.
This demonstrates a core Python concept that's essential for writing clean, pythonic code.

List comprehensions are one of Python's most powerful and elegant features.
They provide a concise way to create lists compared to using loops.
"""

# ============================================================================
# BASIC LIST COMPREHENSION
# ============================================================================

# Traditional approach with a loop
squares_loop = []
for i in range(5):
    squares_loop.append(i ** 2)
print("Traditional loop:", squares_loop)  # [0, 1, 4, 9, 16]

# List comprehension approach
squares_comp = [i ** 2 for i in range(5)]
print("List comprehension:", squares_comp)  # [0, 1, 4, 9, 16]
# Result is identical but more concise and readable


# ============================================================================
# WHY USE LIST COMPREHENSIONS?
# ============================================================================

# 1. Conciseness - Write less code
# 2. Performance - Generally faster than loops for creating lists
# 3. Readability - More pythonic and elegant
# 4. Functionality - Can include conditions easily

# Example: Create squares of only even numbers
# With loop:
even_squares_loop = []
for i in range(10):
    if i % 2 == 0:
        even_squares_loop.append(i ** 2)

# With list comprehension:
even_squares_comp = [i ** 2 for i in range(10) if i % 2 == 0]
print("Even squares:", even_squares_comp)  # [0, 4, 16, 36, 64]


# ============================================================================
# SYNTAX: THE FORMULA
# ============================================================================

# General syntax:
# [expression for item in iterable if condition]
#
# Breaking it down:
# - expression: What to compute (e.g., i ** 2)
# - for item in iterable: Loop through a sequence
# - if condition: Optional filter

# Example: Convert strings to integers
str_numbers = ["1", "2", "3", "4", "5"]
int_numbers = [int(x) for x in str_numbers]
print("Converted to int:", int_numbers)  # [1, 2, 3, 4, 5]


# ============================================================================
# PRACTICAL EXAMPLES
# ============================================================================

# Example 1: Extract first character of each word
words = ["python", "java", "javascript", "c"]
first_letters = [word[0] for word in words]
print("First letters:", first_letters)  # ['p', 'j', 'j', 'c']

# Example 2: Uppercase all words
uppercase_words = [word.upper() for word in words]
print("Uppercase:", uppercase_words)  # ['PYTHON', 'JAVA', 'JAVASCRIPT', 'C']

# Example 3: Filter strings by length
long_words = [word for word in words if len(word) > 4]
print("Words with length > 4:", long_words)  # ['python', 'javascript']

# Example 4: Transform and filter combined
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = [x * 2 for x in numbers if x % 2 == 0]
print("Double the even numbers:", result)  # [4, 8, 12, 16, 20]


# ============================================================================
# NESTED LIST COMPREHENSIONS
# ============================================================================

# Create a multiplication table
# Traditional approach:
table_loop = []
for i in range(1, 4):
    row = []
    for j in range(1, 4):
        row.append(i * j)
    table_loop.append(row)

# List comprehension approach:
table_comp = [[i * j for j in range(1, 4)] for i in range(1, 4)]

print("Multiplication table:")
for row in table_comp:
    print(row)
# Output:
# [1, 2, 3]
# [2, 4, 6]
# [3, 6, 9]

# Flatten a 2D list
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [num for row in matrix for num in row]
print("Flattened matrix:", flat)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]


# ============================================================================
# CONDITIONAL EXPRESSIONS IN COMPREHENSIONS
# ============================================================================

# Replace elements conditionally
numbers = [1, 2, 3, 4, 5]

# Set even numbers to 0, keep odd numbers
result = [0 if x % 2 == 0 else x for x in numbers]
print("Replace evens with 0:", result)  # [1, 0, 3, 0, 5]

# Example: Grade assignment based on score
scores = [92, 78, 85, 91, 66]
grades = ["A" if s >= 90 else "B" if s >= 80 else "C" for s in scores]
print("Grades:", grades)  # ['A', 'B', 'B', 'A', 'C']


# ============================================================================
# SET AND DICTIONARY COMPREHENSIONS
# ============================================================================

# Set comprehension - removes duplicates automatically
numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
unique_squares = {x ** 2 for x in numbers}  # Note: { } for sets
print("Unique squares:", unique_squares)  # {1, 4, 9, 16}

# Dictionary comprehension - create key-value pairs
words = ["apple", "banana", "cherry"]
word_lengths = {word: len(word) for word in words}
print("Word lengths:", word_lengths)  # {'apple': 5, 'banana': 6, 'cherry': 6}

# Dictionary from lists
keys = ["a", "b", "c"]
values = [1, 2, 3]
my_dict = {k: v for k, v in zip(keys, values)}
print("Dict from lists:", my_dict)  # {'a': 1, 'b': 2, 'c': 3}


# ============================================================================
# PERFORMANCE COMPARISON
# ============================================================================

import timeit

# Time comparison: 1 million iterations
def using_loop():
    result = []
    for i in range(1000):
        result.append(i ** 2)
    return result

def using_comprehension():
    return [i ** 2 for i in range(1000)]

loop_time = timeit.timeit(using_loop, number=1000)
comp_time = timeit.timeit(using_comprehension, number=1000)

print(f"\nLoop time: {loop_time:.4f} seconds")
print(f"Comprehension time: {comp_time:.4f} seconds")
print(f"Comprehension is {loop_time/comp_time:.2f}x faster")


# ============================================================================
# WHEN TO USE COMPREHENSIONS
# ============================================================================

# ✅ USE comprehensions when:
# - Creating a new list from an existing one
# - The logic is simple and readable (1-2 lines)
# - You need filtering or transformation
# - Performance matters (loops are slower)

# ❌ AVOID comprehensions when:
# - Logic is complex (many nested conditions)
# - Side effects are needed (printing, writing files)
# - Debugging is needed (comprehensions can be hard to debug)
# - Readability would suffer with nesting

# Complex logic example - use a function instead:
def process_data(items):
    """
    Process items with complex logic.
    Better as a separate function than a comprehension.
    """
    results = []
    for item in items:
        # Many lines of processing logic
        processed = item.upper()
        if len(processed) > 5:
            results.append(processed)
    return results

# Then use: data = process_data(words)


# ============================================================================
# PRACTICE EXERCISES
# ============================================================================

print("\n" + "="*50)
print("PRACTICE EXERCISES")
print("="*50)

# Exercise 1: Create a list of squares for numbers 1-10
# TODO: Write your own list comprehension
print("Exercise 1: Squares of 1-10")

# Exercise 2: Filter even numbers from 1-20
print("\nExercise 2: Even numbers 1-20")

# Exercise 3: Convert a list of strings to their lengths
fruits = ["apple", "banana", "cherry", "date"]
print("\nExercise 3: Lengths of fruits")

# Exercise 4: Create nested list (2D grid) of 0s (3x3)
print("\nExercise 4: 3x3 grid of zeros")


# ============================================================================
# KEY TAKEAWAYS
# ============================================================================

"""
Key Takeaways:

1. List comprehension syntax: [expression for item in iterable if condition]

2. Advantages:
   - More concise than loops
   - Generally faster
   - More "pythonic"
   - More readable for simple operations

3. You can also use comprehensions for sets and dictionaries

4. Nested comprehensions work but can reduce readability

5. When logic gets complex, use a regular loop or function instead

6. List comprehensions are a fundamental Python skill - practice them!
"""

print("\nCongratulations! You now understand list comprehensions.")
print("Use them to write more elegant Python code!")
