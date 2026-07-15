# Quesiton : Course Schedule II
# link : https://leetcode.com/problems/course-schedule-ii/description/



def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
    import heapq

    adjlist = [[]for i in range(numCourses)]
    indegree = [0]* numCourses 
    for s , d in prerequisites:
        indegree[d]+=1
        adjlist[s].append(d)

    q = []
    for i in range(len(indegree)):
        if indegree[i]==0:
            heapq.heappush(q , i)
        
    stack = []

    while q :
        popnode = heapq.heappop(q)
        stack.append(popnode)
        for nei in adjlist[popnode]:
            indegree[nei]-=1
            if indegree[nei] ==0:
                heapq.heappush(q , nei)
    if len(stack) != numCourses:
        return []
    return stack[::-1]
    