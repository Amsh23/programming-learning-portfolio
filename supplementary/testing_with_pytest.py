"""
Testing with Pytest - Best Practices

Supplementary material - not original class code.
This demonstrates how to write professional tests that ensure code quality
and prevent bugs in production.

Testing is a core skill that separates professional developers from hobbyists.
No professional code ships without tests.
"""

import pytest
from typing import List


# ============================================================================
# PART 1: FUNCTIONS TO TEST
# ============================================================================

def add(a: float, b: float) -> float:
    """Add two numbers."""
    return a + b


def divide(a: float, b: float) -> float:
    """
    Divide two numbers.
    
    Raises:
        ValueError: If divisor is zero
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def find_max(numbers: List[int]) -> int:
    """
    Find maximum value in list.
    
    Raises:
        ValueError: If list is empty
    """
    if not numbers:
        raise ValueError("List cannot be empty")
    return max(numbers)


def is_even(n: int) -> bool:
    """Check if number is even."""
    return n % 2 == 0


def remove_duplicates(items: List[int]) -> List[int]:
    """Remove duplicates while preserving order."""
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


class Calculator:
    """Simple calculator class for testing OOP."""
    
    def __init__(self, initial: float = 0):
        self.value = initial
    
    def add(self, n: float) -> float:
        """Add to current value."""
        self.value += n
        return self.value
    
    def subtract(self, n: float) -> float:
        """Subtract from current value."""
        self.value -= n
        return self.value
    
    def reset(self):
        """Reset to zero."""
        self.value = 0


# ============================================================================
# PART 2: WRITING BASIC TESTS
# ============================================================================

"""
Test file structure:

1. Test file name: test_<module_name>.py
   OR: <module_name>_test.py
   
2. Test function names: test_<what_you_are_testing>
   Example: test_add_positive_numbers
   
3. Test structure: Arrange, Act, Assert (AAA pattern)
   - Arrange: Set up test data
   - Act: Call the function
   - Assert: Check the result

4. File location:
   ├── src/
   │   └── calculator.py (code)
   └── tests/
       └── test_calculator.py (tests)
"""

# ============================================================================
# PART 3: BASIC TESTS - HAPPY PATH
# ============================================================================

class TestBasicFunctions:
    """Tests for basic functions."""
    
    def test_add_positive_numbers(self):
        """Test adding two positive numbers."""
        # Arrange
        a, b = 2, 3
        expected = 5
        
        # Act
        result = add(a, b)
        
        # Assert
        assert result == expected
    
    def test_add_negative_numbers(self):
        """Test adding two negative numbers."""
        assert add(-2, -3) == -5
    
    def test_add_mixed_signs(self):
        """Test adding numbers with different signs."""
        assert add(5, -3) == 2
        assert add(-5, 3) == -2
    
    def test_add_zero(self):
        """Test adding with zero."""
        assert add(5, 0) == 5
        assert add(0, 0) == 0
    
    def test_add_floats(self):
        """Test adding floating point numbers."""
        result = add(0.1, 0.2)
        # Be careful with float precision!
        assert abs(result - 0.3) < 1e-9  # Check within tolerance


# ============================================================================
# PART 4: TESTS WITH EXCEPTIONS
# ============================================================================

class TestExceptionHandling:
    """Tests for functions that raise exceptions."""
    
    def test_divide_by_zero_raises_error(self):
        """Test that dividing by zero raises ValueError."""
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            divide(5, 0)
    
    def test_divide_normal(self):
        """Test normal division."""
        assert divide(6, 2) == 3
        assert divide(10, 4) == 2.5
    
    def test_find_max_empty_list(self):
        """Test that empty list raises ValueError."""
        with pytest.raises(ValueError, match="cannot be empty"):
            find_max([])
    
    def test_find_max_single_element(self):
        """Test finding max in single element list."""
        assert find_max([42]) == 42
    
    def test_find_max_multiple_elements(self):
        """Test finding max in list."""
        assert find_max([3, 1, 4, 1, 5, 9]) == 9


# ============================================================================
# PART 5: PARAMETRIZED TESTS
# ============================================================================

class TestParametrized:
    """Tests using pytest parametrize - DRY principle."""
    
    @pytest.mark.parametrize("n,expected", [
        (2, True),   # Even
        (4, True),   # Even
        (0, True),   # Even
        (1, False),  # Odd
        (3, False),  # Odd
        (-2, True),  # Negative even
        (-3, False), # Negative odd
    ])
    def test_is_even(self, n, expected):
        """Test is_even with multiple inputs."""
        assert is_even(n) == expected
    
    @pytest.mark.parametrize("input_list,expected", [
        ([1, 1, 2, 2, 3], [1, 2, 3]),
        ([1, 2, 3, 4], [1, 2, 3, 4]),
        ([1, 1, 1, 1], [1]),
        ([], []),
        ([5], [5]),
    ])
    def test_remove_duplicates(self, input_list, expected):
        """Test remove_duplicates with various inputs."""
        assert remove_duplicates(input_list) == expected


# ============================================================================
# PART 6: CLASS/OBJECT TESTING
# ============================================================================

class TestCalculatorClass:
    """Tests for Calculator class - fixtures pattern."""
    
    @pytest.fixture
    def calc(self):
        """Create a fresh Calculator for each test."""
        return Calculator()
    
    def test_add_to_calculator(self, calc):
        """Test adding to calculator."""
        result = calc.add(5)
        assert result == 5
        assert calc.value == 5
    
    def test_subtract_from_calculator(self, calc):
        """Test subtracting from calculator."""
        calc.add(10)  # Start with 10
        result = calc.subtract(3)
        assert result == 7
        assert calc.value == 7
    
    def test_reset_calculator(self, calc):
        """Test resetting calculator."""
        calc.add(100)
        assert calc.value == 100
        calc.reset()
        assert calc.value == 0
    
    def test_chained_operations(self, calc):
        """Test multiple operations in sequence."""
        calc.add(5)
        calc.add(3)
        calc.subtract(2)
        assert calc.value == 6
    
    def test_calculator_with_initial_value(self):
        """Test creating calculator with initial value."""
        calc = Calculator(initial=100)
        assert calc.value == 100
        calc.add(50)
        assert calc.value == 150


# ============================================================================
# PART 7: FIXTURES - SETUP AND TEARDOWN
# ============================================================================

class TestFixtures:
    """Demonstrate fixtures for test setup and teardown."""
    
    @pytest.fixture(autouse=True)
    def setup_and_teardown(self):
        """Setup before test, cleanup after."""
        # Setup
        print("\n  Setting up test...")
        test_data = {"initialized": True}
        
        yield test_data  # Test runs here
        
        # Teardown (cleanup)
        print("\n  Cleaning up test...")
    
    def test_with_setup_teardown(self):
        """This test has automatic setup/teardown."""
        assert True


# ============================================================================
# PART 8: ASSERTIONS - DETAILED MESSAGES
# ============================================================================

class TestAssertions:
    """Demonstrate different assertion techniques."""
    
    def test_assert_equal(self):
        """Basic equality assertion."""
        assert add(2, 3) == 5
    
    def test_assert_not_equal(self):
        """Inequality assertion."""
        assert add(2, 3) != 6
    
    def test_assert_in(self):
        """Check membership."""
        result = remove_duplicates([1, 2, 3, 2, 1])
        assert 1 in result
        assert 4 not in result
    
    def test_assert_is_instance(self):
        """Check type."""
        result = add(2, 3)
        assert isinstance(result, (int, float))
    
    def test_assert_true_false(self):
        """Boolean assertions."""
        assert is_even(4) is True
        assert is_even(5) is False
    
    def test_assert_list_operations(self):
        """Assertions on lists."""
        result = [1, 2, 3]
        assert len(result) == 3
        assert result[0] == 1
        assert result[-1] == 3


# ============================================================================
# PART 9: BEST PRACTICES CHECKLIST
# ============================================================================

"""
Best Practices for Testing:

✓ DO:
  - Write tests WHILE developing (Test-Driven Development)
  - Name tests clearly: test_<what_it_tests>
  - Test both happy path AND error cases
  - Use fixtures for common setup
  - Keep tests independent (no test depends on another)
  - Test one thing per test function
  - Use descriptive assertion messages
  - Test edge cases (empty, zero, negative, max values)
  - Parametrize tests to reduce duplication
  - Run tests frequently (after every change)

✗ DON'T:
  - Skip testing because "it's obvious it works"
  - Write untestable code (hardcoded values, global state)
  - Have tests that sometimes pass, sometimes fail (flaky tests)
  - Write tests that are more complex than the code
  - Ignore test failures
  - Test implementation details, test behavior
  - Make tests interdependent
  - Have tests that print output instead of assert
"""


# ============================================================================
# PART 10: RUNNING TESTS
# ============================================================================

"""
How to run tests:

# Run all tests in current directory
pytest

# Run specific test file
pytest test_calculator.py

# Run specific test class
pytest test_calculator.py::TestCalculator

# Run specific test function
pytest test_calculator.py::test_add_positive_numbers

# Run with verbose output
pytest -v

# Run with output/print statements
pytest -s

# Run and stop on first failure
pytest -x

# Run only tests matching a pattern
pytest -k "test_add"

# Run with coverage report
pytest --cov

# Run with junit report for CI/CD
pytest --junit-xml=results.xml

# Run in parallel (faster)
pytest -n auto  # Requires pytest-xdist plugin
"""


# ============================================================================
# PART 11: TEST COVERAGE
# ============================================================================

"""
Code Coverage: Percentage of code executed by tests

Good coverage = 80%+ ideally
- 100% = Every line executed by at least one test
- 0% = No tests

View coverage:
  pip install pytest-cov
  pytest --cov=src
  
Coverage doesn't guarantee quality, but low coverage means untested code!
"""


# ============================================================================
# PART 12: COMMON TEST PATTERNS
# ============================================================================

class TestCommonPatterns:
    """Common testing patterns and techniques."""
    
    def test_setup_with_fixture(self):
        """Fixture setup pattern."""
        # See @pytest.fixture examples above
        pass
    
    def test_skip_this_test(self):
        """Skip a test temporarily."""
        # @pytest.mark.skip(reason="Not implemented yet")
        pass
    
    def test_xfail_known_issue(self):
        """Mark expected failure for known bug."""
        # @pytest.mark.xfail(reason="Bug #123")
        pass
    
    def test_slow_operation(self):
        """Mark slow tests separately."""
        # @pytest.mark.slow
        # Run with: pytest -m "not slow"
        pass


# ============================================================================
# PART 13: EXAMPLE - FULL TEST FILE STRUCTURE
# ============================================================================

"""
Recommended project structure:

project/
├── src/
│   ├── __init__.py
│   ├── calculator.py       (production code)
│   ├── data_processor.py   (production code)
│   └── utils.py            (production code)
│
├── tests/
│   ├── __init__.py
│   ├── conftest.py         (shared fixtures)
│   ├── test_calculator.py  (tests for calculator)
│   ├── test_data_processor.py
│   └── test_utils.py
│
├── pytest.ini              (pytest configuration)
├── requirements.txt
└── README.md

File: pytest.ini
[pytest]
testpaths = tests
python_files = test_*.py
python_classes = Test*
python_functions = test_*
"""


# ============================================================================
# PART 14: INTERVIEW QUESTIONS
# ============================================================================

"""
Common Testing Interview Questions:

Q: What is the difference between unit tests and integration tests?
A: Unit tests test individual functions in isolation.
   Integration tests test how multiple components work together.

Q: What's a fixture?
A: A fixture is reusable test setup/teardown code.
   Example: Creating a database connection for multiple tests.

Q: What is mocking?
A: Replacing real objects with fake ones to isolate code.
   Example: Mocking a network call during testing.

Q: How do you test code that raises exceptions?
A: Use pytest.raises(ExceptionType) context manager.

Q: What's code coverage?
A: Percentage of code that runs during tests.
   High coverage (80%+) reduces bugs.

Q: Should you test everything?
A: Test the important parts:
   - Business logic
   - Error cases
   - Edge cases
   Skip: Trivial getters/setters, third-party libraries
"""


# ============================================================================
# SUMMARY
# ============================================================================

"""
TESTING SUMMARY:

1. Why Test?
   - Catch bugs before production
   - Enable confident refactoring
   - Serve as documentation
   - Improve code design

2. Test Types:
   - Unit tests: Test individual functions
   - Integration tests: Test components together
   - End-to-end tests: Test full workflows

3. Best Practices:
   - Write tests early (TDD)
   - Test happy path AND errors
   - Use descriptive names
   - Keep tests independent
   - Parametrize similar tests

4. Tools:
   - pytest: Testing framework
   - pytest-cov: Coverage reports
   - pytest-xdist: Parallel testing
   - pytest-mock: Mocking

5. How to Start:
   - Install pytest: pip install pytest
   - Create tests/ folder
   - Write test_<module>.py files
   - Run tests: pytest
   - Add coverage: pytest --cov

Remember: Code without tests is broken by default.
Professional developers test their code.
"""

print(__doc__)
