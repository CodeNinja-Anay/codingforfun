"""
Input validation module that provides utilities for getting and validating user numerical input.
Contains functions for ensuring user input meets specific numerical criteria.
"""

def get_valid_input(min_value=1, max_value=100):
    """
    Validates user input to ensure it's a whole number between min_value and max_value.
    
    Args:
        min_value (int): Minimum acceptable value (default: 1)
        max_value (int): Maximum acceptable value (default: 100)
    
    Returns:
        int: Valid user input number
    """
    while True:
        try:
            user_input = input(f"Please enter a whole number between {min_value} and {max_value}: ")
            number = int(user_input)
            if min_value <= number <= max_value:
                return number
            print(f"Error: Number must be between {min_value} and {max_value}")
        except ValueError:
            print("Error: Please enter a valid whole number")
