class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        listlen = len(nums)
        setlen = len(set(nums))
        print(setlen,listlen)
        if (listlen == setlen):
            return False
        else:
            return True