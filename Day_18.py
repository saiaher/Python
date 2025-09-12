n = int(input("Enter number of rows: "))

triangle = []

for i in range(n):
    row = [1]  

    if i > 0:
        for j in range(1, i):
            value = triangle[i - 1][j - 1] + triangle[i - 1][j]
            row.append(value)

        row.append(1)  

    triangle.append(row)


for l in triangle:
    print(l)
