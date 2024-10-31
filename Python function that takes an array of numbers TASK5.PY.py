def sum_array(arr):
    # Input validation
    if arr is None or len(arr) <= 1:
        return 0

    # Remove the highest and lowest elements and sum the rest
    return sum(arr) - max(arr) - min(arr)

# Examples
print(sum_array([6, 2, 1, 8, 10]))
print(sum_array([1, 1, 11, 2, 3]))
print(sum_array([]))
print(sum_array([5]))
