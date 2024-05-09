
def apply_op(a, b, op):
    if op == "+":
        return a + b
    return a * b
    
def solve(a, b, c):
    op1 = None
    op2 = None

    if a == 1:
        op1 = "+"

    if c == 1:
        op2 = "+"

    if b == 1:
        if a <= c:
            op1 = "+"
        else:
            op2 = "+"

    if op1 == None:
        op1 = "*"
    if op2 == None:
        op2 = "*"

    res1 = 0
    res2 = 0

    res1 = apply_op(a, b, op1)
    res1 = apply_op(res1, c, op2)

    res2 = apply_op(b, c, op2)
    res2 = apply_op(res2, a, op1)

    return max(res1, res2)

print(solve(int(input()), int(input()), int(input())))
