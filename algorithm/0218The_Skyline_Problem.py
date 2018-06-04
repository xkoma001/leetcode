class Heap:
    def __init__(self, nums):
        self.nums = nums
        self.nums.insert(0, -1)
        self.size = len(self.nums)-1
        self.len = 0

    def top(self):
        if self.size < 1:
            return -1
        return self.nums[1]

    def pop(self):
        if self.size < 1:
            return

        if self.size == 1:
            self.size -= 1
            return

        self.nums[1] = self.nums[self.size]
        self.size -= 1
        self.max_heap(1)
        return


    def max_heap(self, i):
        l, r = i*2, i*2+1
        largest = i
        if l <= self.size and self.nums[l] > self.nums[i]:
            largest = l
        if r <= self.size and self.nums[r] > self.nums[largest]:
            largest = r
        if largest != i:
            self.nums[largest], self.nums[i] = self.nums[i], self.nums[largest]
            self.max_heap(largest)

    def remove(self, val):
        if self.size < 1:
            return
        target = self.size+1
        for i in range(1, self.size+1):
            if self.nums[i] == val:
                target = i
                break

        if target != self.size+1:
            if target != self.size:
                self.nums[target] = self.nums[self.size]
            self.size -= 1
            self.max_heap(target)
        return

    def add(self, val):
        self.size += 1
        if self.len < self.size:
            self.len += 1
            self.nums.append(val)
        else:
            self.nums[self.size] = val
        self.incre(self.size, val)
        return

    def incre(self, i, val):
        if self.nums[i] < val:
            return
        self.nums[i] = val

        while i != 1 and self.nums[i] > self.nums[i//2]:
            self.nums[i//2], self.nums[i] = self.nums[i], self.nums[i//2]
            i = i//2
        return


class Solution:
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        from functools import cmp_to_key

        height = []
        for (l, r, h) in buildings:
            height.append((l, -h))
            height.append((r, h))

        cmp = cmp_to_key(lambda a, b: a[0]-b[0] if a[0] != b[0] else a[1]-b[1])
        height.sort(key=cmp)

        pre = 0
        p_heap = Heap([])
        p_heap.add(0)

        ans = []
        from collections import defaultdict
        rms = defaultdict(int)

        for h in height:
            if h[1] < 0:
                p_heap.add(-h[1])
            else:
                rms[h[1]] += 1

            cur = p_heap.top()
            while rms[cur] != 0:
                rms[cur] -= 1
                p_heap.pop()
                cur = p_heap.top()

            if pre != cur:
                pre = cur
                ans.append((h[0], cur))
        return ans
