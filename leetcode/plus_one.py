class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
      
        ''' 
        digit = ''.join(str(i) for i in digits)
        lastdigit = digits[-1]
        lastdigit = int(lastdigit)
        lastdigit = lastdigit + 1
        lastdigit = str(lastdigit)
        str1 = ''.join(str(i) for i in digits[:-1])
        newstr = str1 + lastdigit
        newlist = []
        newlist[:0] = newstr
        return newlist
        '''
    
        digit = ''.join(str(i) for i in digits)
        digit = int(digit) + 1
        newlist = [int(x) for x in str(digit)]
        return newlist
        
        
        
        #print (digit)