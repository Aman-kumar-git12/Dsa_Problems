# Question : Longest Substring with K Uniques
# link : https://www.geeksforgeeks.org/problems/longest-k-unique-characters-substring0853/1




def longestKSubstr(self, s, k):
    # code here
    
    map = {}
    i , j = 0 , 0 
    n = len(s)
    length = 0 
    maxlength = -1 
    count = 0 
    while j < n :
        # calculation 
        if s[j] not in map :
            map[s[j]] = 1 
            count+=1 
        else :
            map[s[j]]  +=1
            count+=1 
        
        # if sum != k 
        if len(map) < k:
            j+=1 
            
        # if sum == k   
        elif len(map)== k :
            # calculation ans 
            maxlength = max(maxlength ,count)
            j+=1 
        else:
            # remove calculation 
            while len(map) > k:
                map[s[i]] -=1
                count-=1 
                if map[s[i]] == 0:
                    del map[s[i]]
                # slide window 
                i+=1
            j+=1 
    return maxlength