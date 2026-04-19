class Solution:
    def maxDistance(self, nums1, nums2):
        res = 0

        for i in range(len(nums1)):
            lo, hi = i, len(nums2) - 1
            
            while lo <= hi:
                mid = (lo + hi) // 2
                
                if nums2[mid] >= nums1[i]:
                    res = max(res, mid - i)
                    lo = mid + 1   # try to go further right
                else:
                    hi = mid - 1   # go left
        
        return res