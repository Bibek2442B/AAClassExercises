import math
def entropyFunction(list):
    total = 0
    try:
        for item in list:
            num = float(item)
            total += (num / len(list)) * (math.log2(num / len(list)))
    except ValueError:
        return "Invalid value in the list"
    else:
        return -total

list = [20, 14, 24, 43, 46]
print(f"The entropy of the list is {entropyFunction(list)}")
