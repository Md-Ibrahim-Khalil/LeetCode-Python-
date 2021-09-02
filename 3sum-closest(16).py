# 16. 3Sum Closest

# Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

# Return the sum of the three integers.

# You may assume that each input would have exactly one solution.

 

# Example 1:

# Input: nums = [-1,2,1,-4], target = 1
# Output: 2
# Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
# Example 2:

# Input: nums = [0,0,0], target = 1
# Output: 0
 

# Constraints:

# 3 <= nums.length <= 1000
# -1000 <= nums[i] <= 1000
# -104 <= target <= 104

# class Solution:
    # def threeSumClosest(self, nums: List[int], target: int) -> int:
    
        nums.sort()
        n = len(nums)
        closest = -1
        diff = float("inf")
        
        for i in range(n-2):
            start = i + 1
            end = n - 1
            
            while start < end:
                curr_sum = nums[i] + nums[start] + nums[end]
                
            if curr_sum == target:
                return target
                
            if abs(curr_sum - targert) < diff:
                diff = abs(curr_sum - target)
                closest = curr_sum
                
            if curr_sum < target:
                start += 1
            else: 
                end -= 1
            
            return closest
