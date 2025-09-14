  #Write a function that returns the sum of the digits of a given number.
class Sum:
    def sum_of_all(self, numbers_list):
        total_sum = 0
        for number in numbers_list:
            number = abs(number) 
            while number > 0:
                total_sum += number % 10  
                number = number // 10  
        return total_sum

s = Sum()
print(s.sum_of_all([123, 456, 789]))  
print(s.sum_of_all([12, -34, 56]))    

             
