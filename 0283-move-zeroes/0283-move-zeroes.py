class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        i = 0
        l = len(nums)

        while i < l:
            if nums[i] == 0:
                del nums[i]
                nums.append(0)
                l -= 1
            else:
                i += 1