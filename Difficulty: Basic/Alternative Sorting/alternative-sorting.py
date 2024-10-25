class Solution:
    def alternateSort(self,arr):
        arr.sort()  # Sort the array
        na = []
        while arr:
            if arr:  # Add the largest element
                na.append(arr.pop(-1))
            if arr:  # Add the smallest element
                na.append(arr.pop(0))
        return na
        # Your code goes here


#{ 
 # Driver Code Starts
#Initial Template for Python 3
#Position this line where user code will be pasted.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.alternateSort(arr)
        print(*ans)
        print("~")
        t -= 1

# } Driver Code Ends