# Question :  Bellman-Ford Algorithm
# link : https://www.geeksforgeeks.org/problems/distance-from-the-source-bellman-ford-algorithm/1
def bellmanFord(self, V, edges, src):

    distance = [100000000] * V 
        
    distance[src] = 0
    for i in range(V-1):
        for s , d , w in edges:
            if distance[s] !=100000000 and distance[s] + w < distance[d]:
                distance[d] = distance[s] + w


    for s , d , w in edges:
        if distance[s] != 100000000 and distance[s] + w < distance[d]:
            return [-1]
            
    return distance