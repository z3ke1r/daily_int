'''
  Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
  Output: 7 -> 0 -> 8
  Explanation: 342 + 465 = 807.
'''

# Definition for singly-linked list.


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2, c=0):
        # declarations
        suma = 0
        sumb = 0
        place = 1
        loopCount = 0

        while(l1 and l2):
            suma += (l1.val * place)
            sumb += (l2.val * place)
            place *= 10
            l1 = l1.next
            l2 = l2.next
            loopCount += 1

        result = suma + sumb
        place = 1

        r = ListNode(0)
        a = r  # keep track of the beginning of r

        for i in range(loopCount):
            r.val = int(((1 / place) * result)) % 10
            place *= 10
            r.next = ListNode(0)
            r = r.next

        return a


l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

result = Solution().addTwoNumbers(l1, l2)
while result:
    print(result.val)
    result = result.next
# 7 0 8
