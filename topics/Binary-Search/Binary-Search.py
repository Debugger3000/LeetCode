class Solution:
    def search(self, nums: List[int], target: int) -> int:
        leng = len(nums)
        for i in range(leng):
            p1 = nums[i]
            p2 = nums[-(i+1)]
            
            if p1 == p2 and p1 == target:
                return i
            elif p1 == target:
                return i
            elif p2 == target:
                return leng - (i+1)
        return -1


# General Binary Search algo
# Two pointers 
# Time Complexity : O (n) - constant time and not log n :(
