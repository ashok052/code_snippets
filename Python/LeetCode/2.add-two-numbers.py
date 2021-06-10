#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from math import pow


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def fullValue(listNode):
            value = 0
            pos = 0
            currentNode = listNode
            while currentNode:
                print(currentNode.val, pos, pow(10, pos), int(
                    pow(10, pos)), currentNode.val * int(pow(10, pos)), value)
                value += currentNode.val * int(pow(10, pos))
                currentNode = currentNode.next
                pos += 1
            print(value)
            return value

        def fullValue_new(listNode):
            string = []
            currentNode = listNode
            while currentNode:
                string.append(currentNode.val)
                currentNode = currentNode.next
            value = int(''.join([str(x) for x in string[::-1]]))
            print(f"{string} = {value}")
            return int(value)

        def intToNode(value):
            print(value)
            node = None
            for char in str(value):
                prev = node
                node = ListNode(int(char), prev)
            return node

        a = fullValue_new(l1)
        b = fullValue_new(l2)
        print(f"{a} + {b} = {a+b}")
        sum = a + b
        return intToNode(sum)
# @lc code=end
