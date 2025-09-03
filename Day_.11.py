#
class Element:
    def majority_element(self, nums):
        candidate = None
        count = 0
        for num in nums:
            if count == 0:
                candidate = num  # <-- Missing in your version!
            if num == candidate:
                count += 1
            else:
                count -= 1
        return candidate

s1 = Element()
print(s1.majority_element([1, 3, 3, 4, 44, 4, 4, 4])) 


    
