class Data:
    def __init__(self, data):
        self.data = data

class Node:
    def __init__ (self, data):
        self.data = data
        self.next = None
        self.previous = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None


    def add_data(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.previous = current
            self.tail = new_node

    
    def delete_data(self, data):
        if not self.head:
            print("List is empty")
            return False

        current = self.head
        while current:
            if current.data == data:
                if current == self.head:
                    self.head = current.next
                if current == self.tail:
                    self.tail = current.previous
                if current.previous:
                    current.previous.next = current.next
                if current.next:
                    current.next.previous = current.previous
                print(f"{data} deleted successfully.")
                return True
            current = current.next
        print("Data not found in list.")
        return False
            
    
    def iterate(self):
        if not self.head:
            print("List is empty")
            return
        else:
            current = self.head
            while current:
                print(f"Data: {current.data}")
                current = current.next
    

new_list = DoublyLinkedList()
new_list.add_data("1")
new_list.add_data("2")
new_list.add_data("3")
new_list.add_data("4")


new_list.iterate()
new_list.delete_data("3")
new_list.iterate()

