from linkedlistinterface import LinkedListInterface
class N:
    def __init__(self, d, n_i):
        self.d = d  
        self.n_i = n_i  
    def __repr__(self):
        return f"N@{hex(id(self))}"
class LinkedList(LinkedListInterface):
    def __init__(self, m_s=100):
        self.m_s = m_s  
        self.ns = [N(None, -1) for _ in range(m_s)]  
        self.h_i = -1  
        self.f_l = 0  
        for i in range(m_s - 1):
            self.ns[i].n_i = i + 1
        self.ns[m_s - 1].n_i = -1
    def a_n(self):
        if self.f_l == -1:
            raise OverflowError("Out of memory")
        i = self.f_l
        self.f_l = self.ns[self.f_l].n_i
        return i
    def f_n(self, i):
        self.ns[i].n_i = self.f_l
        self.f_l = i
    def insert(self, d):
        i = self.a_n()
        self.ns[i].d = d
        self.ns[i].n_i = self.h_i
        self.h_i = i
    def delete(self, d):
        c_i = self.h_i
        p_i = -1
        while c_i != -1 and self.ns[c_i].d != d:
            p_i = c_i
            c_i = self.ns[c_i].n_i
        if c_i != -1:
            if p_i != -1:
                self.ns[p_i].n_i = self.ns[c_i].n_i
            else:
                self.h_i = self.ns[c_i].n_i
            self.f_n(c_i)
    def display(self):
        c_i = self.h_i
        while c_i != -1:
            print(self.ns[c_i].d, end=" ")
            c_i = self.ns[c_i].n_i
        print()
    def search(self, d):
        c_i = self.h_i
        while c_i != -1:
            if self.ns[c_i].d == d:
                return self.ns[c_i]  
            c_i = self.ns[c_i].n_i
        return None  
if __name__ == "__main__":
    ll = LinkedList()
    ll.insert(10)
    ll.insert(79)
    ll.delete(79)
    ll.insert(22)
    ll.insert(48)
    ll.display()  
    print("Search for 10:", ll.search(10))  
    print("Search for 15:", ll.search(15))



#output
#48 22 10 
#Search for 10: N@0x1c8bfa0b0e0
#Search for 15: None
