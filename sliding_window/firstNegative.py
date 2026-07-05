# Question : First Negative in Windows of Size K
# link : https://www.geeksforgeeks.org/problems/first-negative-integer-in-every-window-of-size-k3345/1


def firstNegInt(self, arr, k): 
    # main = []
    # for i in range(len(arr)):
    #     if i-k+1 >= 0:
    #         inserted = 0
    #         for j in range(i-k+1 , i+1):
    #             if arr[j] < 0 :
    #                 main.append(arr[j])
    #                 inserted = 1 
    #                 break
    #         if inserted == 0:
    #             main.append(0)
    # return main 
    
        
    from collections import deque


    n = len(arr)
    i = 0
    j = 0
    negatives = deque()
    result = []

    while j < n:

        # Add negative element
        if arr[j] < 0:
            negatives.append(arr[j])

        # Window not yet complete
        if (j - i + 1) < k:
            j += 1

        # Window complete
        elif (j - i + 1) == k:

            # Store answer
            if negatives:
                result.append(negatives[0])
            else:
                result.append(0)

            # Remove outgoing element if it is the first negative
            if arr[i] < 0 and negatives and negatives[0] == arr[i]:
                negatives.popleft()

            # Slide window
            i += 1
            j += 1

    return result