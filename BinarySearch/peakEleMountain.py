# Question : Peak Index in a Mountain Array
# link : https://leetcode.com/problems/peak-index-in-a-mountain-array/description/

def peakIndexInMountainArray(self, nums: List[int]) -> int:
    start , end  = 0 , len(nums)-1
    if len(nums)== 1:
        return 0
    while start <= end:
        mid = end - (end- start)//2
        if mid < len(nums)-1 and mid > 0 :

            if nums[mid] >= nums[mid-1] and nums[mid] >= nums[mid+1]:
                return mid
            elif nums[mid+1]  > nums[mid]:
                start  = mid + 1
            elif nums[mid-1] >  nums[mid ]:
                end = mid -1
        else:
            if mid == 0 :
                if nums[mid] > nums[mid + 1]:
                    return mid
                else :
                    return mid + 1

            else:
                if nums[mid] > nums[mid-1]:
                    return mid
                else:
                    return mid -1 
    return -1
    