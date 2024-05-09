def solve(word, length):
    if length < 2:
        return -1

    c_count = 0
    b_count = 0
    a_count = 0


    while word[-1] != 'a':
        word = word[:-1]
    while word[0] != 'a':
        word = word[1:]

    length = len(word)

    if length < 2:
        return -1
    if length == 2:
        return 2

    print(word)

    arr = []

    b_count = 0
    c_count = 0

    for i in range(length):
        if i < length - 1 and word[i] == 'a' and word[i+1] == 'a':
            return 2

        if word[i] == 'a':
            arr.append([b_count, c_count])
            b_count = 0
            c_count = 0
        elif word[i] == 'b':
            b_count += 1
        elif word[i] == 'c':
            c_count += 1

    print(arr)


t = int(input())

for x in range(t):
    l = int(input())
    w = input()
    print(solve(w, l))
