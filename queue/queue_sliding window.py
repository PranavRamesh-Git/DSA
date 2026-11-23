from collections import deque

def sliding_window(nums, k):
    q = deque()
    ans = []

    for i,num in enumerate(nums):
        while q and q[0] < i - k - 1:
            q.popleft()
        
        while q and nums[q[-1]] < num:
            q.pop()
            
        q.append(i)

        if i >=  k - 1:
            ans.append(nums[q[0]])
    return ans



def shortest_subarray(nums,k):
    ans = float("inf")
    q = deque()
    prefix = [0] * (len(nums) + 1)

    for i in range(len(nums)):
        prefix[i + 1] = prefix[i] + nums[i]
    
    for j in range(len(nums) + 1):
        while q and prefix[j] - prefix[q[0]] >= k:
            ans = min(ans,j - q[0])
            q.popleft()
        
        while q and prefix[j] <= prefix[q[-1]]:
            q.pop()
        
        q.append(j)
    
    if ans != float("inf"):
        return ans
    return -1


if __name__ == "__main__":
    arr = [1,3,-1,-3,5,3,6,7]
    k = 3
    print(sliding_window(arr,k))

    nums = [2,-1,2]
    k = 3
    print(shortest_subarray(nums,k))