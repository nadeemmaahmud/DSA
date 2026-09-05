class LinkedList:
    def __init__(self, val):
        self.val = val
        self.next = None

def add_new_element_beginning(head, val):
    if head is None:


def display_list(head):
    lst = []

    curr = head
    while curr:
        lst.append(str(curr.val))
        curr = curr.next

    print(" -> ".join(lst))

node = LinkedList(1)
node1 = LinkedList(2)
node2 = LinkedList(3)

node.next = node1
node1.next = node2

display_list(node)