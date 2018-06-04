class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 1
        ans = []
        for cur in digits[::-1]:
            sum = cur + carry
            ans.insert(0, sum % 10)
            carry = sum // 10
        if carry != 0:
            ans.insert(0, carry)
        return ans
