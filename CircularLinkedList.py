class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

    def __repr__(self) -> str:
        return str(self.data)
    
class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            new_node.next = self.head
            return
        
        current = self.head

        while current.next != self.head:
            current = current.next

        new_node.next = self.head
        self.head = new_node
        current.next = new_node       

    def insert_at_middle(self, data, position):
        new_node = Node(data)
        count = 1

        if not self.head:
            self.head = new_node
            new_node.next = self.head
            return
        
        current = self.head
        while current.next and count < position-1:
            current = current.next
            count += 1

        new_node.next = current.next
        current.next = new_node

    def insert_at_end(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            new_node.next = self.head
            return
        
        current = self.head
        while current.next != self.head:
            current = current.next

        current.next = new_node
        new_node.next = self.head

    def delete_by_position(self, position):
        if not self.head or position <= 0:
            return
        count = 1
        current = self.head

        if position == 1:
            while True:
                current = current.next
                if current.next == self.head:
                    break
            current.next = self.head.next
            self.head = self.head.next
        
        else:
            while current.next != self.head and count < position-1:
                current = current.next
                count += 1

            if current.next == self.head:
                return

            current.next = current.next.next

    def print_values(self):
        if not self.head:
            return

        current = self.head
        while True:
            print(current, end="->")
            current = current.next
            if current == self.head:
                break
        print("None")  

if __name__ == "__main__":
    CLL = LinkedList()
    CLL.insert_at_beginning(5)
    CLL.insert_at_beginning(8)
    CLL.insert_at_beginning(3)
    CLL.insert_at_end(9)
    CLL.insert_at_middle(33, 3)
    CLL.insert_at_middle(44, 4)
    CLL.print_values()
    CLL.delete_by_position(1)
    CLL.print_values()