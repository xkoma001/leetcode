class Solution:
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        class task:
            def __init__(self, name):
                self.name = name
                self.next = None
        from collections import defaultdict
        total_task = len(tasks)
        bucket = [[] for _ in range(total_task+1)]
        cnt = defaultdict(int)
        for sub_task in tasks:
            cnt[sub_task] += 1

        for key, val in cnt.items():
            bucket[val].append(key)
        tail = dummy = task('0')
        node_len = 0
        idle_tasks = defaultdict(int)

        def get_one_task():
            nonlocal tail
            nonlocal n
            nonlocal node_len

            node_len += 1
            for i in range(total_task, 0, -1):
                for sub in bucket[i]:
                    if idle_tasks[sub] == 0:
                        idle_tasks[sub] = 1
                        cur_node = task(sub)
                        bucket[i].remove(sub)
                        bucket[i-1].append(sub)
                        tail.next = cur_node
                        tail = tail.next
                        if node_len == n + 1:
                            before = dummy.next
                            idle_tasks[before.name] = 0
                            dummy.next = dummy.next.next
                            if dummy.next is None:
                                tail = dummy
                            node_len -= 1
                        return sub
            cur_node = task('0')
            tail.next = cur_node
            tail = tail.next
            if node_len == n+1:
                before = dummy.next
                idle_tasks[before.name] = 0
                dummy.next = dummy.next.next
                if dummy.next is None:
                    tail = dummy
                node_len -= 1
            return None

        step, fin_task = 0, 0
        while fin_task < total_task:
            cur_task = get_one_task()
            if cur_task is not None:
                fin_task += 1
            step += 1
        return step

    def leastInterval2(self, tasks, n):
        from queue import PriorityQueue
        from collections import defaultdict
        task_queue = PriorityQueue()
        counts = defaultdict(int)
        cycle = n+1
        total_times = 0

        for sub in tasks:
            counts[sub] -= 1
        for ch, fre in counts.items():
            task_queue.put((fre, ch))

        while not task_queue.empty():
            times = 0
            tmp = []
            for _ in range(cycle):
                if not task_queue.empty():
                    cur = task_queue.get()
                    tmp.append(cur)
                    times += 1
            for cur in tmp:
                fre = cur[0]
                if fre < -1:
                    task_queue.put((fre+1, cur[1]))
            total_times += cycle if not task_queue.empty() else times
        return total_times

    def leastInterval3(self, tasks, n):
        from collections import defaultdict
        counts = defaultdict(int)
        for sub in tasks:
            counts[sub] += 1
        task_seq = sorted(list(counts.values()))
        i = len(task_seq)-1
        j = i
        while j >= 0 and task_seq[j] == task_seq[i]:
            j -= 1
        return max(len(tasks), (task_seq[i]-1)*(n+1)+i-j)

if __name__ == '__main__':
    s = Solution()
    tasks, n = ["A","A","A","B","B","B"], 2
    print(s.leastInterval(tasks, n))
