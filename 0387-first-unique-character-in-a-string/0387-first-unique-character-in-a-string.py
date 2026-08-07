class Solution:
    def firstUniqChar(self, s: str) -> int:
        dic = {}
        for ch in s:
            dic[ch] = dic.get(ch, 0) + 1

        # for key, val in dic.items():
        #     if val == 1:
        #         return res
        #     res += 1

        for i, ch in enumerate(s):
            if dic[ch] == 1:
                return i

        return -1