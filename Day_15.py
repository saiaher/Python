from typing import List

def longest_consecutive(nums: List[int]) -> int:
    num_set = set(nums)
    longest = 0

    for num in num_set:
        # Only start counting if it's the start of a sequence
        if num - 1 not in num_set:
            current = num
            streak = 1

            while current + 1 in num_set:
                current += 1
                streak += 1

            longest = max(longest, streak)

    return longest
print(longest_consecutive([100, 4, 200, 1, 3, 2]))   # Output: 4
print(longest_consecutive([0,3,7,2,5,8,4,6,0,1]))    # Output: 9
print(longest_consecutive([10, 5, 12, 3, 55, 4, 11]))# Output: 3
print(longest_consecutive([]))                      # Output: 0
