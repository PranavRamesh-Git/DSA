#MIN HEAP
class Minheap():
    def __init__(self,values=None):
        self.heap = list(values) if values is not None else []
        self.heapify()

    def sift_up(self,i):
        while i > 0:
            parent = (i - 1) // 2
            if(self.heap[parent] <= self.heap[i]):
                break
            self.heap[i],self.heap[parent] = self.heap[parent],self.heap[i]
            i = parent

    def sift_down(self,i):
        n = len(self.heap)
        while True:
            smallest = i
            left = i * 2 + 1
            right = i * 2 + 2
            if(left < n   and self.heap[left] < self.heap[smallest]):
                smallest = left
            if(right < n   and self.heap[right] < self.heap[smallest]):
                smallest = right

            if(i == smallest):
                break

            self.heap[smallest],self.heap[i] = self.heap[i],self.heap[smallest]
            i = smallest

    def push(self,i):
        self.heap.append(i)
        n = len(self.heap) - 1
        self.sift_up(n)

    def pop(self):
        n = len(self.heap)
        if n == 0:
            raise IndexError("Heap is empty")
        minimum = self.heap[0]
        last = self.heap.pop()
        if self.heap:
            self.heap[0] = last
            self.sift_down(0)
        return minimum
    def peek(self):
        n = len(self.heap)
        if n == 0:
            return None
        return self.heap[0]
    def heapify(self):
        n = len(self.heap)
        for i in range(n // 2 - 1, -1,-1):
            self.sift_down(i)

#MAX HEAP
class MaxHeap:
    def __init__(self,values=None):
        self.heap = list(values) if values is not None else []
        self.heapify()

    def sift_up(self,i):
        while i > 0:
            parent = (i - 1) // 2
            if(self.heap[parent] >= self.heap[i]):
                break
            self.heap[i],self.heap[parent] = self.heap[parent],self.heap[i]
            i = parent

    def sift_down(self,i):
        n = len(self.heap)
        while True:
            largest = i
            left = i * 2 + 1
            right = i * 2 + 2

            if(left < n and self.heap[left] > self.heap[largest]):
                largest = left
            if(right < n and self.heap[right] > self.heap[largest]):
                largest = right

            if(largest == i):
                break

            self.heap[largest], self.heap[i] = self.heap[i],self.heap[largest]
            i = largest

    def push(self,i):
        self.heap.append(i)
        n = len(self.heap) - 1
        self.sift_up(n)

    def pop(self):
        if not self.heap:
            raise IndexError("heap is empty")
        maximum = self.heap[0]
        last = self.heap.pop()

        if self.heap:
            self.heap[0] = last
            self.sift_down(0)
        return maximum

    def peek(self):
        if not self.heap:
            return None
        return self.heap[0]

    def heapify(self):
        n = len(self.heap)
        for i in range(n // 2 - 1, -1,-1):
            self.sift_down(i)

    def extend(self,values):
        self.heap.extend(values)
        self.heapify()

    def __repr__(self):
        return f"{self.heap}"

#HEAP SORT
def heapSort(heap):
    def sift_down(i,n):
        while True:
            largest = i
            left = i * 2 + 1
            right = i * 2 + 2

            if(left < n and heap[left] > heap[largest]):
                largest = left
            if(right < n and heap[right] > heap[largest]):
                largest = right

            if(largest == i):
                break

            heap[largest], heap[i] = heap[i],heap[largest]
            i = largest

    n = len(heap)

    for i in range(n // 2 -1,-1,-1):
        sift_down(i,n)

    for i in range(n-1, 0 , -1):
        heap[0],heap[i] = heap[i],heap[0]
        sift_down(0,i)

    return heap



if __name__ == '__main__':
    h = Minheap()
    h.push(8)
    h.push(5)
    h.push(2) 
    h.push(1)
    h.push(10)
    h.heap.extend([6,7,12]) # or we can just do values = [6,7,12] for val in values: self.h.push(val)
    print(h.heap)
    print(h.pop())
    print(h.peek())          



        
    
