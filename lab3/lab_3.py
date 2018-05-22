string = "test 5 a0A pass007"

words = string.split(' ')
counts = []

for i in range(len(words)):
    countInt = 0
    countLet = 0
    let = 0
    num = 0
    letters = len(words[i])
    for c in words[i]:
        if c.isdigit():
            countInt = countInt + 1

    countLet = letters - countInt
    let = countLet % 2
    num = countInt % 2
    if let == 0 and num > 0:
        counts.append(letters)
    else:
        counts.append(0)

maximum = counts[0]
index = 0
for i in range(1, len(counts)):
    if maximum < counts[i]:
        maximum = counts[i]
        index = i

print(words[index])