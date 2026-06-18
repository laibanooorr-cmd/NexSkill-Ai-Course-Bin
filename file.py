n = 5
num = 1
for i in range(1, n + 1):
    row = []
    for _ in range(i):
        row.append(str(num))
        num += 1
    print(" ".join(row))