# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    
    
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    
    
        def insert(lead,val):
            temp = ListNode(val)
            if (lead == None):
                lead = temp
            else:
                ptr = lead
                while (ptr.next != None):
                    ptr = ptr.next
                ptr.next = temp
            return lead
    
    
        value1 = ""
        cur = l1
        while cur is not None:
            
            value1 += str(cur.val)
            cur = cur.next
        value2 = ""
        cur = l2
        while cur is not None:
            
            value2 += str(cur.val)
            cur = cur.next


            
        
        value1 = value1[::-1]
        value2 = value2[::-1]

        value3 = int(value1) + int(value2)

        sol = []

        value3 = str(value3)

        for digit in value3:
            cur = int(digit)
            sol.append(cur)

        sol = list(reversed(sol))
        
        #root = ListNode()
        root = None
        for i in range(0,len(sol),1):
            root = insert(root,sol[i])
        return root 
        