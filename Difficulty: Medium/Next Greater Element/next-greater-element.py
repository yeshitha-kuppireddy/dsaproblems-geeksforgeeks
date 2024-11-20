# User function Template for python3

class Solution:
    # Function to find the next greater element for each element of the array.
    def nextLargerElement(self, arr):
        n=len(arr)
        r=[-1]*n
        for i in range(n):
            for j in range(i,n):
                if arr[j]>arr[i]:
                    r[i]=arr[j]
                    break
        return r

#{ 
 # Driver Code Starts
# Initial Template for Python 3

t = int(input())  # number of test cases
for _ in range(t):
    arr = list(map(int, input().split()))  # input array
    s = Solution().nextLargerElement(arr)  # find the next greater elements

    # Output formatting
    if s:
        print(" ".join(map(str, s)))  # Print next greater elements
    else:
        print("[]")  # Print empty list if no next greater element is found
    print("~")
# } Driver Code Ends