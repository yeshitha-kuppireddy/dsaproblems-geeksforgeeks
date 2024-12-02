#User function Template for python3

class Solution:
    # Function to return max value that can be put in knapsack of capacity.
    def knapSack(self, capacity, val, wt):
        # code here
        n=len(val)
        dp=[[0]*(capacity+1) for _ in range(n+1)]
        for i in range(n+1):
            for j in range(1,capacity+1):
                if wt[i-1]<=j:
                    dp[i][j]=max(dp[i-1][j],val[i-1]+dp[i-1][j-wt[i-1]])
                else:
                    dp[i][j]=dp[i-1][j]
        return dp[n][capacity]
        

#{ 
 # Driver Code Starts
if __name__ == '__main__':
    test_cases = int(input())
    for _ in range(test_cases):
        # Read capacity
        capacity = int(input())
        values = list(map(
            int,
            input().strip().split()))  # Using 'values' instead of 'val'
        weights = list(map(
            int,
            input().strip().split()))  # Using 'weights' instead of 'wt'
        ob = Solution()
        print(ob.knapSack(capacity, values, weights))
        print("~")

# } Driver Code Ends