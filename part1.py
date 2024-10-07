class Data:
    def __init__(self, data):
        self.data = data

class Node:
    def __init__ (self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None


    def add_data(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    
    def delete_data(self, data):
        if not self.head:
            print("List is empty")
            return

        if self.head.data == data:
            print(f"{data} deleted successfully.")
            self.head = self.head.next

        prev = None
        current = self.head
        while current:
            if current.data == data:
                prev.next = current.next
                print(f"{data} deleted successfully.")
                return
            prev = current
            current = current.next
    
    def iterate(self):
        if not self.head:
            print("List is empty")
            return
        else:
            current = self.head
            while current:
                print(f"Data: {current.data}")
                current = current.next
    

new_list = SinglyLinkedList()
new_list.add_data("1")
new_list.add_data("2")
new_list.add_data("3")
new_list.add_data("4")


new_list.iterate()
new_list.delete_data("3")
new_list.iterate()

