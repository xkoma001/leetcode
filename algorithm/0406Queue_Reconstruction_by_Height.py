class Solution:
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        if not people:
            return people

        people.sort(key=lambda x: x[0])
        ans = []

        cur_max = people[-1][0]
        while people:
            cur_em = []
            while people and people[-1][0] == cur_max:
                cur_em.append(people.pop())

            cur_em.sort(key=lambda x: x[1])
            if people:
                cur_max = people[-1][0]
            for em in cur_em:
                ans.insert(em[1], em)
        return ans
