class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        arr.sort()
        dict_v = {}
        for num in arr:
            count = bin(num).count('1')
            if count not in dict_v:
                dict_v[count] = [num]
            else:
                dict_v[count].append(num)
        result = []
        for num in sorted(dict_v.keys()):
            result.extend(dict_v[num])
            
        return result