def check_divisibility(num, divisor):
    """
    Task 1
    - Create a function to check if the number (num) is divisible by another number (divisor).
    - Both num and divisor must be numeric.
    - Return True if num is divisible by divisor, False otherwise.
    """
    
    if not (isinstance(num, (int, float)) and isinstance(divisor, (int, float))):
        return -1  # Invalid input
    
    if divisor == 0:
        return -1  # Cannot divide by zero
    
    return num % divisor == 0


# Task 2 — Invoke the function
print(check_divisibility(10, 2))  # Expected: True
print(check_divisibility(7, 3))   # Expected: False
