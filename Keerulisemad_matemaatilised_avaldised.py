"""Math exercises vol2."""

import math

# 1. Time converter function
def time_converter(seconds: int) -> str:
    """Convert time in seconds to hours and minutes."""
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    return f"{seconds} sekundit on {hours} tund(i) ja {minutes} minut(it)."

# 2. Student helper function
def student_helper(angle: int) -> str:
    """Return the sine and cosine of the given angle in degrees."""
    sine = round(math.sin(math.radians(angle)), 1)
    cosine = round(math.cos(math.radians(angle)), 1)
    return f"Nurk: {angle}, siinus: {sine}, koosinus: {cosine}."

# 3. Greetings function
def greetings(n: int) -> str:
    """Return a string that contains 'Hey' n times."""
    lots_of_heys = "Hey" * n
    return lots_of_heys

# 4. Adding numbers function
def adding_numbers(num_a: int, num_b: int) -> str:
    """Return given numbers added together as a string."""
    string_numbers = str(num_a) + str(num_b)
    return string_numbers

# Testing each function with sample inputs
print("Test Results:")
print("time_converter(3665):", time_converter(3665))
print("student_helper(30):", student_helper(30))
print("greetings(4):", greetings(4))
print("adding_numbers(123, 456):", adding_numbers(123, 456))
