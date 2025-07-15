class Demo:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        return self.a+self.b
    
obj1 = Demo(5,2)
print(obj1.add())