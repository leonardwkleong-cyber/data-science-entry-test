def string_reverse(s):
    """
    Task 1
    - Create a function that reverses a given string (s).
    - s must be a string.
    - Return the reversed string.
    """
    
    if not isinstance(s, str):
        return -1  # Invalid input
    
    # Reverse using slicing
    return s[::-1]


# Task 2 — Invoke the function
print(string_reverse("Hello World"))
print(string_reverse("Python"))
