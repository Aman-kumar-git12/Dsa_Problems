# Question : Alien Dictionary
# link : https://www.geeksforgeeks.org/problems/alien-dictionary/1


def findOrder(self, words):
    edges = []
    
    for i in range(1 , len(words)):
        s1 = words[i-1]
        s2 = words[i]
        min_len = min(len(s1) , len(s2))
        
        if len(s1) > len(s2) and s1[:min_len] == s2[:min_len]:
            return ""
        
        pointer = 0 
        while pointer < len(s1) and pointer < len(s2):
            if s1[pointer] !=  s2[pointer]:
                edges.append([s1[pointer] , s2[pointer]])
                break 
            else:
                pointer +=1
        
    
    set_list = set()
    for words in words:
        for word in words:
            set_list.add(word)
            
    adjlist = {char : [] for char in set_list}
    indegree = {char : 0 for char in set_list}
    
        
    
    for s , d in edges:
        
        adjlist[s].append(d)
        indegree[d]+=1
    
    
    
    import heapq
    heap =[]
    for i in indegree:
        if indegree[i]==0:
            heapq.heappush(heap , i)
    
    ans = []
        
    while heap:
        popnode = heapq.heappop(heap)
        ans.append(popnode)
        for nei in adjlist[popnode]:
            indegree[nei]-=1 
            if indegree[nei]== 0 :
                heapq.heappush(heap , nei)
    
    if len(ans) == len(set_list):
        return "".join(ans) 
    return ""
                
                
            
    
    
    
        
        
            
        # code here
        