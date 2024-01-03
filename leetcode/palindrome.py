class Solution:
    def isPalindrome(self, x: int) -> bool:

        if x < 0:
            return False

        rlist = [int(i) for i in str(x)]
        
        nlist = rlist[::-1]

        return (rlist == nlist)