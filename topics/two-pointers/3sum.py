class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        out = []
        leng = len(nums)

        for i in range(leng):
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # skip duplicates after 1st index

            left,right = i+1, leng-1

            # stop looking for cur i, when pointers collide
            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    out.append([nums[i], nums[left], nums[right]])

                    # continue incre / decre for pointers, as same number could have more matches
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

        return out
        

        
