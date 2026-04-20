class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        n = len(colors) - 1
        dis = 0
        for i in range(len(colors)):
            if colors[0] != colors[i]:
                dis = max(dis, i)

            if colors[n] != colors[i]:
                dis = max(dis, n-i)

        return dis