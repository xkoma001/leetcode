class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        m_len = len(height)
        left, right = 0, m_len-1
        res = 0
        max_left, max_right = 0, 0

        while left <= right:
            if height[left] <= height[right]:
                if max_left < height[left]:
                    max_left = height[left]
                else:
                    res += max_left-height[left]
                left += 1
            else:
                if max_right < height[right]:
                    max_right = height[right]
                else:
                    res += max_right-height[right]
                right -= 1
        return res

    def trap2(self, height):
        m_len = len(height)
        i, stack = 0, []
        totals = 0
        while i < m_len:
            if not stack or height[i] <= height[stack[-1]]:
                stack.append(i)
                i += 1
            else:
                bar = stack.pop()
                totals += (min(height[i], height[stack[-1]])-height[bar])*(i-stack[-1]-1) if len(stack) != 0 else 0

        return totals
