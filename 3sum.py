# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

 
# Example 1:

# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Example 2:

# Input: nums = []
# Output: []
# Example 3:

# Input: nums = [0]
# Output: []
 

# Constraints:

# 0 <= nums.length <= 3000
# -105 <= nums[i] <= 105




# Python | Using 2 Pointers | O(N^2) Time | O(1) Space



class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3: return []
        
        def find_triplets(target, left, triplets):
            right = len(nums)-1
            while left < right:
                if nums[left]+nums[right] == target:
                    triplets.append([-target, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                    while left < right and nums[right] == nums[right+1]:
                        right -= 1
                
                elif nums[left] + nums[right] > target:
                    right -= 1
                else:
                    left += 1
        
        nums.sort()
        triplets = []
        for index in range(len(nums)):
            if index > 0 and nums[index] == nums[index-1]:
                continue
            find_triplets(-nums[index], index+1, triplets)
        return triplets
            