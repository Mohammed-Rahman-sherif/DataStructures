class TreeNode:
    def __init__(self, value) -> None:
        self.value = value
        self.right = None
        self.left = None

class BinarySearchTree:
    def __init__(self) -> None:
        self.root = None

    def insert_node(self, value):
        self.root = self._insert_node_recursive(self.root, value)

    def _insert_node_recursive(self, root, value):        
        if root is None:
            return TreeNode(value)
        
        if value < root.value:
            root.left = self._insert_node_recursive(root.left, value)

        elif value > root.value:
            root.right = self._insert_node_recursive(root.right, value)

        return root
    
    def delete_node(self, value):
        self._delete_node_recursive(self.root, value)

    def _delete_node_recursive(self, root, value):
        if root is None:
            return root
        
        if value < root.value:
            root.left = self._delete_node_recursive(root.left, value)
        
        elif value > root.value:
            root.right = self._delete_node_recursive(root.right, value)

        else:
            if root.left is None:
                return root.right
            
            elif root.right is None:
                return root.left
            
            root.value = self._min_value_node(root.left).value
            root.right = self._delete_node_recursive(root.right, root.value)
        
        return root

    def _min_value_node(self, node):
        current = node
        while current:
            current = current.left

        return current
    
    def search_node(self, value):
        return self._search_node_recursive(self.root, value)

    def _search_node_recursive(self, root, value):
        if root is None or value == root.value:
            return root

        if value < root.value:
            return self._search_node_recursive(root.left, value)

        else:
            return self._search_node_recursive(root.right, value) 
    
    def inorder_traversal(self):
        self._inorder_traversal_recursive(self.root)

    def _inorder_traversal_recursive(self, node):
        if node is not None:
            self._inorder_traversal_recursive(node.left)
            print(node.value, end=" ")
            self._inorder_traversal_recursive(node.right)

    def preorder_traversal(self):
        self._preorder_traversal_recursive(self.root)

    def _preorder_traversal_recursive(self, node):
        if node is not None:
            print(node.value, end=" ")
            self._preorder_traversal_recursive(node.left)
            self._preorder_traversal_recursive(node.right)

    def postorder_traversal(self):
        self._postorder_traversal_recursive(self.root)

    def _postorder_traversal_recursive(self, node):
        if node is not None:
            self._postorder_traversal_recursive(node.left)
            self._postorder_traversal_recursive(node.right)
            print(node.value, end=" ")


BST = BinarySearchTree()
values = [10, 30, 50, 20, 40, 40, 10, 90, 70, 80, 30]
for value in values:
    BST.insert_node(value)

print("In-Order Traversal: ")
BST.inorder_traversal()

print("\n\nPre-Order Traversal: ")
BST.preorder_traversal()

print("\n\nPost-Order Traversal: ")
BST.postorder_traversal()

print("\n\nDeleting Node...")
BST.delete_node(20)
BST.inorder_traversal()

search_value = 30
result = BST.search_node(search_value)
if result:
    print(f"\n\nThe search value: {search_value} is found in the tree!")
else:
    print(f"\n\nThe search value {search_value} is not found in the tree!")