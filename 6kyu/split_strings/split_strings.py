# Splits a string into pairs, and if the string is an odd number, the final pair has an underscoure "_"
# Example: 'abc' =>  ['ab', 'c_']
def solution(s):
    char_pair = ""
    pairs_list = []
    for char in s:
        if len(char_pair) == 1:
            new_string = char_pair + char
            pairs_list.append(new_string)
            char_pair = ""
        else:
            char_pair = char
    if len(char_pair) == 1:
        new_string = char_pair + "_"
        pairs_list.append(new_string)
    return pairs_list
