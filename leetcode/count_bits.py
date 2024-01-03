class Solution:
    def count_occurences(self, digit):
        count = 0
        
        print(digit)
        digit = int(digit)
        while (digit > 0):
            if(digit%10 == 1):
                count = count + 1
            digit = digit // 10
        return count
        
    
    
    def countBits(self, n: int) -> List[int]:
        ans = []
        for i in range(0, n + 1):
            ans.append(i)
            ans[i] = bin(ans[i])[2:]
            ans[i] = self.count_occurences(ans[i])
            
            
        return ans