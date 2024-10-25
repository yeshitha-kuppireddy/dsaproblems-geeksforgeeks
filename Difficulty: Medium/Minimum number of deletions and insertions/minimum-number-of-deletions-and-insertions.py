#User function Template for python3
def findlcs(X,Y):
        m = len(X)
        n = len(Y)
    
        # Create a 2D array to store lengths of longest common subsequence.
        # (m+1) x (n+1) to account for the empty subsequences.
        L = [[0] * (n + 1) for _ in range(m + 1)]
    
        # Build the L table in bottom-up fashion
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if X[i - 1] == Y[j - 1]:
                    L[i][j] = L[i - 1][j - 1] + 1
                else:
                    L[i][j] = max(L[i - 1][j], L[i][j - 1])
    
        # The length of LCS is in L[m][n]
        return L[m][n]
class Solution:
    
            
	def minOperations(self, str1, str2):
		# code here
		return len(str1)+len(str2)-2*findlcs(str1,str2)
		


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        s1, s2 = input().split()
        ob = Solution()
        ans = ob.minOperations(s1, s2)
        print(ans)

# } Driver Code Ends