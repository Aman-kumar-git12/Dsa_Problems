# Question : Sort Array by Increasing Frequency
# link : https://leetcode.com/problems/sort-array-by-increasing-frequency/description/

def frequencySort(self, nums: List[int]) -> List[int]:
    map = {}
    for i in range(len(nums)):
        if nums[i] in map:
            map[nums[i]] += 1
        else:
            map[nums[i]] = 1 

    print(map)
    newmap = []
    for i in range(len(nums)):
        newmap.append((map[nums[i]] , nums[i])) 


    ans = []
    newmap.sort(key = lambda x  :( x[0] , -x[1]))
    for i in range(len(newmap)):
        ans.append(newmap[i][1])
    return ans 