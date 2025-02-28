# https://leetcode.com/problems/merge-k-sorted-lists/description/
# Given an array of k linked-lists lists, each linked-list is sorted in ascending order.
# Merge all the linked-lists into one sorted linked-list and return it.

# reference: https://leetcode.com/problems/merge-k-sorted-lists/solutions/6124518/0-ms-runtime-beats-100-user-code-idea-algorithm-solving-step/
# Use divide and conquer to repeatedly split the k lists into two groups, then continuously merge the two parts.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        return self.dc(lists, 0, len(lists)-1)
    def dc(self, lists, left, right) -> Optional[ListNode]:
        """
        Use divide and conquer to repeatedly split the k lists into two groups, then continuously merge the two parts.
        """
        if left == right: # split to the end (only one linked-list), return the linked-list
            return lists[left]
        mid = left + (right-left)//2
        l1 = self.dc(lists, left, mid) # first half
        l2 = self.dc(lists, mid+1, right) # second half
        return self.merge(l1, l2)
    def merge(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1: # no more nodes left in l1
            return l2
        if not l2: # no more nodes left in l2
            return l1
        if l1.val < l2.val: # l1's first num is smaller
            l1.next = self.merge(l1.next, l2) # l1's first num move to head, followed by the result of merging l2 and remaining l1 
            return l1
        else: # l2's first num is smaller or equal
            l2.next = self.merge(l1, l2.next) # l2's first num move to head, followed by the result of merging l2 and l1
            return l2



        