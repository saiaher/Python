output = []

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        output.append("fizzbuzz")
    elif i % 5 == 0:
        output.append("fizz")
    elif i % 3 == 0:
        output.append("buzz")
    else:
        output.append(str(i))

print(output)
