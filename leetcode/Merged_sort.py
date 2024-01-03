class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        storage = []

        if m is 0 and n is 0: # if m is 0,  handle case merge
            return 0
        elif m is 0 and n is not 0:
            storage.extend(nums2)
        elif m is not 0 and n is 0:
            storage.extend(nums1)
        elif m is not 0: # any value but 0 accepted
            for element in range(0,m): # for each value in list do something
                x = nums1[element]
                storage.append(x) # append elements up until m range
            for element in range(0,n):
                y = nums2[element]
                storage.append(y)
        nums1.clear()
        storage.sort()
        nums1.extend(storage)
        print(*storage,sep="\n")
            