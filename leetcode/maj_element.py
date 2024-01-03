class Solution:
    
    def majorityElement(self, nums: List[int]) -> int:
        counts = {}    
        
        for num in nums:
            counts[num] = counts.get(num,0) + 1
        for num in nums:
                if counts[num] > len(nums)/2:
                    return num