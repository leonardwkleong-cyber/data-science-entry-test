def swap(x, y):
    """
    Task 1
    - Create a function that would swap the value of x and y using only x and y as variables.
    - x and y must be numeric.
    - Return -1 if x or y is not numeric.
    - Print the swapped values if both x and y are numeric.
    """
    
    # Validate numeric types
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        return -1
    
    # Swap using Python tuple unpacking (no extra variables)
    x, y = y, x
    
    print("Swapped values:", x, y)


# Task 2 — Invoke the function
print(swap("Apple", 10))   # Expect: -1
swap(9, 17)                # Expect: prints "Swapped values: 17 9"
