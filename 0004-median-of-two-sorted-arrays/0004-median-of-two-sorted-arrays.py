class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        merged = sorted(nums1+nums2)
        n = len(merged)
        if n % 2 == 0:
            return (merged[int(n/2)]+merged[int((n/2)-1)])/2.0
        return merged[n/2]


        