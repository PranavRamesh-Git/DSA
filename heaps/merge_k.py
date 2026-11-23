"""
arrays = [
    [1, 4, 7],
    [2, 5],
    [3, 6, 9]
]
"""
import heapq

def merge_k(arrays):
    result = []
    h = []
    for i,arr in enumerate(arrays):
        if arr:
            heapq.heappush(h,(arr[0],i,0))


    while h:
        value,i,j = heapq.heappop(h)
        result.append(value)
        if j + 1 < len(arrays[i]):
            heapq.heappush(h,(arrays[i][j+1],i,j+1))

    print(result)

if __name__ == '__main__':
    arrays = [
        [1, 4, 7],
        [2, 5],
        [3, 6, 9]  
    ]
    merge_k(arrays)


