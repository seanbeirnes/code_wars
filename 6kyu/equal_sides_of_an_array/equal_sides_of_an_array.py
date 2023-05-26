# Returns the index of an array where the the sum of the numbers to the left of the index is equal to the sum of the numbers to the right of the index.
# If this is not possible, then -1 is returned.
def find_even_index(arr):
    for i in range(len(arr)):
        if sum(arr[:i]) == sum(arr[i+1:]):
            return i
    return -1
