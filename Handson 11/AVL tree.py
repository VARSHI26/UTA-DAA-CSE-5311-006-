class Node:
    def __init__(self, value):
        self.value = value
        self.height = 1
        self.left = None
        self.right = None
class AVLTree:
    def __init__(self):
        self.root = None
    def height(self, node):
        if node is None:
            return 0
        return node.height
    def balance_factor(self, node):
        if node is None:
            return 0
        return self.height(node.right) - self.height(node.left)
    def update_height(self, node):
        node.height = max(self.height(node.left), self.height(node.right)) + 1
    def rotate_left(self, x):
        y = x.right
        T2 = y.left
        y.left = x
        x.right = T2
        self.update_height(x)
        self.update_height(y)
        return y
    def rotate_right(self, y):
        x = y.left
        T2 = x.right
        x.right = y
        y.left = T2
        self.update_height(y)
        self.update_height(x)
        return x
    def balance(self, node):
        self.update_height(node)
        balance = self.balance_factor(node)
        if balance > 1:
            if self.balance_factor(node.right) < 0:  
                node.right = self.rotate_right(node.right)
                return self.rotate_left(node)
            else:  
                return self.rotate_left(node)
        if balance < -1:
            if self.balance_factor(node.left) > 0:  
                node.left = self.rotate_left(node.left)
                return self.rotate_right(node)
            else:  
                return self.rotate_right(node)
        return node
    def insert(self, root, key):
        if root is None:
            return Node(key)
        if key < root.value:
            root.left = self.insert(root.left, key)
        elif key > root.value:
            root.right = self.insert(root.right, key)
        else:
            return root  
        return self.balance(root)
    def find_min(self, node):
        while node.left is not None:
            node = node.left
        return node
    def delete(self, root, key):
        if root is None:
            return root
        if key < root.value:
            root.left = self.delete(root.left, key)
        elif key > root.value:
            root.right = self.delete(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            else:
                temp = self.find_min(root.right)
                root.value = temp.value
                root.right = self.delete(root.right, temp.value)
        return self.balance(root)
    def search(self, root, key):
        if root is None or root.value == key:
            return root
        if key < root.value:
            return self.search(root.left, key)
        return self.search(root.right, key)
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.value, end=" ")
            self.inorder(root.right)
def test_avl_tree():
    print("Testing AVL Tree")
    avl = AVLTree()
    keys = [6, 4, 16, 18, 28, 11, 39]
    for key in keys:
        avl.root = avl.insert(avl.root, key)
        print(f"Inserted {key}")
    print("\nSearch for 6:", "Found" if avl.search(avl.root, 6) else "Not found")
    print("Search for 50:", "Found" if avl.search(avl.root, 50) else "Not found")
    print("\nDeleting 6...")
    avl.root = avl.delete(avl.root, 6)
    print("Search for 6 after deletion:", "Found" if avl.search(avl.root, 6) else "Not found")
    print("\nInorder traversal (sorted order):", end=" ")
    avl.inorder(avl.root)
    print()
if __name__ == "__main__":
    test_avl_tree()
