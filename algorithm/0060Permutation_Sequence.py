class Solution:
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        seqs = [str(i) for i in range(1, n+1)]
        ans = []

        def permutation(seqs, cur_rel):
            nonlocal k
            if not seqs:
                k -= 1
                if k == 0:
                    ans.append(cur_rel)
                return

            if k > 0:
                for pos, val in enumerate(seqs):
                    permutation(seqs[:pos]+seqs[pos+1:], cur_rel+seqs[pos])
            return

        permutation(seqs, "")
        return ans[0]

    def getPermutation2(self, n, k):
        ans = ""
        seqs = [str(i) for i in range(1, n+1)]
        fac = [1] * n

        count = 1
        while count != n:
            fac[count] = fac[count-1] * count
            count += 1

        k = k-1
        while seqs:
            m = k // fac[n-1]
            ans += seqs[m]
            seqs = seqs[:m] + seqs[m+1:]
            k = k - m*fac[n-1]
            n -= 1
        return ans

if __name__ == '__main__':
    s = Solution()
    print(s.getPermutation(8, 17198))
    print(s.getPermutation2(8, 17198))
