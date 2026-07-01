# Question : Find Smallest Letter Greater Than Target
# link : https://leetcode.com/problems/find-smallest-letter-greater-than-target/description/

def nextGreatestLetter(self, letters: List[str], target: str) -> str:
    start , end = 0 , len(letters)-1
    res = '#'
    while start <= end:
        mid = start + (end - start)//2
        if letters[mid] <= target:
            start = mid + 1
        else :
            res = letters[mid]
            end = mid -1 
    if res == '#':
        return letters[0]
    return res