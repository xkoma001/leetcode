class Solution:
    def maxArea(self, height):
        """
        思路１:
        自己只能想到暴力的O(n^2)
        思路2:
        双指针法
        面积由宽度和最短高度决定
        从最宽的距离向最短的距离移动的过程，如果两条边的高度比原先的还小，则直接继续缩短距离直到为0
        时间复杂度O(n)
        :type height: List[int]
        :rtype: int
        """
        i, j = 0, len(height)-1
        max_area = 0
        while i < j:
            h = min(height[i], height[j])
            new_area = h * (j-i)
            max_area = new_area if new_area > max_area else max_area
            while i < j and height[i] <= h:
                i += 1
            while i < j and height[j] <= h:
                j -= 1

        return max_area

if __name__ == '__main__':
    s = Solution()
    data = [1,2, 4, 3]
    print(s.maxArea(data))