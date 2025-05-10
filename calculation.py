import sys

def perform_calculations(data):
    """Performs two calculations: sum and average of the data."""
    total = sum(data)
    average = total / len(data) if data else 0
    return total, average