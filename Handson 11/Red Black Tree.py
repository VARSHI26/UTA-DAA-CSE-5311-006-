R = True
B = False
class N:
    def __init__(self, key, color=R):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None
        self.color = color
class RBT:
    def __init__(self):
        self.NIL = N(0, B)
        self.root = self.NIL
    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.NIL:
            y.left.parent = x
        y.parent = x.parent
        if x.parent == self.NIL:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y
    def right_rotate(self, y):
        x = y.left
        y.left = x.right
        if x.right != self.NIL:
            x.right.parent = y
        x.parent = y.parent
        if y.parent == self.NIL:
            self.root = x
        elif y == y.parent.right:
            y.parent.right = x
        else:
            y.parent.left = x
        x.right = y
        y.parent = x
    def insert_fixup(self, z):
        while z.parent.color == R:
            if z.parent == z.parent.parent.left:
                y = z.parent.parent.right
                if y.color == R:
                    z.parent.color = B
                    y.color = B
                    z.parent.parent.color = R
                    z = z.parent.parent
                else:
                    if z == z.parent.right:
                        z = z.parent
                        self.left_rotate(z)
                    z.parent.color = B
                    z.parent.parent.color = R
                    self.right_rotate(z.parent.parent)
            else:
                y = z.parent.parent.left
                if y.color == R:
                    z.parent.color = B
                    y.color = B
                    z.parent.parent.color = R
                    z = z.parent.parent
                else:
                    if z == z.parent.left:
                        z = z.parent
                        self.right_rotate(z)
                    z.parent.color = B
                    z.parent.parent.color = R
                    self.left_rotate(z.parent.parent)
        self.root.color = B
    def insert(self, key):
        z = N(key)
        z.left = self.NIL
        z.right = self.NIL
        
        y = self.NIL
        x = self.root
        while x != self.NIL:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.parent = y
        if y == self.NIL:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z
        self.insert_fixup(z)
    def transplant(self, u, v):
        if u.parent == self.NIL:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent
    def delete_fixup(self, x):
        while x != self.root and x.color == B:
            if x == x.parent.left:
                w = x.parent.right
                if w.color == R:
                    w.color = B
                    x.parent.color = R
                    self.left_rotate(x.parent)
                    w = x.parent.right
                if w.left.color == B and w.right.color == B:
                    w.color = R
                    x = x.parent
                else:
                    if w.right.color == B:
                        w.left.color = B
                        w.color = R
                        self.right_rotate(w)
                        w = x.parent.right
                    w.color = x.parent.color
                    x.parent.color = B
                    w.right.color = B
                    self.left_rotate(x.parent)
                    x = self.root
            else:
                w = x.parent.left
                if w.color == R:
                    w.color = B
                    x.parent.color = R
                    self.right_rotate(x.parent)
                    w = x.parent.left
                if w.right.color == B and w.left.color == B:
                    w.color = R
                    x = x.parent
                else:
                    if w.left.color == B:
                        w.right.color = B
                        w.color = R
                        self.left_rotate(w)
                        w = x.parent.left
                    w.color = x.parent.color
                    x.parent.color = B
                    w.left.color = B
                    self.right_rotate(x.parent)
                    x = self.root
        x.color = B
    def delete(self, key):
        z = self.search(key)
        if z == self.NIL:
            print("Key not found in the tree")
            return
        y = z
        y_original_color = y.color
        if z.left == self.NIL:
            x = z.right
            self.transplant(z, z.right)
        elif z.right == self.NIL:
            x = z.left
            self.transplant(z, z.left)
        else:
            y = self.minimum(z.right)
            y_original_color = y.color
            x = y.right
            if y.parent == z:
                x.parent = y
            else:
                self.transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            self.transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color
        if y_original_color == B:
            self.delete_fixup(x)
    def search(self, key):
        return self._search(self.root, key)
    def _search(self, node, key):
        if node == self.NIL or key == node.key:
            return node
        if key < node.key:
            return self._search(node.left, key)
        return self._search(node.right, key)
    def minimum(self, node):
        while node.left != self.NIL:
            node = node.left
        return node
    def maximum(self, node):
        while node.right != self.NIL:
            node = node.right
        return node
    def print_tree(self, node, indent="", last=True):
        if node != self.NIL:
            print(indent, end="")
            if last:
                print("R----", end="")
                indent += "     "
            else:
                print("L----", end="")
                indent += "|    "
            color = "R" if node.color == R else "B"
            print(f"{node.key}({color})")
            self.print_tree(node.left, indent, False)
            self.print_tree(node.right, indent, True)
def test_red_black_tree():
    print("Testing Red-Black Tree")
    rbt = RBT()
    keys = [25, 74, 52, 33, 11]
    for key in keys:
        rbt.insert(key)
    print("\nRed-Black Tree after insertions:")
    rbt.print_tree(rbt.root)
    print("\nSearch operations:")
    test_keys = [52, 100]
    for key in test_keys:
        result = rbt.search(key)
        if result != rbt.NIL:
            print(f"Key {key} found (Color: {'R' if result.color == R else 'B'})")
        else:
            print(f"Key {key} not found")
    print("\nDeleting key 52...")
    rbt.delete(52)
    print("Tree after deletion:")
    rbt.print_tree(rbt.root)
    result = rbt.search(52)
    print(f"\nSearch 52 after deletion: {'Found' if result != rbt.NIL else 'Not found'}")
if __name__ == "__main__":
    test_red_black_tree()
