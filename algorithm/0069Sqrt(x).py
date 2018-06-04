class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 1:
            return 1

        low, high = 1, x
        while low < high:
            mid = (low + high) // 2
            rel = mid * mid
            if rel == x:
                return mid
            elif rel > x:
                high = mid
            else:
                low = mid + 1
        return low-1
