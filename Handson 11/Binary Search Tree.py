class N:
    def __init__(s, k):
        s.k = k
        s.l = None
        s.r = None
class BST:
    def __init__(s):
        s.rt = None
    def insert(s, rt, k):
        if rt is None:
            return N(k)
        if k < rt.k:
            rt.l = s.insert(rt.l, k)
        elif k > rt.k:
            rt.r = s.insert(rt.r, k)
        return rt
    def search(s, rt, k):
        if rt is None or rt.k == k:
            return rt
        if k > rt.k:
            return s.search(rt.r, k)
        return s.search(rt.l, k)
    def delete(s, rt, k):
        if rt is None:
            return rt
        if k < rt.k:
            rt.l = s.delete(rt.l, k)
        elif k > rt.k:
            rt.r = s.delete(rt.r, k)
        else:
            if rt.l is None:
                return rt.r
            elif rt.r is None:
                return rt.l
            temp = rt.r
            while temp.l is not None:
                temp = temp.l
            rt.k = temp.k
            rt.r = s.delete(rt.r, temp.k)
        return rt
    def inorder_traversal(s, rt):
        if rt:
            s.inorder_traversal(rt.l)
            print(rt.k, end=" ")
            s.inorder_traversal(rt.r)
def test_bst():
    print("Testing Binary Search Tree")
    bst = BST()
    keys = [21, 16, 4, 40, 10, 90, 74]
    for k in keys:
        bst.rt = bst.insert(bst.rt, k)
    print("\nSearch operations:")
    test_keys = [6, 10]
    for k in test_keys:
        result = bst.search(bst.rt, k)
        print(f"Search {k}: {'Found' if result else 'Not found'}")
    print("\nDelete node 10")
    bst.rt = bst.delete(bst.rt, 10)
    result = bst.search(bst.rt, 10)
    print(f"Search 10 after deletion: {'Found' if result else 'Not found'}")
    print("\n Final BST:")
    bst.inorder_traversal(bst.rt)
    print("\n")
if __name__ == "__main__":
    test_bst()
