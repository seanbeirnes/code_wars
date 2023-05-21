# Function takes in a sequence and returns a list of items, without any adjacent duplicate items.
def unique_in_order(sequence):
    new_arr = []
    last_item = None
    for index, item in enumerate(sequence):
        if item != last_item:
            new_arr.append(item)
        last_item = item
        
    return new_arr
