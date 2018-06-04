class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """

        from collections import defaultdict
        from collections import deque

        def make_dict(word_list):
            d = defaultdict(list)
            for w in word_list:
                if w != beginWord:
                    for i in range(len(w)):
                        s = w[:i] + '_' + w[i + 1:]
                        d[s] = d[s] + [w]
            return d

        queue = deque([(beginWord, 1, [beginWord])])
        layer = dict()
        d = make_dict(wordList + [beginWord])
        ladder = 0
        ans = []

        while queue:
            wd, size, path = queue.popleft()

            if wd not in layer:
                layer[wd] = size
            elif size != layer[wd]:
                continue
            if wd == endWord and size == layer[wd]:
                ans.append(path)
                ladder = size
                continue
            if ladder == 0 or size < ladder:
                for i in range(len(wd)):
                    for next_wd in d[wd[:i] + '_' + wd[i+1:]]:
                        if next_wd not in layer or size+1 == layer[next_wd]:
                            new_path = path[:] + [next_wd]
                            queue.append((next_wd, size + 1, new_path))
        return ans

if __name__ == '__main__':
    s = Solution()
    be, en = "red", "tax"
    wd_list = ["ted","tex","red","tax","tad","den","rex","pee"]
    print(s.findLadders(be, en, wd_list))
