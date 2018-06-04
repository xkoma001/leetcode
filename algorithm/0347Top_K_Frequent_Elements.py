class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        def increment_obj(nums, i, obj):
            if nums[i][1] > obj[1]:
                return False
            nums[i] = obj
            while i != 1 and nums[i][1] > nums[i//2][1]:
                nums[i], nums[i//2] = nums[i//2], nums[i]
                nums_hash[nums[i][0]] = i
                nums_hash[nums[i//2][0]] = i//2
                i = i // 2
            return

        def add_val(nums, obj):
            size = len(nums) - 1
            size += 1
            nums.append(obj)
            increment_obj(nums, size, obj)

        def max_heap(nums, i, size):
            l, r = i*2, i*2+1
            largest = i
            if l <= size and nums[i][1] < nums[l][1]:
                largest = l
            if r <= size and nums[largest][1] < nums[r][1]:
                largest = r
            if largest != i:
                nums[i], nums[largest] = nums[largest], nums[i]
                max_heap(nums, largest, size)
            return

        nums_hash = dict()
        heap_nums = [(0, 0)]
        ans, size = [], 0

        for num in nums:
            if num not in nums_hash:
                size += 1
                nums_hash[num] = size
                add_val(heap_nums, (num, 1))
            else:
                i = nums_hash[num]
                increment_obj(heap_nums, i, (num, heap_nums[i][1]+1))

        size = len(heap_nums)-1
        for _ in range(k-1):
            ans.append(heap_nums[1][0])
            heap_nums[1] = heap_nums[size]
            size -= 1
            max_heap(heap_nums, 1, size)
        ans.append(heap_nums[1][0])
        return ans

    def topKFrequent2(self, nums, k):
        from collections import defaultdict
        ans = []
        cnt = defaultdict(int)
        n = len(nums)
        bucket = [[] for _ in range(n+1)]
        for num in nums:
            cnt[num] += 1
        for key in cnt.keys():
            bucket[cnt[key]].append(key)

        kind = 0
        for i in range(n, -1, -1):
            for num in bucket[i]:
                ans.append(num)
                kind += 1
                if kind == k:
                    return ans
