# Question : Find Minimum in Rotated Sorted Array
# link : https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

# old method 
def findMin(self, nums: List[int]) -> int:
    start  , end = 0 , len(nums) -1 
    
    n = len(nums)
    while start <= end :
        if nums[start] <= nums[end]:
            return nums[start]
        
        mid = end - (end -start)//2 
        prev = (mid + 1) % n
        next = (mid + n -1 )% n 

        if nums[mid] <= nums[prev] and nums[mid] <= nums[next]:
            return nums[mid] 
        elif nums[start] <= nums[mid]:
            start = mid + 1 
        elif nums[end] >= nums[mid]:
            end = mid -1 

    return -1 

# new method 

def findMin(self, nums: List[int]) -> int:
    start, end = 0, len(nums) - 1
    while start < end:
        mid = start + (end - start) // 2
        if nums[mid] > nums[end]:
            start = mid + 1
        else:
            end = mid

    return nums[start]
