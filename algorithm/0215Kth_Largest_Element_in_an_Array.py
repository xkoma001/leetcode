class Heap:
    def max_heap(self, nums, i, size):
        l, r = i*2, i*2+1
        largest = i
        if l <= size and nums[l] > nums[i]:
            largest = l
        if r <= size and nums[r] > nums[largest]:
            largest = r
        if largest != i:
            nums[largest], nums[i] = nums[i], nums[largest]
            self.max_heap(nums, largest, size)

    def build_max_heap(self, nums):
        nums.insert(0, 0)
        size = len(nums)-1
        for j in range(size//2, 0, -1):
            self.max_heap(nums, j, size)
        return nums

    def sort_heap(self, nums):
        nums = self.build_max_heap(nums)
        size = len(nums)-1
        new_nums = []
        while size > 0:
            new_nums.append(nums[1])
            nums[1] = nums[size]
            size -= 1
            self.max_heap(nums, 1, size)
        return new_nums


class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k <= 0 or not nums:
            return -1
        heap = Heap()
        nums = heap.build_max_heap(nums)
        size = len(nums)-1
        while k > 1:
            nums[1] = nums[size]
            size -= 1
            heap.max_heap(nums, 1, size)
            k -= 1
        return nums[1]

    def findKthLargest2(self, nums, k):
        nums.sort(reverse=True)
        return nums[k-1]

    def findKthLargest3(self, nums, k):
        n = len(nums)-1
        l, h = 0, n

        def partion(low, high):
            pivot = nums[low]
            while low < high:
                while nums[high] <= pivot and low < high:
                    high -= 1
                if high != low:
                    nums[low] = nums[high]
                while nums[low] > pivot and low < high:
                    low += 1
                if low != high:
                    nums[high] = nums[low]

            nums[low] = pivot
            return low

        while True:
            rv = partion(l, h)
            if rv == k-1:
                break
            elif rv < k-1:
                l = rv+1
            else:
                h = rv-1
        return nums[rv]

