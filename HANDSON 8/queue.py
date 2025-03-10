from queueinterface import QueueInterface
class Queue(QueueInterface):
    def __init__(s, m_s=30):
        s.m_s = m_s  
        s.arr = [None] * m_s  
        s.f = -1  
        s.r = -1  
    def is_empty(s):
        return s.f > s.r or s.f == -1
    def enqueue(s, data):
        if s.r < s.m_s - 1:
            s.r += 1
            s.arr[s.r] = data
            if s.f == -1:
                s.f = 0
        else:
            print("Queue Overflow, exceeded max size", s.m_s)
    def dequeue(s):
        if s.is_empty():
            print("Queue is empty")
        else:
            s.f += 1
            if s.f > s.r:
                s.f = s.r = -1
    def peek(s):
        if s.is_empty():
            print("Queue is empty")
            return -1  
        else:
            return s.arr[s.f]
if __name__ == "__main__":
    que = Queue()
    que.enqueue(99)
    que.enqueue(18)
    que.dequeue()
    que.enqueue(30)
    print(que.peek())  
    print("Is Queue empty:", que.is_empty())


#output
#18
#Is Queue empty: False
