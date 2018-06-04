class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """

        i, j = 0, 0
        total = 0
        while j < n:
            if i < m:
                while i < m and nums1[total] < nums2[j]:
                    i += 1
                    total += 1
                if i < m:
                    tmp = nums2[j]
                    for k in range(total, total+m-i+1):
                        nums1[k], tmp = tmp, nums1[k]
                    total += 1
                    j += 1
            else:
                nums1[total] = nums2[j]
                total += 1
                j += 1
        return

    def merge2(self, nums1, m, nums2, n):
        i, j, k = m-1, n-1, m+n-1

        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
        while j >= 0:
            nums1[j] = nums2[j]
            j -= 1
        return

