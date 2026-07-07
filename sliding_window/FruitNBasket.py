# Question :  Fruit Into Baskets
# link : https://leetcode.com/problems/fruit-into-baskets/description/

def totalFruit(self, s: List[int]) -> int:

    i , j = 0 , 0 
    n = len(s)
    map  = {}
    maxlength , count = 0 , 0 

    while j < n :
        if str(s[j]) not in map:
            map[str(s[j])] =1 
            count+= 1
        else : 
            map[str(s[j])] +=1 
            count+= 1

        if len(map) <  2:
            j+=1
        elif len(map) == 2:
            maxlength = max(count , maxlength)
            j+=1
        
        elif len(map) >  2:
            while len(map) > 2:
                map[str(s[i])]-=1
                count-= 1
                if map[str(s[i])] ==0:
                    del map[str(s[i])]
                i+=1 
            j+=1 
    if len(map) == 1 :
        return len(s)
    return maxlength