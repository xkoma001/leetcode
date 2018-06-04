# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution:
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        ans = []
        new_interval = newInterval

        for i, interval in enumerate(intervals):
            if not new_interval:
                ans.append(interval)
                continue
            if new_interval.end < interval.start:
                ans.append(new_interval)
                ans.append(interval)
                new_interval = None
            elif new_interval.start > interval.end:
                ans.append(interval)
            else:
                new_interval = Interval(min(interval.start, new_interval.start), max(interval.end, new_interval.end))
        if new_interval:
            ans.append(new_interval)
        return ans
