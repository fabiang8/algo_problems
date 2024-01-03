from itertools import product

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        valuesdict = {}
        
        valuesdict["2"] = ["a","b","c"]
        valuesdict["3"] = ["d","e","f"]
        valuesdict["4"] = ["g","h","i"]
        valuesdict["5"] = ["j","k","l"]
        valuesdict["6"] = ["m","n","o"]
        valuesdict["7"] = ["p","q","r","s"]
        valuesdict["8"] = ["t","u","v"]
        valuesdict["9"] = ["w","x","y","z"]
        
        digits = str(digits)
        digitlist = []
        
        for char in digits:
            digitlist.append(char)
            
        permutations = []    
            
        if len(digitlist) < 0:
            return permutations
        elif len(digitlist) == 1:
            return valuesdict[digitlist[0]]
        elif len(digitlist) == 2:
            newlist = []
            arr1 = valuesdict[digitlist[0]]
            arr2 = valuesdict[digitlist[1]]
            dlist = []
            dlist.append(arr1)
            dlist.append(arr2)
            for element in itertools.product(*dlist):
                newel = ''.join(element)
                newlist.append(newel)
            return newlist  
                
        elif len(digitlist) == 3:
            arr1 = valuesdict[digitlist[0]]
            arr2 = valuesdict[digitlist[1]]
            arr3 = valuesdict[digitlist[2]]
            #print(arr1)
            dlist = []
            dlist.append(arr1)
            dlist.append(arr2)
            dlist.append(arr3)
            #print(*dlist)
            newlist = []
            for element in itertools.product(*dlist):
                #print(element)
                #newlist = []
                newel = ''.join(element)
                newlist.append(newel)
            return newlist  
        elif len(digitlist) == 4:
            arr1 = valuesdict[digitlist[0]]
            arr2 = valuesdict[digitlist[1]]
            arr3 = valuesdict[digitlist[2]]
            arr4 = valuesdict[digitlist[3]]
            dlist = []
            dlist.append(arr1)
            dlist.append(arr2)
            dlist.append(arr3)
            dlist.append(arr4)
            newlist = []
            for element in itertools.product(*dlist):
                newel = ''.join(element)
                newlist.append(newel)
            return newlist    