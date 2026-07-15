# Question:  Course Schedule
# link: https://leetcode.com/problems/course-schedule/description/



def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
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

    if len(stack) == numCourses:
        return True 
    return False 
        
    