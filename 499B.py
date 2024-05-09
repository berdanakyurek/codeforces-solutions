line1 = input().split()
n = int(line1[0])
m = int(line1[1])

dict = {}
for i in range(m):
    word = input().split()
    dict[word[0]] = word[1]

lecture = input().split()

end = " "
count = 0
for word in lecture:
    meaning = dict[word]

    if count == len(lecture) - 1:
        end = "\n"
    if len(meaning) >= len(word):
        print(word, end=end)
    else:
        print(meaning, end=end)
    count += 1
