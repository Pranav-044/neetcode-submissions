# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        final=[]
        for i in lists:
            while i:
                final.append(i.val)
                i=i.next
        res=sorted(final)
        curr=ListNode(0)
        head=curr
        for j in range(len(res)):
            temp=ListNode(res[j])
            curr.next = temp
            curr=curr.next
        return head.next

        




        
        