class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = {}

        for n in nums:
            count[n] = count.get(n, 0) + 1
        res = 0
        for key, values in count.items():
            res += values * (values - 1) // 2

        return res
        