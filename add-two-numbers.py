# Add Two Numbers

# Given two non-empty linked lists
# representing two non-negative integers.
#
# The digits are stored in reverse order
# and each of their nodes contain a single digit
# add the two numbers and and return it as a linked list

# Input (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output (7 -> 0 -> 8)

# Explanation 342 + 465 = 807
from collections import deque

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        d1 = deque()
        d2 = deque()
        def accum(ln, _deque):
            _deque.appendleft(str(ln.val))            
            if ln.next:
                accum(ln.next,_deque)
                
        accum(l1, d1)
        accum(l2, d2)
        n1 = int("".join(list(d1)))
        n2 = int("".join(list(d2)))

        # reverse the sum
        answer = list(str(n1 + n2)[::-1])
        
        # Make the return type ListNode
        def recur(ls):
            if not ls:
                return None
            return ListNode(ls[0], recur(ls[1:]))
        
        return recur(answer)

# The Python answer chosen at
# -->  https://leetcode.com/problems/add-two-numbers/solution/
#
# is too code golf like.
#
# Keep your code simple, so you can read it years later!
def mathySolution(l1,l2,carry=0):
    val = l1.val + l2.val + carry
    carry = val // 10
    ret = ListNode(val % 10)

    if (l1.next != None or\
        l2.next != None or\
        carry != 0):
        if l1.next == None:
            l1.next = ListNode(0)
        if l2.next == None:
            l2.next = ListNode(0)
        ret.next = mathySolution(l1.next,l2.next,carry)
    return ret

        

if __name__ == "__main__":
    l1 = ListNode(2, ListNode(4, ListNode(3)))
    l2 = ListNode(5, ListNode(6, ListNode(4)))
    s = Solution()

    def display(an):
        print(an.val)
        if an.next:
            display(an.next)

    display(s.addTwoNumbers(l1,l2))
    display(mathySolution(l1,l2))

