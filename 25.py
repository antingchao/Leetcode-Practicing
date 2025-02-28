# https://leetcode.com/problems/reverse-nodes-in-k-group/description/
# Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

# reference: https://leetcode.com/problems/reverse-nodes-in-k-group/solutions/6073691/0-ms-runtime-beats-100-user-code-idea-algorithm-solving-step/
# in-place reversal technique

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if k==1 or not head: # k==1 output is same as original linked list 
            return head

        virtual = ListNode(-1, head) # create virtual head to keep track of the head of linked list & help the operation of first loop

        # count total len
        count = self.listNodeLen(head)
        # detailed note is in README and 25-note.jpeg
        prev = virtual
        while (count >= k): # remaining nodes are sufficient to be reversed # reverse
            curr = prev.next 
            nxt = curr.next
            for _ in range(1,k): # modify k-1 times (e.g. 1->2->3 k=3 modify 2=3-1 times)
                curr.next = nxt.next # curr move backward
                nxt.next = prev.next # nxt move to the first of the k-group (nxt.next link to the first one)
                prev.next = nxt # nxt move to the first of the k-group (prev link to nxt)
                nxt = curr.next # nxt++
            count -= k
            prev = curr
        return virtual.next

    def listNodeLen(self, head)->int:
        """
        count the len of the linked list
        """
        if not head:
            return 0
        count = 1
        while head.next:
            count += 1
            head = head.next
        return count