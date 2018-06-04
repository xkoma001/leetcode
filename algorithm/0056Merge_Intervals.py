# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e


class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        ans = []
        intervals = sorted(intervals, key=lambda item: item.start)

        cur_interval = []
        for interval in intervals:
            if not cur_interval:
                cur_interval = interval
            elif cur_interval.end < interval.start:
                ans.append(cur_interval)
                cur_interval = interval
            else:
                cur_interval.end = interval.end if interval.end > cur_interval.end else cur_interval.end

        if cur_interval:
            ans.append(cur_interval)
        return ans
