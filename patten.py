row=5
for i in range(1,10):
    if i<=row:
        star=i
    else:
        star=2*row-i  
    space=row-star
    line=""*space+star*"*"      
    print(line)





    row=5
for i in range(1,10):
    if i<=row:
        star=i
    else:
        star=2*row-i  
    space=row-star
    line=" "*space+star*"*"      
    print(line)



for i in range(1,6):
    for j in range(i):
        print("*",end=" ")
    print()    