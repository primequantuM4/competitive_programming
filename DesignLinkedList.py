class Node:
    def __init__(self, val=None):
        self.val = val
        self.next, self.prev = None


class MyLinkedList:

    def __init__(self):
        self.head = Node()

    def get(self, index: int) -> int:
        current = self.head
        ptr = 0
        while ptr < index:
            current = current.next
            ptr += 1
            if current is None:
                return -1
        if current.next is None:
            return -1
        return current.next.val

    def addAtHead(self, val: int) -> None:
        values = Node(val)
        values.next = self.head.next
        self.head.next = values
        return self.head.next.val

    def addAtTail(self, val: int) -> None:
        if self.head.next == None:
            self.head.next = Node(val)
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = Node(val)

    def addAtIndex(self, index: int, val: int) -> None:
        current = self.head
        for ptr in range(index):
            current = current.next
        inserted_value = Node(val)
        if current is None:
            current = inserted_value
        inserted_value.next = current.next
        current.next = inserted_value

    def deleteAtIndex(self, index: int) -> None:
        current = self.head
        for ptr in range(index):
            current = current.next
            if current is None:
                return
        
        if current.next is None:
            return
        elif current.next.next is None:
            current.next = None
        else:
            current.next = current.next.next
