class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        if not numCourses:
            return False
        queue = []
        totals = course_num = numCourses
        courses = [[] for _ in range(course_num)]
        has_used = [0]*course_num

        # init
        for pre in prerequisites:
            courses[pre[1]].append(pre[0])

        for i in range(course_num):
            if not courses[i]:
                queue.append(i)
                has_used[i] = 1

        while queue:
            fin = queue.pop(0)
            totals -= 1
            for i in range(course_num):
                if not has_used[i] and fin in courses[i]:
                    courses[i].remove(fin)
                    if not courses[i]:
                        queue.append(i)
                        has_used[i] = 1
        return True if totals == 0 else False

    def canFinish2(self, numCourses, prerequisites):
        def dfs_cycle(visited, on_path, courses, cur):
            if visited[cur]:
                return False
            visited[cur] = 1
            on_path[cur] = 1
            for neigh in courses[cur]:
                if on_path[neigh] or dfs_cycle(visited, on_path, courses, neigh):
                    return True
            on_path[cur] = 0
            return False

        courses = [set() for _ in range(numCourses)]
        has_visited = [0] * numCourses
        on_path = [0] * numCourses

        for pre in prerequisites:
            courses[pre[1]].add(pre[0])

        for i in range(numCourses):
            if not has_visited[i] and dfs_cycle(has_visited, on_path, courses, i):
                return False
        return True


