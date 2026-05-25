class Solution:
    def minimumSwaps(self, nums: list[int]) -> int:
        l, r = 0, len(nums) - 1
        cnt = 0
        while l <= r:
            if nums[l] == 0 and nums[r] != 0:
                nums[l], nums[r] == nums[r], nums[l]
                l += 1
                r -= 1
                cnt += 1
            elif nums[l] == 0 and nums[r] == 0:
                r -= 1
            else:
                l += 1

        return cnt