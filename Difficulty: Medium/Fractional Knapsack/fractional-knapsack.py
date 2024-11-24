#User function Template for python3
class Solution:
    # Function to get the maximum total value in the knapsack.
    def fractionalknapsack(self, p, w, c):
        #code here
        n=len(p)
        if n==0 or c==0:
            return -1
        pv=0.0
        pw=[(p[i]/w[i],i) for i in range(n)]
        pw.sort(reverse=True,key=lambda x:x[0])
        rc=c
        for r,j in pw:
            if rc==0:
                break
            ws=w[j]
            ps=p[j]
            tw=min(rc,ws)
            rc-=tw
            pv+=(tw/ws)*ps
        #print(f"knapsack filled {c-rc}")
        return pv

#{ 
 # Driver Code Starts
#Position this line where user code will be pasted.

if __name__ == '__main__':
    test_cases = int(input())
    for _ in range(test_cases):
        # Read values array
        values = list(map(int, input().strip().split()))

        # Read weights array
        weights = list(map(int, input().strip().split()))

        # Read the knapsack capacity
        W = int(input().strip())

        ob = Solution()
        print("%.6f" % ob.fractionalknapsack(values, weights, W))
        print("~")

# } Driver Code Ends