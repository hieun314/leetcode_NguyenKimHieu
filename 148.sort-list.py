#
# @lc app=leetcode id=148 lang=python3
#
# [148] Sort List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        arr.sort()
        head = ListNode()
        new_list = head
        for num in arr:
            new_list.next = ListNode(num)
            new_list = new_list.next
        return head.next    
# @lc code=end

