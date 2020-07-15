
"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    # Replaces the head of the list with the new value that is passed in

    def add_to_head(self, value):

        # Initialize a node with a value of the value passed in
        new_node = ListNode(value, None, self.head)

        # If the list is empty
        if not self.head and not self.tail:  # if self.length == 0
            # if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.length = 1

        # If the list has 2 or more items
        else:
            prev_head = self.head
            self.head = new_node
            self.head.next = prev_head

            # Increment our length
            self.length += 1
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """

    # Removes the head node and returns the value stored in it
    def remove_from_head(self):
        # If the list is empty
        if not self.head and not self.tail:  # self.length == 0
            return None

        # If the list has one item
        elif self.head == self.tail:  # not self.head.next:
            # get a reference to the head
            head_to_return = self.head

            # delete the list head's reference & the tail's reference
            self.head = None
            self.tail = None

            self.length = 0

            # return the value
            return head_to_return.value

        # If the list has 2 or more items
        else:
            # get a reference to the head
            head_to_return = self.head

            # set the head to be what was previously next to the head
            self.head = self.head.next
            # set what was previously before the head to none
            self.head.prev = None

            # Increment the length
            self.length -= 1

            # return the value
            return head_to_return.value

    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    # Replaces the tail of the list with a new value that is passed in

    def add_to_tail(self, value):
        # Initialize a node with a value of the value passed in
        new_node = ListNode(value, None, None)

        # If the list is empty
        if not self.tail and not self.head:
            self.head = new_node
            self.tail = new_node
            self.length += 1

        # If the list has 2 or more items
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1

    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    # Removes the tail node and returns the value stored in it

    def remove_from_tail(self):
        # If the list is empty
        if not self.head and not self.tail:
            # if self.tail is None:
            return None

        # If the list has one item
        elif self.head == self.tail:
            # get a reference to the tail
            tail_node_to_remove = self.tail

            # delete the tail from the list
            self.tail.delete()

            self.length -= 1

            # delete the list's head reference
            self.head = None
            # delete the list's tail reference
            self.tail = None

            # return the value
            return tail_node_to_remove.value

        # If the list has 2 or more items
        else:
            # get a reference to the tail
            tail_node_to_remove = self.tail

            # delete the tail from the list
            self.tail.delete()

            self.length -= 1

            # return the value
            return tail_node_to_remove.value

    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    # Takes a reference to a node in the list & moves it to the front
    # of the list, shifting all other nodes down

    def move_to_front(self, node):

        # If the list is empty
        if not self.head and not self.tail:
            self.add_to_head(node.value)

        # If the list has one item
        elif self.head == self.tail:
            # if the node is already in the front
            if self.head is node:
                return
            else:
                self.head = node
                self.tail = node

        # If the list has 2 or more items
        else:
            self.add_to_head(node.value)
            node.delete()
            self.length -= 1

    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    # Takes a reference to a node in the list and moves it to the end of the list,
    # shifting all other nodes up

    def move_to_end(self, node):

        # If the list is empty
        if not self.head and not self.tail:
            self.add_to_tail(node.value)

        # If the list has one item
        elif self.head == self.tail:
            self.add_to_tail(node.value)

        # if the node is in the front
        elif self.head == node:
            self.head = self.head.next
            self.head.prev = None
            self.length -= 1
            self.add_to_tail(node.value)

        else:
            node.delete()
            self.length -= 1
            self.add_to_tail(node.value)
    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    # Takes a reference to a node in the list and removes it from the list.
    # The deleted node's `previous` and `next` pointers should point to each afterwards.

    def delete(self, node):

        # If the list is empty
        if not self.head and not self.tail:
            return

        elif self.head == self.tail:
            node.delete()
            self.head = None
            self.tail = None
            self.length = 0

        elif self.head == node:
            self.head = node.next
            node.delete()
            self.length -= 1

        elif self.tail == node:
            self.tail = node.prev
            node.delete()
            self.length -= 1

        else:
            node.delete()
            self.length -= 1

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    # Returns the maximum value in the list

    def get_max(self):

        max_value = None

        # If the list is empty
        if not self.head:
            return -1

        else:
            node_to_check = self.head
            max_value = self.head.value
            # If the list has one or more items
            while node_to_check.next is not None:
                node_to_check = node_to_check.next
                if node_to_check.value > max_value:
                    max_value = node_to_check.value
            return max_value
