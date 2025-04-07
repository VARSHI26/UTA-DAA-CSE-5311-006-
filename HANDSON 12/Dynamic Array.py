class DynamicArray:
    def __init__(s, ini_cap=5):
        s.cap = ini_cap
        s.size = 0  
        s.arr = [0] * s.cap  
    def __resize(s, new_cap):
        new_arr = [0] * new_cap
        for i in range(s.size):
            new_arr[i] = s.arr[i]
        s.arr = new_arr
        s.cap = new_cap
    def insert(s, el):
        if s.size == s.cap:
            s.__resize(2 * s.cap)  
        s.arr[s.size] = el
        s.size += 1
    def delete(s, el=None):
        if el is not None:
            found = False
            for i in range(s.size):
                if not found and s.arr[i] == el:
                    found = True
                    s.size -= 1
                if found and i < s.size:
                    s.arr[i] = s.arr[i + 1] if (i + 1 < s.size) else 0
        else:
            if s.size > 0:
                s.arr[s.size - 1] = 0
                s.size -= 1
    def print_array(s):
        for i in range(s.size):
            print(s.arr[i], end=" ")
        print()
if __name__ == "__main__":
    numbers = DynamicArray(5)
    numbers.insert(10)
    numbers.insert(20)
    numbers.insert(30)
    numbers.insert(40)
    numbers.insert(50)
    numbers.print_array()   
    numbers.insert(60)
    numbers.insert(70)
    numbers.insert(80)
    numbers.print_array()  
    numbers.delete(50)
    numbers.delete()
    numbers.print_array()  
