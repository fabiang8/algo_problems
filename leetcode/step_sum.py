class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        
        start_val = 1
        
        while True:
            total= start_val
            is_valid = True
            
            for num in nums:
                total += num
                
                
                if total < 1:
                    is_valid = False
                    break
                          
            if is_valid: 
                return start_val
            else:
                start_val += 1
                