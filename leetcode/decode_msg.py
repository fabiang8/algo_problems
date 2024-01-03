class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        i = 97
        hashm = { ' ' : ' '}
        for char in key:
            if char not in hashm and char is not ' ':
                hashm[char] = chr(i)
                i+=1

        res = ""
        for char in message:
            res+= hashm[char]
        return res        
