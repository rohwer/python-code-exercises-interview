# leetcode.com/problems/two-sum
# 1. in their list

# Given an array of integers,
# return indices of the two numbers
# such that they add up to a specific target.

# You may assume that each input would have
# exactly one solution,

# and you may not use
# the same element twice. (e.g. 2 + 2 = 4)

# Example
# Given nums = [2, 7, 11, 15], target = 9

# Because numes[0] + nums[1] = 2 + 7 = 9
# return [0, 1]

nums = [2,7,11,15]
target = 9

# Brute
def adder(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                print(f"Found: {i} and {j}")
                return
    else:
        print("None found")

# Pretty
def pretty(nums, target):
    h = {}
    for index, number in enumerate(nums):
        n = target - number
        if n not in h:
            h[number] = index
        else:
            print(f"Found: {h[n]} and {index}")            
            return

# Javascript solution is interesting to contrast
# var twoSum = function(nums, target) {
#     let map = new Map;
#     for (var i=0; i < nums.length; i++) {
#         let n = target - nums[i];
#         if (map.has(n)) {
#            return [map.get(n), i]
#         }
#         map.set(nums[i], i);
#     }
# }


if __name__ == "__main__":
    # adder(nums, target)
    pretty(nums, target)
            

    
