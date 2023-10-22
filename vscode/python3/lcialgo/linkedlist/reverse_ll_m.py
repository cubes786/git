from typing import Optional

class ListNode:
    def __init__(self, value=0, next=None):
        self.val = value
        self.next = next
    
class Solution:
    def reverseLLByClippingOneNodeAtATime(self, ptr: Optional[ListNode]) -> Optional[ListNode]:
        #reverseLLByClippingOneNodeAtATime: This is like taking one car at a time from the front
        #of the line and moving it to the front of a new line. We keep doing this until all cars are moved from 
        #the old line to the new line. Now, the new line has all the cars in reverse order compared 
        #to the original line.
        #1-2-3-4
        #1 2-3-4
        #2-1 3-4
        #3-2-1 4
        #4-3-2-1
        prev,curr=None,ptr
        while curr:
            next_temp=curr.next
            curr.next=prev
            prev=curr
            curr=next_temp
        return prev
    
    def reverseLLByInsertingOneNodeAtATime(self, ptr: Optional[ListNode]) -> Optional[ListNode]:
        #reverseLLByInsertingOneNodeAtATime: This is like having an extra helper car at the front of the line.
        #We take one car at a time from the middle of the line and put it right after the helper car. 
        #We keep doing this until all cars have been moved to be after the helper car. Now, if we ignore
        #the helper car, we have all the cars in reverse order.

        #Final stage at each iteration 
        #D(P)-1(C)-2-3-4
        #D(P)-2-1(C)-3-4
        #D(P)-3-2-1(C)-4
        #D(P)-4-3-2-1(C)

        #First iteration
        #D(P)-1(C)-2(N)-3-4
        #D(P)-1(C)-3-4 2(N)-3-4
        #D(P)-1(C)-3-4 2(N)-1(C)-3-4
        #D(P)-2(N)-1(C)-3-4

        #Second iteration
        #D(P)-2-1(C)-3(N)-4
        #D(P)-2-1(C)-4 3(N)
        #D(P)-2-1(C)-4 3(N)-2-1(C)-4         
        #D(P)-3(N)-2-1(C)-4

        dummy=ListNode(0,None)
        dummy.next=ptr
        prev,curr=dummy,dummy.next
        while curr.next:
            next_temp=curr.next            
            curr.next=next_temp.next
            next_temp.next=prev.next
            prev.next=next_temp            
        return dummy.next

    def printTraversell(self, head):
        while head:
            print(f'{head.val}', end=' ')
            head=head.next
        print('\n')
    
sol=Solution()
h4=ListNode(4,None)
h3=ListNode(3,None)
h2=ListNode(2,None)
h1=ListNode(1,None)
h1.next=h2
h2.next=h3
h3.next=h4

import copy
h11=copy.deepcopy(h1)
sol.printTraversell(h1)
sol.printTraversell(sol.reverseLLByClippingOneNodeAtATime(h1))
sol.printTraversell(h11)
sol.printTraversell(sol.reverseLLByInsertingOneNodeAtATime(h11))




