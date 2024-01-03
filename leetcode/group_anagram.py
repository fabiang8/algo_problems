class Solution:
    
    
    def hashed(self,string):
        return ''.join(sorted(string))
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # for each string in list 
        answers = []
        kmap = {}
        
        for string in strs:
            sortval = self.hashed(string) # sorted string
            
            if (sortval not in kmap):
                kmap[sortval] = []
            kmap[sortval].append(string)
        
        for val in kmap.values():
            answers.append(val)
        
        
        return answers
            