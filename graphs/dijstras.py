'''
Dijstra's Algorithm Implementation - relies on BFS and a priority queue 
to keep track of edges with min_distance. 
Running time with priority queue O(v + ElogE)
'''
import heapq

# assume that input graph is an adjacency list as a nested dictionary


def dijstras(graph, start):
    distances = {}
    for v in graph.keys():
        distances[v] = float('inf')
    distances[start] = 0
    pq = [(distances[start], start)]

    while pq:
        cur_distance, u = heapq.heappop(pq)
        if cur_distance > distances[u]:
            continue
        for v, dist in graph[u].items():
            if cur_distance + dist < distances[v]:
                distances[v] = cur_distance + dist
                heapq.heappush(pq, (dist, v))
    return distances


graph = {
    'A': {'B': 1, 'C': 2},
    'B': {'C': 4},
    'C': {'D': 2},
    'D': {}
}

print(dijstras(graph, 'A'))
