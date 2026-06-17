class Solution:
    def addTwoNumbers(self, l1, l2):
        head = ListNode(0)
        temp = head
        carry = 0

        while l1 is not None or l2 is not None or carry > 0:

            num1 = 0
            num2 = 0

            if l1 is not None:
                num1 = l1.val
                l1 = l1.next

            if l2 is not None:
                num2 = l2.val
                l2 = l2.next

            total = num1 + num2 + carry
            carry = total // 10

            new_node = ListNode(total % 10)
            temp.next = new_node
            temp = temp.next

        return head.next