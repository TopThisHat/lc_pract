import types

class ListNode:
    def __init__(self, val:int = 0, next: any =None):
        self.val = val
        self.next = next

def addTwoNumbers(l1: ListNode, l2: ListNode)->ListNode:
    """
    This is pretty straight forward.  We want to loop through both nodes together and add the corresponding values.
    So we have to keep track of when to carry a 1 over and create a new ListNode with the values.


    The way I approached this is by creating a dummy node and setting it to 0 and use a pretty common pattern for
    NodeList.  Create a new object that references the dummy node and modify that value.  The modification will such as
    reference.next will modify result and we also mutate the reference without mutating the original value and store that new
    values in a new memory location.

    Now I loop through both ListNodes and add the two terms and track the carry by using divmod.



    """

    result = ListNode(val=0)
    reference = result
    carry = 0

    while l1 or l2 or carry:
        x = l1.val if l1 else 0
        y = l2.val if l2 else 0

        carry, out = divmod(x + y + carry, 10)

        reference.next = ListNode(out)
        reference = reference.next

        l1 = (l1.next if l1 else None)
        l2 = (l2.next if l2 else None)

    return result.next

