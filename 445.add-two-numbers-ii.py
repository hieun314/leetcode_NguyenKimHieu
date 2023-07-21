#
# @lc app=leetcode id=445 lang=python3
#
# [445] Add Two Numbers II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = [0]
        num2 = [0]
        output = None
        while l1:
            num1.append(l1.val)
            l1 = l1.next
        while l2:
            num2.append(l2.val)
            l2 = l2.next
        i, j, carry = -1, -1, 0
        while True:
            total = num1[i] + num2[j] + carry
            carry = total//10
            node = ListNode(total%10)
            node.next = output
            output = node
            if i != -len(num1):
                i -= 1
            if j != -len(num2):
                j -= 1
            if i == -len(num1) and j == -len(num2):
                if carry == 1:
                    node = ListNode(1)
                    node.next = output
                    output = node                
                break
        return output        
# @lc code=end

