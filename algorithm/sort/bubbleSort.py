from random import shuffle


row = list(range(0, 10))
shuffle(row)
print(row)

for i in range(len(row)):
    change = False
    for j in range(len(row) - 1, i, -1):
        if row[j - 1] > row[j]:
            row[j], row[j - 1] = row[j - 1], row[j]
            change = True
    if change != True:
        break
    print(row, change)
