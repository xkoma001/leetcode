from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        思路１:
        取出strs中每个字符串str,排序(按字母序),后去hash表d中查找对应字符串，
        若不存在该字符串，则增添到hash表中，并将str插入到strs中．
        hash结构(key, value), key为排序后的字符串,value为ｒtype的索引
        假设字符串最大长度为m
        时间消耗为O(nmlogm),空间消耗为T(mn)
        应该有巧妙的数据结构，这样做很有可能超时
        思路2:
        可以用数(0-26)映射对应的英文字符(a-z)出现次数,hash表d(key, value),
        (2, 1, 3) -> ('baaccc')
        假设最长的字符串为m
        时间消耗为O(nm),空间消耗为T(mn)
        """

        rv, d, index = [], dict(), 0
        for s in strs:
            r = ''.join(sorted(list(s)))
            if r not in d:
                d[r] = index
                index += 1
                rv.append([])
            rv[d[r]].append(s)

        return rv

    def groupAnagrams2(self, strs):
        d = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for ch in s:
                count[ord(ch)-ord('a')] += 1
            d[tuple(count)].append(s)

        return list(d.values())

if __name__ == '__main__':
    s = Solution()
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(s.groupAnagrams(strs))
    print(s.groupAnagrams2(strs))
