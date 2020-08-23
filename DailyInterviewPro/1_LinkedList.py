"""
Description:
You are given two linked-lists representing two non-negative integers.
The digits are stored in reverse order and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""

# Definition for singly-linked list.


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        output = "ListNode : "
        while self is not None:
            temp = "{} -> ".format(self.val)
            output += temp
            self = self.next
        output += "None"
        return output

    def __repr__(self):
        pass


class Solution:
    def addTwoNumbers(self, ln1, ln2, c=0):
        # Fill this in.
        ln3 = ListNode(0)
        while ln1 is not None or ln2 is not None:
            val = 0
            if ln1 is not None:
                val += ln1.val
                ln1 = ln1.next
            if ln2 is not None:
                val += ln2.val
                ln2 = ln2.next
            ln3.val = val
        print(ln3)


def main():
    ln1 = ListNode(2)
    ln1.next = ListNode(4)
    ln1.next.next = ListNode(3)
    print(ln1)

    ln2 = ListNode(5)
    ln2.next = ListNode(6)
    ln2.next.next = ListNode(4)
    print(ln2)

    result = Solution().addTwoNumbers(ln1, ln2)
    while result:
        print(result.val)
        result = result.next
    # 7 0 8


if __name__ == "__main__":
    main()
