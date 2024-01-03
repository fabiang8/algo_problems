class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:

    
        people.sort() # sort people array

        first = 0  # index 0
        last = len(people) - 1 # last index
        boat_count  = 0
        while (first <= last):
            if (first == last):
                boat_count += 1
                break
                
            if(people[first] + people[last] <= limit):
                first += 1
                
            last -= 1
            boat_count += 1

        return boat_count
