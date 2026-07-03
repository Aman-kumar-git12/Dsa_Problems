# Question : Search in Rotated Sorted Array
# link : https://leetcode.com/problems/search-in-rotated-sorted-array/description/



def search(self, nums: List[int], target: int) -> int:
    start , end = 0 , len(nums)-1 
    n = len(nums)
    def binary(arr , start , end):
        
        while start <= end:
            mid = end - (end - start)//2
            if nums[mid] == target:
                return mid 
            elif target > arr[mid]:
                start = mid +1 
            else:
                end = mid - 1 
        return -1 

    

    def findmin(arr , start , end):
        
        while start <= end:
            if nums[start] <= nums[end]:
                return start

            mid = end - (end- start)//2
            next = (mid + 1 ) % n 
            prev = (mid + n - 1 )% n 

            if nums[mid] <= nums[prev] and nums[mid] <= nums[next]:
                return mid
            elif nums[start] <= nums[mid]:
                start = mid + 1 
            elif nums[mid] <= nums[end]:
                end = mid -1 
        return -1 
    
    minindex = findmin(nums ,start , end )

    
    if binary(nums , 0 , minindex -1) != -1:
        return binary(nums , 0 , minindex-1)
    elif binary(nums , minindex, len(nums)-1) != -1 :
        return binary(nums , minindex, len(nums)-1)
    else:
        return -1

    