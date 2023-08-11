class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
        self.prev = None

    def __repr__(self) -> str:
        return str(self.data)

class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.end = None

    def insert_in_sort(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            return
        
        current = self.head

        if current.data >= data:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        
        while current.next and current.next.data < data:
            current = current.next

        new_node.next = current.next
        new_node.prev = current
        current.next = new_node
        current.next.prev = new_node

    def insert_in_end(self, data):
        new_node = Node(data)
        
        if not self.head:
            self.head = new_node

        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current

    def insert_in_beginning(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node

        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insert_in_middle(self, data, position):
        new_node = Node(data)
        count = 0
        current = self.head
        if not self.head:
            self.head = new_node

        else:
            while count < position:
                current = current.next
                count+=1
            new_node.next = current.next
            new_node.prev = current
            current.next.prev = new_node
            current.next = new_node

    def delete_by_position(self, position):
        count = 1
        if not self.head or position <= 0:
            return
        
        current = self.head
        if current and position == 1:
            self.head = current.next
            self.head.prev = None
        else:
            while current and count < position:
                current = current.next
                count += 1
            
            current.prev.next = current.next
            current.next.prev = current.prev

    def reverse_dll(self):
        if not self.head:
            return
        
        current = self.head
        while current.next:
            current = current.next
        self.head = current
        while current:
            current.prev, current.next = current.next, current.prev
            current = current.next

    def swap_dll(self): #ISSUE
        if not self.head or not self.head.next:
            return
        
        current = self.head
        while current.next:
            current.next, current.next.prev = current.next.prev, current.next
            current = current.next
    
    def print_values(self):
        current = self.head

        while current:
            print(current.data, end="-->")
            current = current.next
        print("None")

if __name__ == "__main__":
    DLL = LinkedList()
    '''DLL.insert_in_end(5)
    DLL.insert_in_end(6)
    DLL.insert_in_end(4)
    DLL.insert_in_end(3)
    DLL.print_values()
    print("\n----------insert in beginning----------")
    DLL.insert_in_beginning(1)
    DLL.insert_in_beginning(2)
    DLL.insert_in_beginning(8)
    DLL.print_values()
    print("\n----------insert in middle----------")
    DLL.insert_in_middle(33, 3)
    DLL.print_values()
    DLL.reverse_dll()
    DLL.print_values()'''
    DLL.insert_in_sort(10)
    DLL.insert_in_sort(45)
    DLL.insert_in_sort(25)
    DLL.insert_in_sort(50)
    DLL.insert_in_sort(60)
    DLL.print_values()
    #DLL.swap_dll()
    #DLL.print_values()
    DLL.delete_by_position(2)
    DLL.print_values()
        
        