from typing import List, TypeVar, Generic
T = TypeVar('T')
class MinHeap(Generic[T]):
    def __init__(self):
        self.heap: List[T] = []
    def p_n(self, i: int) -> int:
        return (i - 1) // 2
    def l_n(self, i: int) -> int:
        return 2 * i + 1
    def r_n(self, i: int) -> int:
        return 2 * i + 2
    def validate_swap(self, i: int, j: int) -> bool:
        return 0 <= i < len(self.heap) and 0 <= j < len(self.heap) and self.heap[i] > self.heap[j]
    def swap_nodes(self, i: int, j: int):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
    def heapify_up(self, i: int):
        p = self.p_n(i)
        if i > 0 and self.validate_swap(p, i):
            self.swap_nodes(p, i)
            self.heapify_up(p)
    def heapify_down(self, i: int):
        small = i
        l, r = self.l_n(i), self.r_n(i)
        if l < len(self.heap) and self.validate_swap(small, l):
            small = l
        if r < len(self.heap) and self.validate_swap(small, r):
            small = r
        if small != i:
            self.swap_nodes(small, i)
            self.heapify_down(small)
    def get_root_node(self):
        return self.heap[0] if self.heap else None
    def push_node(self, element: T):
        self.heap.append(element)
        self.heapify_up(len(self.heap) - 1)
    def pop_root(self):
        if self.heap:
            root = self.heap[0]
            self.heap[0] = self.heap[-1]
            self.heap.pop()
            self.heapify_down(0)
            return root
        return None
    def build_heap(self, array: List[T]):
        self.heap = array[:]
        for i in range(len(self.heap) // 2 - 1, -1, -1):
            self.heapify_down(i)
    def __repr__(self):
        return str(self.heap)
# Testing
if __name__ == "__main__":
    # Integer Heap
    heap_int = MinHeap[int]()
    arr_int = [68, 86, 44, 31, 99, 12, 75, 98]
    heap_int.build_heap(arr_int)
    print("Initial Integer heap:", heap_int)
    heap_int.push_node(21)
    print("Heap after adding an element: 21 ->", heap_int)
    print("Popping Root:", heap_int.pop_root(), "->", heap_int)
    # Float Heap
    heap_float = MinHeap[float]()
    arr_float = [118.4, 56.2, 161.1, 84.3, 238.6, 31.7, 75.3, 85.9]
    heap_float.build_heap(arr_float)
    print("\nInitial Float heap:", heap_float)
    heap_float.push_node(67.1)
    print("Heap after adding an element: 67.1 ->", heap_float)
    heap_float.push_node(45.1)
    print("Heap after adding an element: 45.1 ->", heap_float)
    print("Popping Root:", heap_float.pop_root(), "->", heap_float)
    print("Popping Root:", heap_float.pop_root(), "->", heap_float)
    # Custom StudentMarks Heap
    class StudentMarks:
        def __init__(self, name: str, marks: int):
            self.name = name
            self.marks = marks
        def __lt__(self, other):
            return self.marks < other.marks
        def __gt__(self, other):
            return self.marks > other.marks
        def __repr__(self):
            return f"Student(name: {self.name}, marks: {self.marks})"
    heap_student = MinHeap[StudentMarks]()
    students = [
        StudentMarks("Hema", 60),
        StudentMarks("varshitha", 85),
        StudentMarks("vivek", 70),
        StudentMarks("sanvi", 95),
        StudentMarks("sathvi", 90)
    ]
    heap_student.build_heap(students)
    print("\nInitial Student heap:", heap_student)
    print("Popping Root:", heap_student.pop_root())
    print("Heap structure:", heap_student)
