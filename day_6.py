class Stack:
  
    def number(self, lst):
        stack = []
        for i in lst:
            if i % 5 == 0:
                stack.append(i)
        return stack

  
    def number_2(self, lst_2):
        stack = []
        for i in lst_2:
            if i == '+':
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(num1 + num2)
            elif i == '*':
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(num1 * num2)
            else:
                stack.append(int(i))
        return stack[0]  



s1 = Stack()

print(s1.number([5, 515, 20, 30, 23, 11]))     
print(s1.number_2(['2', '1', '+', '3', '*']))  