class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        nums1 [1,2,3]
        nums2 [2,4]

        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m, n = len(nums1), len(nums2)
        if n < m:
            return self.findMedianSortedArrays(nums2, nums1)
        if n == 0:
            return False
        elif m == 0:
            if n % 2 == 0:
                return float((nums2[n//2-1]+nums2[n//2])/2)
            else:
                return float(nums2[n//2])

        low, high = 0, m
        half_len = (m+n+1) // 2
        while low <= high:
            i = (low+high) // 2
            j = half_len-i
            if i < m and nums2[j-1] > nums1[i]:
                low = i+1
            elif i > 0 and nums1[i-1] > nums2[j]:
                high = i-1
            else:
                if i == 0:
                    max_of_left = nums2[j-1]
                elif j == 0:
                    max_of_left = nums1[i-1]
                else:
                    max_of_left = max(nums1[i-1], nums2[j-1])

                if i == m:
                    min_of_right = nums2[j]
                elif j == n:
                    min_of_right = nums1[i]
                else:
                    min_of_right = min(nums1[i], nums2[j])

                if (m+n) % 2 == 0:
                    return float((max_of_left+min_of_right)/2)
                else:
                    return float(max_of_left)
