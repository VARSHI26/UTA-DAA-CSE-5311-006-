import ctypes
class HashNode:
    __st__ = ('k', 'v', 'n', 'p') 
    def __init__(s, k, v):
        s.k = k
        s.v = v
        s.n = None
        s.p = None
class HashTable:
    def __init__(s, ini_cap=8):
        if ini_cap < 1:
            raise ValueError("Initial capacity must be positive")
        s.cap = ini_cap
        s.size = 0
        s.table = (ctypes.py_object * s.cap)()
        for i in range(s.cap):
            s.table[i] = None  
        s.inc_th = 0.75
        s.dec_th = 0.25
        s.min_cap = 8
        s._h_c = (5**0.5 - 1) / 2  
    def _h(s, k):
        if not isinstance(k, int):
            raise TypeError("Keys must be integers")
        return int(s.cap * ((k * s._h_c) % 1))
    def set_hash_function(s, c=None):
        if c is None:
            c = float(input("Enter new hash constant: "))
        if not (0 < c < 1):
            raise ValueError("Hash constant should be between 0 and 1")
        s._h_c = c
        s._resize(s.cap)  
    def insert(s, k, v):
        index = s._h(k)
        new_node = HashNode(k, v)
        if s.table[index] is None:
            s.table[index] = new_node
        else:
            curr = s.table[index]
            while curr:
                if curr.k == k:
                    curr.v = v
                    return
                if curr.n is None:
                    break
                curr = curr.n
            curr.n = new_node
            new_node.prev = curr
        s.size += 1
        if s.size >= s.cap * s.inc_th:
            s._resize(s.cap * 2)
    def get(s, k):
        index = s._h(k)
        curr = s.table[index]
        while curr:
            if curr.k == k:
                return curr.v
            curr = curr.n
        return -1  
    def remove(s, k):
        index = s._h(k)
        curr = s.table[index]
        while curr:
            if curr.k == k:
                if curr.p:
                    curr.p.n = curr.n
                else:
                    s.table[index] = curr.n
                if curr.n:
                    curr.n.p = curr.p
                s.size -= 1
                if (s.cap > s.min_cap and 
                    s.size <= s.cap * s.dec_th):
                    s._resize(max(s.min_cap, s.cap // 2))
                return
            curr = curr.n
        print(f"Key {k} not found")
    def _resize(s, new_cap):
        old_table = s.table
        old_cap = s.cap
        s.cap = new_cap
        s.table = (ctypes.py_object * s.cap)()
        for i in range(s.cap):
            s.table[i] = None
        s.size = 0  
        for i in range(old_cap):
            curr = old_table[i]
            while curr:
                n_node = curr.n
                s.insert(curr.k, curr.v)
                curr = n_node
        print(f"Table resized to {new_cap}")
    def display(s):
        print("\nHash Table:")
        for i in range(s.cap):
            print(f"index {i}:", end="")
            curr = s.table[i]
            while curr:
                print(f" -> {curr.k}:{curr.v}", end="")
                curr = curr.n
            print()
if __name__ == "__main__":
    ht = HashTable(6)
    o = [
        ('insert', 5, 100),
        ('insert', 4, 90),
        ('remove', 11, None),
        ('insert', 11, 70),
        ('insert', 66, 30),
        ('insert', 33, 88),
        ('insert', 45, 76),
        ('insert', 54, 88)
    ]
    for op, k, v in o:
        if op == 'insert':
            ht.insert(k, v)
            print(f"Inserted k {k}")
        elif op == 'remove':
            ht.remove(k)
    print(f"Value for k 33: {ht.get(33)}")
    ht.display()


