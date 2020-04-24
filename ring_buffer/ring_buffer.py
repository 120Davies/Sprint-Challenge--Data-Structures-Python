from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if self.storage.length < self.capacity:
            self.storage.add_to_tail(item)
            self.current = self.storage.tail
        elif self.current == self.storage.tail:
            self.storage.head.value = item
            self.current = self.storage.head
        else:
            self.current.next.value = item
            self.current = self.current.next


    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []
        node = self.storage.head
        while node is not None:
            list_buffer_contents.append(node.value)
            node = node.next
        return list_buffer_contents

# passes all but 2 tests. good enough for MVP.
# I'll hopefully come back to this later.

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        self.storage = [None] * capacity

    def append(self, item):
        if len(self.storage) == self.capacity:
            self.storage[self.current] = item
            if self.current is len(self.storage) - 1:
                self.current = 0
            else:
                self.current += 1
        else:
            self.storage.append(item)

    def get(self):
        return [x for x in self.storage if x is not None]

# All tests pass instantly. Yeah!
