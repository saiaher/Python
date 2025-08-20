sai=1,2,3,4
x=sai[0]
for i in sai[1:]:
    print(i)
    if i < x:
        x=i
return x  
