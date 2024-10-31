from typing import List
def ones(num):
    count = 0
    [0,1]
    
class Solution:
    def countBits(self, n : int) -> List[int]:
        # code here
        ans = [0] * (n + 1)
        for i in range(1, n + 1):
            ans[i] = ans[i >> 1] + (i & 1)  # Shift right and check last bit
        return ans



#{ 
 # Driver Code Starts
class IntArray:

    def __init__(self) -> None:
        pass

    def Input(self, n):
        arr = [int(i) for i in input().strip().split()]  #array input
        return arr

    def Print(self, arr):
        for i in arr:
            print(i, end=" ")
        print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        n = int(input())

        obj = Solution()
        res = obj.countBits(n)

        IntArray().Print(res)
        print("~")

# } Driver Code Ends