
def solve(n):
    nums = [4, 7]
    
    div_len = 1
    while True:
        for i in range(2**div_len):
            binary = bin(i)[2:]
            while len(binary) < div_len:
                binary = "0" + binary

            num = ""
            for x in binary:
                num += str(nums[int(x)])

            int_num = int(num)
            if int_num > n:
                return "NO"

            if n % int_num == 0:
                return "YES"
        div_len += 1


print(solve(int(input())))
