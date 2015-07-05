# Given a linked list, remove the nth node from the end of list and return its
# head.
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} n
    # @return {ListNode}
    def removeNthFromEnd(self, head, n):
        nodes = self.getNodesCount(head)
        n = nodes - n + 1 # nodo a eliminar desde el inicio
        if n == 1 :
            return (head.next)
        i = 0
        node = head
        while node != None :
            i += 1
            if i + 1 == n :
                node.next = node.next.next
            node = node.next
        return head
    def getNodesCount(self, head) :
        nodes = 0
        node = head
        while node != None :
            nodes += 1
            node = node.next
        return nodes

if __name__ == "__main__" :
    head = ListNode(1)
    #head.next = ListNode(2)
    #head.next.next = ListNode(3)
    #head.next.next.next = ListNode(4)
    #head.next.next.next.next = ListNode(5)
    node = head
    while node != None :
        print (node.val, end=" ")
        node = node.next
    print ()
    s = Solution()
    head = s.removeNthFromEnd(head, 1)
    node = head
    while node != None :
        print (node.val, end=" ")
        node = node.next
    print ()
