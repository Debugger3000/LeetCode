class Solution:
    def maxArea(self, height: List[int]) -> int:

        max_area = 0
        left = 0
        right = len(height)-1

        while left < right:
            left_val = height[left]
            right_val = height[right]
            
            area = (right - left) * min(left_val, right_val)

            if area > max_area:
                max_area = area

            if left_val < right_val:
                left += 1
            else:
                right -= 1
        return max_area

# Two pointers at each end

# TRICK: move pointer with lesser value towards middle of array...
