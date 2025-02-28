# https://leetcode.com/problems/median-of-two-sorted-arrays/description/
# use merge sort to find the median in two sorted array
# referred to the official solution

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        len1 = len(nums1)
        len2 = len(nums2)
        p1, p2 = 0, 0 # index of nums1 and nums2

        def get_min(p1, p2):
            """
            selects the smaller value from two sorted lists (nums1 and nums2) 
            based on the current index p1 and p2
            """
            if p1 == len1: # nums1 finished
                ans = nums2[p2]
                p2 += 1
                return ans, p1, p2
            elif p2 == len2: # nums2 finished
                ans = nums1[p1]
                p1 += 1
                return ans, p1, p2
            elif p1<len1 and p2<len2: # return smaller one and index++
                if nums1[p1] < nums2[p2]:
                    ans = nums1[p1]
                    p1 += 1
                    return ans, p1, p2
                else:
                    ans = nums2[p2]
                    p2 += 1
                    return ans, p1, p2

        if (len1 + len2) % 2 == 0: # median is avg of mid1 and mid2
            for i in range( (len1 + len2) // 2 - 1 ):
                temp, p1, p2 = get_min(p1, p2)
            mid1, p1, p2 = get_min(p1, p2)
            mid2, p1, p2 = get_min(p1, p2)
            return (mid1 + mid2) / 2.0
        else: # median is the middle one
            for i in range( (len1 + len2) // 2 ):
                temp, p1, p2 = get_min(p1, p2)
            temp, p1, p2 = get_min(p1, p2)
            return temp