class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
    
    def __repr__(self) -> str:
        return str(self.data)

class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def insertion_by_sort(self, data):
        new_node = Node(data)

        if not self.head or data <= self.head.data:
            new_node.next = self.head
            self.head = new_node
            return
        
        current = self.head
        while current.next and current.next.data < data:
            current = current.next
        
        new_node.next = current.next
        current.next = new_node

    def insert_at_the_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_the_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def insert_by_position(self, data, position):
        new_node = Node(data)
        current = self.head
        count = 1

        while current.next and count < position - 1:
            current = current.next
            count += 1
        
        new_node.next = current.next
        current.next = new_node

    def delete_by_position(self, position):
        current = self.head
        count = 1

        if position <= 0 or not self.head:
            return

        if position == 1:
            self.head = self.head.next
            return

        while current.next and count < position - 1:
            current = current.next
            count += 1
        
        if current and current.next:
            current.next = current.next.next

    def delete_by_value(self, value):
        if not self.head:
            return
        
        if self.head.data == value:
            self.head = self.head.next
            return
        
        current = self.head
        while current.next:
            if current.next.data == value:
                current.next = current.next.next
                return
            current = current.next

    def addition_of_sll(self):
        if not self.head:
            return

        sum = 0
        current = self.head
        while current:
            sum += current.data
            current = current.next
        return sum

    def search_value(self, value):
        if not self.head:
            return
        
        current = self.head
        while current:
            if current.data == value:
                return True
            current = current.next
        return False
    
    def len_of_SLL(self):
        if not self.head:
            return

        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count
    
    def reverse_of_SLL(self):
        if not self.head:
            return
        
        prev_node = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev_node
            prev_node = current
            current = next_node
        self.head = prev_node

    def print_the_values(self):
        current = self.head
        while current:
            print(current, end="->")
            current = current.next
        print('None')

if __name__ == "__main__":
    SLL = LinkedList()
    SLL.insertion_by_sort(55)
    SLL.insertion_by_sort(75)
    SLL.insertion_by_sort(56)
    SLL.insertion_by_sort(35)
    SLL.print_the_values()
    SLL.insert_at_the_beginning(5)
    SLL.insert_at_the_beginning(7)
    SLL.insert_at_the_beginning(3)
    SLL.insert_at_the_beginning(2)
    SLL.insert_at_the_beginning(9)
    SLL.print_the_values()
    SLL.insert_at_the_end(10)
    SLL.print_the_values()
    SLL.insert_by_position(33, 3)
    SLL.print_the_values()
    SLL.delete_by_position(2)
    SLL.print_the_values()
    SLL.delete_by_value(5)
    SLL.print_the_values()
    SLL.delete_by_value(10)
    SLL.print_the_values()
    print("The sum of all elements in the list", SLL.addition_of_sll())
    print("Search result: ", SLL.search_value(33))
    SLL.print_the_values()
    print("The lenth of SLL", SLL.len_of_SLL())
    SLL.reverse_of_SLL()
    SLL.print_the_values()

