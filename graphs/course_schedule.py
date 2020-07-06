# https://leetcode.com/problems/course-schedule/

import collections


class Solution:
    def canFinish(self, numCourses, prerequisites):
        # edge case
        if not prerequisites:
            return True

        adj_list = collections.defaultdict(list)
        for u, v in prerequisites:
            adj_list[v].append(u)

        visited = [False] * numCourses
        recurse_stack = [False] * numCourses

        for v in list(adj_list):
            if not visited[v]:
                if hasCycle(adj_list, v, visited):
                    return False
        return True


def hasCycle(adj_list, v, visited):

    if visited[v] == "visited":
        return False

    if visited[v] == "visiting":
        return True

    visited[v] = "visiting"

    for e in adj_list[v]:
        if hasCycle(adj_list, e, visited):
            return True

    visited[v] = "visited"
    return False
