# Checks if a number is a narcissistic number and returns True or False.
# Example:   1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153  -->  returns True
def narcissistic( value ):
    def split_places(num):
        place_values = []
        while num > 0:
            place_value = num % 10
            num //= 10
            place_values.append(place_value)
        return place_values
    split_number = split_places(value)
    digits = len(split_number)
    result = 0
    for int in split_number:
        result += int ** digits
    return result == value
