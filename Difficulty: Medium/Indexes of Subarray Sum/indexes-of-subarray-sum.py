#User function Template for python3
class Solution:
    def subArraySum(self, arr, target):
        # code here
        cs = 0  # Current sum of the window
        start = 0  # Start index of the window
        for end in range(len(arr)):
            cs += arr[end]  # Add the current element to the current sum
    
            # Shrink the window from the left if the current sum is too large
            while cs > target and start <= end:
                cs -= arr[start]
                start += 1
    
            # Check if the current sum equals the target
            if cs == target:
                return [start+1, end+1]
    
        return [-1]


#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input().strip())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        d = int(input().strip())
        ob = Solution()
        result = ob.subArraySum(arr, d)
        print(" ".join(map(str,
                           result)))  # Print the result in the desired format
        tc -= 1
        print("~")

# } Driver Code Ends