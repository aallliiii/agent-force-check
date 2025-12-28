import math
from typing import List, Dict

def add_numbers(a: int, b: int) -> int:
    """Returns the sum of two numbers."""
    return a + b

def factorial(n: int) -> int:
    """Returns the factorial of a number."""
    if n < 0:
        raise ValueError("Negative numbers not allowed")
    return math.prod(range(1, n + 1)) if n else 1

def find_max(numbers: List[int]) -> int:
    """Returns the maximum value in a list."""
    if not numbers:
        raise ValueError("Empty list")
    return max(numbers)

def average_grade(grades: Dict[str, float]) -> float:
    """Calculates average from a dictionary of grades."""
    if not grades:
        raise ValueError("No grades provided")
    return sum(grades.values()) / len(grades)
