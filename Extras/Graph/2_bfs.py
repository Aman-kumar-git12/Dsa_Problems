# link : https://my.newtonschool.co/playground/code/rfrgp2riw1ox
from collections import deque
def bfsOfGraph(n, edges, src):
    adjlist = [[]for i in range(n)]

    for s, d in edges:
        adjlist[s].append(d)
        adjlist[d].append(s)

    q = deque([src])
    result = []
    visited = [False] * n 

    while q:
        popnode = q.popleft()
        final.append(popnode)
        visited[popnode] = True 

        for nei in adjlist[popnode]:
            if not visited[nei]:
                q.append(nei)

    return result