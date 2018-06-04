# Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b


class Solution:
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        from collections import defaultdict
        m_len = len(points)
        rel = 0
        if m_len <= 1:
            return m_len

        def gcd(x, y):
            if y == 0:
                return x
            return gcd(y, x%y)

        for i in range(m_len):
            same_lines = defaultdict(lambda: 0)
            over_lap, cur_max = 0, 0
            for j in range(i+1, m_len):
                x = points[i].x-points[j].x
                y = points[i].y-points[j].y
                if x == 0 and y == 0:
                    over_lap += 1
                    continue
                r = gcd(x, y)
                if r != 0:
                    x //= r
                    y //= r
                same_lines[(x, y)] += 1
                cur_max = max(cur_max, same_lines[(x, y)])
            rel = max(rel, cur_max+over_lap+1)

        return rel
