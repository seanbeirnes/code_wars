# Given an array of integers, the function returns the number the occurs an odd number of times.
# Example: [1,2,2,3,3,3,4,3,3,3,2,2,1] returns 4.
def find_it(seq):
    dict = {}
    for int in seq:
        if int not in dict:
            dict[int] = 1
        else:
            dict[int] += 1
    for key, value in dict.items():
        if value % 2 != 0:
            return key
    return dict
