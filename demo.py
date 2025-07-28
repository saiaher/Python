def sai(lst,target):
    Index = {}
    for i, num in enumerate(lst):
        if target - num in Index:
            return [Index[target-num],i]
        Index[num]=i
print(sai([1,2,2,2,2,3,4,4566,7,756,7,75,67567,56,56,7,567,57,5,45,5,5,55676767545,6,65,65,6,56,65,6,6,565,76,57,67745,7,56767],6)) 
  

