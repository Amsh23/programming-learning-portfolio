"""
Binary Search Implementation

Supplementary material - not original class code.
This demonstrates a fundamental algorithm with O(log n) complexity.

Binary search is one of the most important algorithms in computer science.
It demonstrates how algorithmic thinking can reduce complexity from O(n) to O(log n).
"""

# ============================================================================
# LINEAR SEARCH (Slower: O(n) complexity)
# ============================================================================

def linear_search(numbers: list[int], target: int) -> int:
    """
    Find target in list by checking each element sequentially.
    
    Time Complexity: O(n) - worst case, must check every element
    Space Complexity: O(1) - uses constant extra space
    
    Args:
        numbers: List of integers to search in (doesn't need to be sorted)
        target: Value to find
        
    Returns:
        Index of target if found, -1 if not found
    """
    for i in range(len(numbers)):
        if numbers[i] == target:
            return i
    return -1


# Example:
test_list = [3, 1, 4, 1, 5, 9, 2, 6]
print("Linear search for 5:", linear_search(test_list, 5))  # Output: 4

# Problem: What if list has 1,000,000 elements?
# Worst case: we check all 1,000,000 elements!


# ============================================================================
# BINARY SEARCH (Faster: O(log n) complexity)
# ============================================================================

def binary_search_iterative(numbers: list[int], target: int) -> int:
    """
    Find target in SORTED list by repeatedly dividing search space in half.
    
    Time Complexity: O(log n) - divide by 2 each time
    Space Complexity: O(1) - uses constant extra space
    
    Args:
        numbers: SORTED list of integers
        target: Value to find
        
    Returns:
        Index of target if found, -1 if not found
        
    Example:
        >>> binary_search_iterative([1, 3, 5, 7, 9], 5)
        2
    """
    left = 0
    right = len(numbers) - 1
    
    while left <= right:
        # Find middle element
        mid = (left + right) // 2
        mid_value = numbers[mid]
        
        # Check if we found the target
        if mid_value == target:
            return mid
        
        # If target is smaller, search left half
        elif target < mid_value:
            right = mid - 1
        
        # If target is larger, search right half
        else:
            left = mid + 1
    
    # Target not found
    return -1


# Example with sorted list:
sorted_list = [1, 3, 5, 7, 9, 11, 13, 15]
print("\nBinary search for 7:", binary_search_iterative(sorted_list, 7))  # Output: 3
print("Binary search for 6:", binary_search_iterative(sorted_list, 6))  # Output: -1


# ============================================================================
# BINARY SEARCH (RECURSIVE APPROACH)
# ============================================================================

def binary_search_recursive(numbers: list[int], target: int,
                          left: int = 0, right: int = None) -> int:
    """
    Recursive implementation of binary search.
    
    Time Complexity: O(log n)
    Space Complexity: O(log n) - due to recursion call stack
    
    Args:
        numbers: SORTED list of integers
        target: Value to find
        left: Left boundary (default: 0)
        right: Right boundary (default: len(numbers)-1)
        
    Returns:
        Index if found, -1 if not found
    """
    if right is None:
        right = len(numbers) - 1
    
    # Base case: target not found
    if left > right:
        return -1
    
    mid = (left + right) // 2
    mid_value = numbers[mid]
    
    # Base case: found target
    if mid_value == target:
        return mid
    
    # Recursive case: search left half
    elif target < mid_value:
        return binary_search_recursive(numbers, target, left, mid - 1)
    
    # Recursive case: search right half
    else:
        return binary_search_recursive(numbers, target, mid + 1, right)


print("Binary search recursive for 7:", binary_search_recursive(sorted_list, 7))  # Output: 3


# ============================================================================
# VISUALIZING HOW BINARY SEARCH WORKS
# ============================================================================

def binary_search_with_visualization(numbers: list[int], target: int) -> int:
    """Binary search that shows each step."""
    left = 0
    right = len(numbers) - 1
    step = 0
    
    print(f"\nSearching for {target} in {numbers}")
    print("="*60)
    
    while left <= right:
        mid = (left + right) // 2
        mid_value = numbers[mid]
        step += 1
        
        # Visualize current search space
        visual = ""
        for i in range(len(numbers)):
            if i < left or i > right:
                visual += "  .  "  # Outside search space
            elif i == mid:
                visual += f"[{numbers[i]}]"  # Middle element
            else:
                visual += f" {numbers[i]} "
        
        print(f"Step {step}: Left={left}, Mid={mid}, Right={right}")
        print(f"Search space: {visual}")
        
        if mid_value == target:
            print(f"✓ Found {target} at index {mid} after {step} steps!")
            return mid
        elif target < mid_value:
            print(f"  {target} < {mid_value}, search left half")
            right = mid - 1
        else:
            print(f"  {target} > {mid_value}, search right half")
            left = mid + 1
    
    print(f"✗ {target} not found after {step} steps")
    return -1


# Visualize binary search:
binary_search_with_visualization([1, 3, 5, 7, 9, 11, 13, 15], 11)


# ============================================================================
# COMPLEXITY COMPARISON: VISUAL
# ============================================================================

print("\n" + "="*60)
print("COMPLEXITY COMPARISON")
print("="*60)

import math

test_sizes = [10, 100, 1000, 10000, 1000000]

for size in test_sizes:
    linear_max = size  # Worst case: O(n)
    binary_max = math.ceil(math.log2(size))  # O(log n)
    ratio = linear_max / binary_max if binary_max > 0 else 0
    
    print(f"\nList size: {size:,} elements")
    print(f"  Linear search worst case: {linear_max:,} checks")
    print(f"  Binary search worst case: {binary_max} checks")
    print(f"  Binary search is {ratio:.0f}x faster!")


# ============================================================================
# REAL-WORLD EXAMPLE: FIND A WORD IN DICTIONARY
# ============================================================================

# Simulate a dictionary (sorted words)
dictionary = [
    "apple", "banana", "cherry", "date", "elderberry",
    "fig", "grape", "honeydew", "kiwi", "lemon"
]

print("\n" + "="*60)
print("REAL-WORLD EXAMPLE: Dictionary Search")
print("="*60)

binary_search_with_visualization(dictionary, "grape")


# ============================================================================
# EDGE CASES AND IMPORTANT NOTES
# ============================================================================

print("\n" + "="*60)
print("EDGE CASES")
print("="*60)

# Edge case 1: Empty list
empty = []
print(f"Empty list: {binary_search_iterative(empty, 5)}")  # -1

# Edge case 2: Single element (found)
single_found = [5]
print(f"Single element (found): {binary_search_iterative(single_found, 5)}")  # 0

# Edge case 3: Single element (not found)
single_not_found = [5]
print(f"Single element (not found): {binary_search_iterative(single_not_found, 3)}")  # -1

# Edge case 4: Target at edges
edges = [1, 2, 3, 4, 5]
print(f"Target at start: {binary_search_iterative(edges, 1)}")  # 0
print(f"Target at end: {binary_search_iterative(edges, 5)}")  # 4

# Edge case 5: Duplicates (binary search returns one index)
duplicates = [1, 2, 2, 2, 3]
print(f"Duplicates (returns index of one 2): {binary_search_iterative(duplicates, 2)}")  # 1, 2, or 3


# ============================================================================
# KEY REQUIREMENT: LIST MUST BE SORTED!
# ============================================================================

print("\n" + "="*60)
print("CRITICAL: LIST MUST BE SORTED!")
print("="*60)

# Wrong: Unsorted list - binary search may fail
unsorted = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"Unsorted list: {unsorted}")
print(f"Binary search result: {binary_search_iterative(unsorted, 5)}")  # ✗ Wrong/unreliable!

# Right: Sort first, then binary search
sorted_data = sorted(unsorted)
print(f"Sorted list: {sorted_data}")
print(f"Binary search result: {binary_search_iterative(sorted_data, 5)}")  # ✓ Correct


# ============================================================================
# PRACTICE EXERCISES
# ============================================================================

print("\n" + "="*60)
print("PRACTICE EXERCISES")
print("="*60)

# Exercise 1: Find index of 11 in this sorted list
exercise1 = [2, 5, 8, 11, 14, 17, 20]
print(f"\nExercise 1: Find 11 in {exercise1}")
print(f"Result: {binary_search_iterative(exercise1, 11)}")  # Should be 3

# Exercise 2: Find index of 1 in this sorted list
exercise2 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
print(f"\nExercise 2: Find 1 in {exercise2}")
print(f"Result: {binary_search_iterative(exercise2, 1)}")  # Should be 0

# Exercise 3: What about a value that doesn't exist?
print(f"\nExercise 3: Find 100 in {exercise2}")
print(f"Result: {binary_search_iterative(exercise2, 100)}")  # Should be -1


# ============================================================================
# KEY TAKEAWAYS
# ============================================================================

"""
KEY TAKEAWAYS:

1. Binary Search Basics:
   - Works ONLY on sorted lists
   - Reduces search from O(n) to O(log n)
   - Essential algorithm to know

2. How it works:
   - Eliminate half the search space each iteration
   - Compare middle element to target
   - Narrow down to left or right half

3. Iterative vs Recursive:
   - Iterative: O(1) space, easier to understand
   - Recursive: O(log n) space, more elegant

4. Key Requirements:
   - List MUST be sorted
   - Only works on arrays/lists with random access

5. When to use binary search:
   - When you need to find elements in sorted data
   - When speed matters (1,000,000 items)
   - When you're implementing search functionality

6. Real-world applications:
   - Dictionary/phone book search
   - Database queries
   - Version control (git bisect)
   - Testing bisection method
   - API endpoints (pagination)
"""

print("\nYou've learned binary search - a fundamental algorithm!")
print("Use it whenever you need to search in sorted data.")
