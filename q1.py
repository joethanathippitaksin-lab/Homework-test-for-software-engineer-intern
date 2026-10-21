def sum_positive(numbers):
    """Return the sum of all numbers greater than 0."""
    return sum(n for n in numbers if n > 0)


data = [-3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, -10]
print(sum_positive(data))