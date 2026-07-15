# link : https://my.newtonschool.co/playground/code/1uzdnnid0q5l
def shortestDistance(n, edges, src,dst):
    adjlist = [[]for i in range(n)]
    for s, d in edges:
        adjlist[s].append(d)
        adjlist[d].append(s)

    q = deque([(src , 0)])
    result = []
    visited = [False] * n 

    while q:
        popnode , dist  = q.popleft()
        if popnode == dst:
            return dist
        result.append(popnode)
        visited[popnode] = True 

        for nei in adjlist[popnode]:
            if not visited[nei]:
                visited[nei] = True
                q.append((nei , dist+1))

    return -1
        