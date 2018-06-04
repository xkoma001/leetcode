class Solution:
    def jump(self, nums):
        """
        time out
        :param nums:
        :return:
        """
        step, n = 0, len(nums)
        target = n-1

        while target != 0:
            for i in range(target):
                if i+nums[i] >= target:
                    target = i
                    step += 1
                    break
        return step

    def jump2(self, nums):
        """
        :param nums:
        :return:
        """

        farthest, cur_end = nums[0], nums[0]
        step, n = 0, len(nums)
        for i in range(1, n):
            farthest = max(farthest, nums[i]+i)
            if cur_end > n-1:
                step += 1
                break

            if i == cur_end:
                step += 1
                cur_end = farthest

        return step




        return jumps;
if __name__ == '__main__':
    s = Solution()
    a = [7,0,9,6,9,6,1,7,9,0,1,2,9,0,3]
    b = [0]
    print(s.jump(a))
    print(s.jump2(a))
    print(s.jump2(b))
