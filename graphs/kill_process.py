from collections import defaultdict
# Kill Process Function


def dfs(adj_list, results,  kill):
    results.append(kill)
    for v in adj_list[kill]:
        dfs(adj_list, results, v)


def killProcess(pid, ppid, kill):
    adj_list = defaultdict(list)
    for i in range(len(ppid)):
        if ppid[i] == 0:
            continue
        adj_list[ppid[i]].append(pid[i])
    results = []
    dfs(adj_list, results, kill)
    return results


print(killProcess([25, 3, 7, 4, 6, 10, 5, 8, 1, 9, 2],
                  [7, 7, 6, 7, 0, 5, 8, 6, 9, 8, 9],
                  8))
