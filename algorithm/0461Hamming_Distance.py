class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        z = x ^ y
        count = 0
        while z != 0:
            count += z & 1
            z = z >> 1
        return count
