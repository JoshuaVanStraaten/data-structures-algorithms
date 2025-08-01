class Node:
    """
    An object for storing a single node of a linked list.
    Models two attributes - data and a pointer to the next node.
    """
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f"<Node data: {self.data}>"


class LinkedList:
    """
    Singly linked list class
    """
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def size(self):
        """
        Returns the number of nodes in the linked list
        Takes O(n) time
        """
        current = self.head
        count = 0
        while current:
            count += 1
            # Assign current to the next node
            current = current.next
        return count

    def add(self, data):
        """
        Adds a new node containing data at the head of the list
        Takes O(1) time
        """
        new_node = Node(data)
        # To set the new node as the head of the list,
        # we need to point the new node's next to the current head
        new_node.next = self.head
        self.head = new_node

    def search(self, key):
        """
        Search for the first node containing data that matches the key
        Returns the node or `None` if not found
        Takes O(n) time
        """
        current = self.head
        while current:
            if current.data == key:
                return current
            current = current.next
        return None

    def insert(self, data, index):
        """
        Insert a new node containing data at the specified index
        Insertion takes O(1) time if inserting at the head, but O(n) time
        if inserting at any other pos since we need to traverse the list
        """
        if index == 0:
            self.add(data)
            return

        if index > 0:
            new = Node(data)

            pos = index
            current = self.head
            while pos > 1:
                current = current.next
                pos -= 1

            # Save the current node as prev and the next node as nxt
            # so we can insert the new node in between
            prev = current
            nxt = current.next

            # Insert the new node (assign the next pointers)
            prev.next = new
            new.next = nxt

    def remove(self, key):
        """
        Removed node containing data that matches the key
        Returns the removed node or `None` if not found
        Takes O(n) time
        """
        current = self.head
        previous = None
        found = False

        while not found and current:
            if current.data == key and current is self.head:
                found = True
                # Remove head by making head the next node
                self.head = current.next
            elif current.data == key:
                found = True
                # Remove the node by making the previous node point
                # to the next node
                previous.next = current.next
            else:
                # If the current node is not the one we want to remove,
                # move to the next node and save the previous node.
                previous = current
                current = current.next

        return current

    def node_at_index(self, index):
        if index == 0:
            return self.head
        else:
            current = self.head
            pos = 0

            while (pos < index):
                current = current.next
                pos += 1

        return current

    def __repr__(self):
        """
        Return a string representation of the linked list
        Takes O(n) time
        """
        nodes = []
        current = self.head

        while current:
            if current is self.head:
                nodes.append(f"[Head: {current.data}]")
            elif current.next is None:
                nodes.append(f"[Tail: {current.data}]")
            else:
                nodes.append(f"[{current.data}]")

            current = current.next

        return "->".join(nodes)


# Without `__repr__`, when printing a Node object,
# it would show the memory address instead of the data.
# l = LinkedList()
# N1 = Node(10)
# l.head = N1
# print(l.size())
# l.add(20)
# print(l.size())
# l.add(30)
# print(l)
# print(l.search(20))
