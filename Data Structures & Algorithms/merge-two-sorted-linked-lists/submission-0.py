# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode()
        dummy2=dummy
        cur1=list1
        cur2=list2

        while cur1 and cur2:
            if cur1.val>cur2.val:
                dummy2.next=cur2
                dummy2=dummy2.next
                cur2=cur2.next
            else:
                dummy2.next=cur1
                dummy2=dummy2.next
                cur1=cur1.next
        while cur1:
            dummy2.next=cur1
            cur1=cur1.next
            dummy2=dummy2.next
        
        while cur2:
            dummy2.next=cur2
            cur2=cur2.next
            dummy2=dummy2.next
            
        return dummy.next