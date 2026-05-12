class Solution:

    def searchRange(self, nums: List[int], target: int) -> List[int]:

        occ = []
        low = 0
        high = len(nums) - 1

        while low <= high:

            mid = low + ((high - low) // 2)

            if nums[mid] == target:
                occ.insert(0, mid)
                high = mid - 1

            elif nums[mid] < target:
                low = mid + 1

            else:
                high = mid - 1

        low = 0
        high = len(nums) - 1

        while low <= high:

            mid = low + ((high - low) // 2)

            if nums[mid] == target:
                occ.append(mid)
                low = mid + 1

            elif nums[mid] < target:
                low = mid + 1

            else:
                high = mid - 1

        if len(occ) == 0:
            return [-1, -1]

        return [occ[0], occ[-1]]