from stackinterface import StackInterface
class Stack(StackInterface):
    def __init__(s, m_s=30):
        s.m_s = m_s  
        s.arr = [None] * m_s  
        s.top = -1  
    def push(s, d):
        if s.top < s.m_s - 1:
            s.top += 1
            s.arr[s.top] = d
        else:
            print("Stack Overflow, exceeded max size", s.m_s)
    def pop(s):
        if s.is_empty():
            print("Stack is empty")
        else:
            s.top -= 1
    def peek(s):
        if s.is_empty():
            print("Stack is empty")
            return -1  
        else:
            return s.arr[s.top]
    def is_empty(s):
        return s.top == -1
if __name__ == "__main__":
    s = Stack()
    s.push(16)
    s.push(9)
    s.pop()
    s.push(11)
    print(s.peek())  
    print("Is Stack empty:", s.is_empty())  
    s.pop()
    s.pop()
    print("Is Stack empty:", s.is_empty())



#output
#11
#Is Stack empty: False
#Is Stack empty: True



