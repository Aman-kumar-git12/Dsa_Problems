# Quesiton : Minimum Window Substring
# link: https://leetcode.com/problems/minimum-window-substring/description/



def minWindow(self, s: str, t: str) -> str:
    map = {}
    for i in t:
        if i not in map:
            map[i] = 1 
        else :
            map[i] += 1
    
    i , j , n = 0 , 0 , len(s)
    minlength = len(s)+1
    storage = (-1 , -1)
    length = len(map)

    while j < n :
        if s[j] in map:
            map[s[j]] -= 1
            if map[s[j]] == 0 :
                length -= 1 
            
        if length > 0:
            j+=1    
        elif length == 0:

            while length ==0 :
                if j - i + 1 < minlength:
                    minlength = j - i + 1
                    storage = (i , j)
                
                if s[i] in map :
                    map[s[i]] +=1 
                    if map[s[i]] > 0 :
                        length += 1 
                
                i+=1 
            j+=1
    if storage[1] == -1:
        return ""
    return s[storage[0]:storage[1]+1]
            