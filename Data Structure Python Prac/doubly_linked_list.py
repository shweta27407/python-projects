"""
Notes
# head and tail are always empty as they are dummy for adding, removing elements
# 

"""

class DoublyLinkedNode:
    def __init__(
        self,
        item: int = None,
        prev: "DoublyLinkedNode | None" = None,
        next: "DoublyLinkedNode | None" = None
    ) -> None:
        self._item = item
        self._prev = prev
        self._next = next


class DoublyLinkedList:
    def __init__(self) -> None:
        self._head = DoublyLinkedNode()
        self._tail = DoublyLinkedNode(prev=self._head)
        self._size = 0
    
    def __len__(self) -> int:
        if not self.head:
            return '[]'
        else:
            return self._size
   
    def is_empty(self) -> bool:
        if self._head is None:
            return True
        return False

    def add_first(self, item: int) -> None:
        if self.head is None:
            new_node = DoublyLinkedNode(item)
            self.head = new_node
            print("node inserted")
            return
        new_node = DoublyLinkedNode(item)
        new_node._next = self.head
        self.head._prev = new_node
        self.head = new_node
    
    def get_first(self) -> int | None:
        if self.is_empty():
            raise Exception("List is empty")
        else:
            return self.__header.get_next()
    
    def remove_first(self) -> int | None:
        if self.head is None:
            print("The list has no element to delete")
            return 
        if self.head._next is None:
            self.head = None
            return
        self.head = self.head._next
        self.start_prev = None;

    def add_last(self, item: int) -> None:
        if self.head is None:
            new_node = DoublyLinkedNode(item)
            self.head = new_node
            return
        n = self.head
        while n._next is not None:
            n = n._next
        new_node = DoublyLinkedNode(item)
        n._next = new_node
        new_node._prev = n
    
    def get_last(self) -> int | None:
        if self.is_empty():
            raise Exception("List is empty")
        else:
            return self.__trailer.get_previous()
    
    def remove_last(self) -> int | None:
        if self.head is None:
            print("The list has no element to delete")
            return 
        if self.head._next is None:
            self.head = None
            return
        n = self.head
        while n._next is not None:
            n = n._next
        n._prev._next = None

if __name__ == "__main__":
    pass
