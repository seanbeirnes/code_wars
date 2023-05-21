# Takes in a number between 1 and 3999 and converts it into a roman numeral, following the order and rules of roman numerals.
def solution(n):
    arr = []
    places = {"100":0,"10":0,"1":0}
    while n >= 1000:
        n -= 1000
        arr.append("M")
    while n >= 100:
        n -= 100
        places["100"] += 1
    while n >= 10:
        n -= 10
        places["10"] += 1
    while n >= 1:
        n -= 1
        places["1"] += 1
    
    def roman_maker(int, lstr, mid, hstr):
        result = []
        if int == 5:
            return mid
        elif int == 9:
            return lstr + hstr
        elif int > 5:
            result.append(mid)
            while int > 5:
                int -= 1
                result.append(lstr)
        elif int == 4:
            return lstr + mid
        elif int > 0:
            while int > 0:
                int -= 1
                result.append(lstr)
        else:
            return ""
        return "".join(result)
    
    arr.append(roman_maker(places["100"], "C", "D", "M"))
    arr.append(roman_maker(places["10"], "X", "L", "C"))
    arr.append(roman_maker(places["1"], "I", "V", "X"))
    return "".join(arr)
