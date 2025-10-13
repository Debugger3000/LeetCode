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



# actual binary search code...
def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1  # search boundaries

        while left <= right:
            mid = (left + right) // 2   # find the middle index

            if nums[mid] == target:
                return mid               # found it!
            elif nums[mid] < target:
                left = mid + 1           # search the right half
            else:
                right = mid - 1          # search the left half

        return -1  # not found


# General Binary Search algo
# Two pointers 
# Time Complexity : O (n) - constant time and not log n :(
