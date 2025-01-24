class Solution:
    def leaders(self, arr):
        # code here
        m=arr[-1]
        sol=[]
        for i in range(len(arr)-1,-1,-1):
            if arr[i]>=m:
                m=arr[i]
                sol.append(arr[i])
        return sol[::-1]


#{ 
 # Driver Code Starts
t = int(input())  # number of test cases
for _ in range(t):
    arr = list(map(int, input().split()))  # input array
    s = Solution().leaders(arr)  # find the leaders

    # Output formatting
    if s:
        print(" ".join(map(str, s)))  # Print leaders in the required order
    else:
        print("[]")  # Print empty list if no leaders are found

    print("~")

# } Driver Code Ends