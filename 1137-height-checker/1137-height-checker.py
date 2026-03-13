class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        nums = sorted(heights)
        count = 0

        for i in range(len(nums)):
            if heights[i] != nums[i]:
                count += 1

        return count
        