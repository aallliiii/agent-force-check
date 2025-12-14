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


class Rectangle:
    """Represents a rectangle shape."""

    def _init_(self, width: float, height: float):
        if width <= 0 or height <= 0:
            raise ValueError("Dimensions must be positive")
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height

    def perimeter(self) -> float:
        return 2 * (self.width + self.height)

    def is_square(self) -> bool:
        return self.width == self.height


def print_age(age):
    print(age)

def print_banana(f):
    print(f)


def check_k_character(g):
    if g=="k":
        return True
    else:
        return False

def check_oo_character(g):
    if g=="oo":
        return True
    else:
        return False
    
    
    
def check_b_character(g):
    if g=="b":
        return True
    else:
        return False
    
    
def check_o_character(g):
    if g=="o":
        return True
    else:
        return False
    
def check_a_character(g):
    if g=="a":
        return True
    else:
        return False
    
def check_k_character(g):
    if g=="k":
        return True
    else:
        return False
    
def check_is_even(number):
    if number %2==0:
        return True
    else:
        return False


def print_age(age):
    print(age)

def print_banana(f):
    print(f)


def check_k_character(g):
    if g=="k":
        return True
    else:
        return False

def check_oo_character(g):
    if g=="oo":
        return True
    else:
        return False
    
    
    
def check_b_character(g):
    if g=="b":
        return True
    else:
        return False
    