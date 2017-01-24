'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
'''
list1 = [5]
list2 = [5]
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
def addTwoNumbers(l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        startNode = ListNode(-1)
        curNode = startNode
        carry = 0;
        while(l1 or l2 or carry == 1):
            _val1 = l1.val if l1 else 0
            _val2 = l2.val if l2 else 0
            _sum = _val1 + _val2 + carry
            _digit = 0
            if _sum >= 10:
                _digit = _sum -10
                carry = 1
            else:
                _digit = _sum
                carry = 0
            _node = ListNode(_digit)
            curNode.next = _node
            curNode = curNode.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
        return startNode.next

def makeNodeList(list):
    startNode = ListNode(list[0])
    curNode = startNode
    # print list[1::]
    for x in list[1::]:
        _node = ListNode(x)
        curNode.next = _node
        curNode = curNode.next
    return startNode

def printNodeList(nodes):
    while nodes:
        print nodes.val
        nodes = nodes.next


nodes1 = makeNodeList(list1)
nodes2 = makeNodeList(list2)
printNodeList(addTwoNumbers(nodes1,nodes2))