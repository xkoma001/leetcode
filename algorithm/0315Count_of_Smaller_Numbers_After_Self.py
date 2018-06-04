class Solution:
    def countSmaller(self, nums):
        ans = [0]*len(nums)

        def merge_sort(em):
            if not em or len(em) == 1:
                return em
            half = len(em) // 2
            left, right = merge_sort(em[:half]), merge_sort(em[half:])
            rv = []
            m, n = len(left), len(right)
            i = j = 0

            while i < m or j < n:
                if j == n or i < m and left[i][1] <= right[j][1]:
                    ans[left[i][0]] += j
                    rv.append(left[i])
                    i += 1
                else:
                    rv.append(right[j])
                    j += 1
            return rv

        em = list(enumerate(nums))
        merge_sort(em)
        return ans

    def countSmaller2(self, nums):
        class Node:
            def __init__(self, val):
                self.val = val
                self.count = 0
                self.smaller = 0
                self.left = None
                self.right = None

        def insert(node, val):
            total = 0
            while node.val != val:
                if node.val > val:
                    node.smaller += 1
                    if node.left is None:
                        node.left = Node(val)
                    node = node.left
                else:
                    total += node.smaller+node.count
                    if node.right is None:
                        node.right = Node(val)
                    node = node.right
            node.count += 1
            return node.smaller+total

        ans = []
        n = len(nums)
        if n == 0:
            return ans

        root = Node(nums[-1])
        for num in nums[::-1]:
            ans.append(insert(root, num))
        return ans[::-1]

if __name__ == '__main__':
    s = Solution()
    vals = [5, 2, 6, 1]
    print(s.countSmaller2(vals))