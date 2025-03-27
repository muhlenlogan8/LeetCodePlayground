"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]

Constraints:
* 2 <= nums.length <= 104
* -109 <= nums[i] <= 109
* -109 <= target <= 109
* Only one valid answer exists.

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
"""

"""
:type nums: List[int]
:type target: int
:rtype: List[int]
"""

# Solution with loops O(n^2)
class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

# Solution 2 using dictionary (hash maps) O(n)
"""
Create dictionary
Iterate through the list
Check if target - nums[i] is in the dictionary
If it is, return the indices of the two numbers
If it is not, add the number to the dictionary as {nums[i]: i} where nums[i] is the key and i is the value
"""
class Solution2(object):
    def twoSum(self, nums, target):
        dict = {}
        for i in range(len(nums)):
            if target - nums[i] in dict:
                return [dict[target - nums[i]], i]
            dict[nums[i]] = i

# Case1:
nums = [2,7,11,15]
target = 9
sol = Solution()
print(sol.twoSum(nums, target)) # Output: [0,1]
sol2 = Solution2()
print(sol2.twoSum(nums, target)) # Output: [0,1]