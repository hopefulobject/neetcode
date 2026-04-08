# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        if head.next == None:
            return None

        dummy = ListNode(0)

        dummy.next = head

        count = 1

        while head.next != None:
            head = head.next
            count += 1

        count = count - n + 1

        head = dummy

        for _ in range(count-1):
            head=head.next

        head.next = head.next.next

        return dummy.next


        


            

        

        

        
            

        
