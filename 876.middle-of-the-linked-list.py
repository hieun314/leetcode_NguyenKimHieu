#
# @lc app=leetcode id=876 lang=python3
#
# [876] Middle of the Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count = 0
        tmp = head
        while tmp:
            count += 1
            tmp = tmp.next
        mid = count//2
        output = ListNode()
        while head:
            if mid <= 0:
                break
            head = head.next
            mid -= 1
        return head
# @lc code=end

