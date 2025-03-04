a = [[1, 0, 0], 
     [0, 1, 0], 
     [0, 0, 1]]

b = [[1, 2, 3], 
     [4, 5, 6], 
     [7, 8, 9]]

rows = len(a)
cols = len(b[0])

c = []

for i in range(rows):
    row = []
    for j in range(cols):
        row.append(0)
    c.append(row)

for i in range(rows):
    for j in range(cols):
        for k in range(rows):
            c[i][j] += a[i][k] * b[k][j]

print(c)