# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        len1=0
        len2=0
        curr1=headA
        curr2=headB
        while(curr1):
            curr1=curr1.next
            len1+=1
        while(curr2):
            curr2=curr2.next
            len2+=1
        curr1,curr2=headA,headB
        if(len1>len2):
            for i in range(len1-len2):
                curr1=curr1.next
        else:
            for i in range(len2-len1):
                curr2=curr2.next
        while(curr1 and curr2):
            if curr1==curr2:
                return curr1
            curr1=curr1.next
            curr2=curr2.next
        return None
        