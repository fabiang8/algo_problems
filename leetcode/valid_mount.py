class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        i = 1
        while(i < len(arr) and arr[i] > arr[i-1]):    # check for increasing    
            i += 1

        if (i == len(arr) or i == 1):
            return False

        while(i < len(arr) and arr[i - 1] > arr[i]):
            i += 1

        return i == len(arr) 
