import math

def entropyFunction(p1,p2):
    try:
        a=float(p1);b=float(p2)
        return -a * math.log2(a) - b * math.log2(b)
    except ValueError:
        return "Invalid input"


print(f"The entropy of 0 and 1 is {entropyFunction(0,1)}")
print(f"The entropy of 0.5 and 0.5 is ", entropyFunction(0.5,0.5))
print(f"The entropy of 0.1 and 0.9 is ", entropyFunction(0.1,0.9))
print(f"The entropy of 0.9 and 0.1 is ",entropyFunction(0.9,0.1))
