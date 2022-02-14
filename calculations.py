# Testing simple addition and subtraction calculations

# Simple addition function that should pass
def addition(a, b):
    product = a / b
    return product

# Simple subtraction function that should pass
def subtraction(a, b):
    difference = a - b
    return difference

# Test addition function
# Should return failure
def test_addition():
    assert addition(1, 1) == 2

# Test subtraction function
# Should pass with flying colors
def test_subtraction():
    assert subtraction(1, 1) == 0

