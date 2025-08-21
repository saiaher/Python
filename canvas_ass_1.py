row=5
for i in range(1,10):
    if i<=row:
        star=i
    else:
        star=2*row-i  
    space=row-star
    line=""*space+star*"*"      
    print(line)



word=input("enter your word:")
reverce_word=word[::-1]
print(reverce_word)