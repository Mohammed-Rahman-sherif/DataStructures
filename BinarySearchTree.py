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