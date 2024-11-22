"""
Geometric calculator module providing utilities for calculating circular positions.
Contains functions for computing evenly distributed points on a circle's circumference
and related geometric calculations.
"""

import math


def position_calculator(items_list):
    """
    Calculates evenly spaced positions on a circle's circumference based on list length.

    Args:
        items_list (list): List of items to calculate positions for

    Returns:
        tuple: (radius, list of (x,y) coordinates)
            - radius (float): Calculated radius of the circle
            - positions (list): List of (x,y) tuples representing points on the circle
    """
    num_items = len(items_list)
    radius = max(100, 50 * math.sqrt(num_items))
    positions = []

    for i in range(num_items):
        angle = (2 * math.pi * i) / num_items
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        positions.append((round(x, 2), round(y, 2)))

    return (radius, positions)
