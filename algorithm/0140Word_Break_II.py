class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """

        def depth(s, wordDict, memo):
            if not s:
                return []
            if s in memo:
                return memo[s]

            res = []
            for word in wordDict:
                if not s.startswith(word):
                    continue
                if len(word) == len(s):
                    res.append(s)
                else:
                    for rest in depth(s[len(word):], wordDict, memo):
                        res.append(word + ' ' + rest)
            memo[s] = res
            return memo[s]

        memo = {}
        return depth(s, wordDict, memo)

