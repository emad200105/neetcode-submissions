# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy1=ListNode()
        dummy2=dummy1

        while list1 and list2:
            if list1.val<list2.val:
                dummy2.next=list1
                list1=list1.next
            else:
                dummy2.next=list2
                list2=list2.next
            dummy2=dummy2.next
        
        while list1:
            dummy2.next=list1
            list1=list1.next
            dummy2=dummy2.next
        
        while list2:
            dummy2.next=list2
            list2=list2.next
            dummy2=dummy2.next

        return dummy1.next