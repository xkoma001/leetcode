class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """

        n = len(gas)
        i, cur_gas = 0, 0
        while i < n:
            j = i
            cur_gas = 0
            while True:
                cur_gas += gas[j] - cost[j]
                if cur_gas < 0:
                    break
                next = (j+1) % n
                if next == i:
                    return i
                j = next
            i += 1
        return -1

    def canCompleteCircuit2(self, gas, cost):
        start, end = len(gas)-1, 0

        cur_gas = gas[start]-cost[start]
        while start != end:
            if cur_gas >= 0:
                cur_gas += gas[end]-cost[end]
                end += 1
            else:
                start -= 1
                cur_gas += gas[start]-cost[start]

        return start if cur_gas >= 0 else -1


