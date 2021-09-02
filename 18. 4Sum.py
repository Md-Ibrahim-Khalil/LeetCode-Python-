# Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

# 0 <= a, b, c, d < n
# a, b, c, and d are distinct.
# nums[a] + nums[b] + nums[c] + nums[d] == target
# You may return the answer in any order.


# Example 1:

# Input: nums = [1,0,-1,0,-2,2], target = 0
# Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
# Example 2:

# Input: nums = [2,2,2,2,2], target = 8
# Output: [[2,2,2,2]]


# Constraints:

# 1 <= nums.length <= 200
# -109 <= nums[i] <= 109
# -109 <= target <= 109


# Solution in Python 3 (beats 100.00%) (48 ms) ( O(n³) ) (Asymptotic Analysis)

# Asymptotic Worst Case Analysis:
# For ease of analysis, we will assume that the input list is sorted since sorting only takes O(n log n) time. The worst case occurs if the target is equal to the sum of the four greatest elements in the list. This is because the search would have to continue until the very end to find the desired quadruplet (a,b,c,d). For example, a list of the form N = [1,2,3,4,5,6,7,8,9,10] with target = 34 would require a complete run through all iterations of the three nested for loops. Note that the reason that there are only three nested for loops even though we are looking for a quadruplet is because finding the triplet (a,b,c) determines a unique value of d which will lead to a sum of target. Thus, we only need to search for triplets (a,b,c) such that target - (a+b+c) is in the original list.

# Observe that in the worst case, there is only one valid solution and that is found by adding the last
# four (i.e. the largest four) elements of the input list. Specifically, the desired quadruplet will be ( N[n-4], N[n-3], N[n-2], N[n-1] ),
# where N is the sorted input list and n is its length. The outer for loop will have to iterate from i = 1 to i = n-5 with a guarantee of
# failure in finding the desired quadruplet since the lowest element in the desired quadrauplet occurs at index n-4. For each iteration of
# the outer for loop, the remaining two nested inner for loops iterate through the remaining elements to the right of index i, looking at
# all possible ordered pairs (b,c) such that target - (a+b+c) is in the original list. This is an O(n²) search that occurs within each
# iteration of the outer for loop. It is guaranteed to fail in the worst case for outer loop indices from i = 1 to i = n-5. Thus in the
# worst case this algorithm is O(n³).


class Solution:
    def fourSum(self, n: List[int], t: int) -> List[List[int]]:
    	if not n: return []
    	n.sort()
    	L, N, S, M = len(n), {j:i for i,j in enumerate(n)}, set(), n[-1]
    	for i in range(L-3):
    		a = n[i]
    		if a + 3*M < t: continue
    		if 4*a > t: break
    		for j in range(i+1,L-2):
    			b = n[j]
    			if a + b + 2*M < t: continue
    			if a + 3*b > t: break
    			for k in range(j+1,L-1):
    				c = n[k]
    				d = t-(a+b+c)
    				if d > M: continue
    				if d < c: break
    				if d in N and N[d] > k: S.add((a,b,c,d))
    	return S
            
