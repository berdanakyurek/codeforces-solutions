def abs(n):
    if n < 0:
        return -1 * n
    return n

def solve(x, y, a, b):
    use_b = False
    if b <= 2 * a:
        use_b = True

    total = 0
    
    if use_b and x > 0 and y > 0:
        minimum = min(x, y)
        total += minimum * b
        x -= minimum
        y -= minimum

    if use_b and x < 0 and y < 0:
        maximum = -1 * max(x, y)
        total += maximum * b
        x += maximum
        y += maximum
    return total + (abs(x) + abs(y)) * a

for i in range(int(input())):
    split1 = input().split()
    split2 = input().split()

    x = int(split1[0])
    y = int(split1[1])
    a = int(split2[0])
    b = int(split2[1])
    print(solve(x, y, a, b))
