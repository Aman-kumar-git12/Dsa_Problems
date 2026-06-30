# Question : 153. Find Minimum in Rotated Sorted Array
# link : https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/

def findMin(self, nums: List[int]) -> int:
        start , end = 0 , len(nums)-1 
        while start <= end :

            mid = end - (end - start )//2

            if nums[mid] == nums[end]:
                return min(nums[start] , nums[end])
            elif nums[mid] < nums[start]:
                end = mid
            elif nums[mid] > nums[end]:
                start = mid
            else:
                return nums[start]

        