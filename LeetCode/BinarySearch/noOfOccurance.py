def noOfOccurance(self, nums: List[int], target: int) -> List[int]:
        first = -1
        last = -1 
        start , end = 0 , len(nums) -1 
        while start <= end:
            mid = end - (end - start)//2
            if nums[mid] == target:
                first = mid 
                end = mid - 1 
            elif nums[mid] < target:
                start = mid + 1 
            else:
                end = mid -1 
        

        start , end = 0 , len(nums) -1 
        while start <= end:
            mid = end - (end - start)//2
            if nums[mid] == target:
                last = mid 
                start = mid  + 1 
            elif nums[mid] < target:
                start = mid + 1 
            else:
                end = mid -1 
        return last - first + 1 if first != -1 and lsat!= -1 else 0 
