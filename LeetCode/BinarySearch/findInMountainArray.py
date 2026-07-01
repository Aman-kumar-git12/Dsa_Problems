# Question: Find in Mountain Array
# link : https://leetcode.com/problems/find-in-mountain-array/description/

def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
    def binarysearchAsc( start , end):
        while start <= end:
            mid = start + (end - start)//2 
            if mountainArr.get(mid) == target:
                return mid
            elif mountainArr.get(mid) > target:
                end = mid -1 
            elif mountainArr.get(mid) < target:
                start = mid + 1 
        return -1 
    def binarysearchDes( start , end):
        while start <= end:
            mid = end - (end - start)//2
            if mountainArr.get(mid) == target:
                return mid 
            elif mountainArr.get(mid) < target:
                end = mid -1 
            elif mountainArr.get(mid) > target:
                start = mid + 1
        return -1
    
    def findPickelement():
        start , end  = 0 , mountainArr.length()-1 
        

        while start <= end:
            mid = end - (end - start)//2
            
            if mid < mountainArr.length()-1 and mid > 0 :

                if mountainArr.get(mid) >= mountainArr.get(mid - 1 ) and mountainArr.get(mid) >= mountainArr.get(mid + 1 ):
                    return mid
                elif mountainArr.get(mid) < mountainArr.get(mid -1 ):
                    end = mid -1 
                elif mountainArr.get(mid) < mountainArr.get(mid + 1):
                    start = mid + 1

            else:
                if mid == 0:
                    if mountainArr.get(mid) > mountainArr.get(mid + 1):
                        return mid 
                    else :
                        return mid + 1
                else :
                    if mountainArr.get(mid) > mountainArr.get(mid -1 ):
                        return mid 
                    else :
                        return mid -1 
                        
    pick  = findPickelement()
    print(pick )

    left = binarysearchAsc( 0 ,pick)
    right = binarysearchDes( pick + 1 , mountainArr.length()-1)

    if left != -1:
        return left 
    elif right != -1 :
        return right 
    else:
        return -1 



    
    