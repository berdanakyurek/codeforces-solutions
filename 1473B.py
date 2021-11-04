import math

def lcmN(a,b):
    return abs(a*b) // math.gcd(a, b)

def lcm(a,b):
    if a == b:
        return a

    if len(a) == len(b):
        return -1

    if len(b) > len(a):
        temp = a
        a = b
        b = temp

    if a[0:len(b)] != b:
        return -1
    
    lcmNumeric = lcmN(len(a),len(b))
    a *= lcmNumeric//len(a)
    b *= lcmNumeric//len(b)
    
    if a == b:
        return a
    return -1
    
t = int(input())

for i in range(t):
    a = input()
    b = input()
    print(lcm(a,b))