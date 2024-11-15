#User function Template for python3
class Solution:
    def getSecondLargest(self, arr):
        # Code Here
        n = len(arr)
    
    # Sort the array in non-decreasing order
        arr.sort()
      
        # start from second last element as last element is the largest
        for i in range(n - 2, -1, -1):
          
            # return the first element which is not equal to the 
            # largest element
            if arr[i] != arr[n - 1]:
                return arr[i]
        
        # If no second largest element was found, return -1
        return -1


#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.getSecondLargest(arr)
        print(ans)
        print("~")
# } Driver Code Ends