# Question : Count Occurences of Anagram
# link : https://www.geeksforgeeks.org/problems/count-occurences-of-anagrams5839/1


def search(self,pattern, string):
    
    n=len(string)
    start=0
    end=0
    d=dict()
    ans=0
    k=len(pattern)
    for i in pattern:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    count=len(d)
    
    while end<n:
        if string[end] in d:
            d[string[end]]-=1
            if d[string[end]] == 0:
                count-=1
        if end-start+1 <k:
            end+=1
        elif end-start+1 == k:
            if count==0:
                ans+=1
            if string[start] in d :
                if d[string[start]] == 0 :
                    count+=1
                d[string[start]]+=1
                
            start+=1
            end+=1
    return ans