class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        count = {}

        for n in nums:
            count[n] = count.get(n, 0) + 1

        for key, value in count.items():
            if value % 2 != 0:
                return False

        return True
        