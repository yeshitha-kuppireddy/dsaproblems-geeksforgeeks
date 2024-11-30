#User function Template for python3
class Solution:
    def nQueen(self, n):
        # code here
        '''b[0]b[1]b['''
        def issafe(b,row,col):
            for i in range(n):
                if b[i][col]:
                    return False
            for i,j in zip(range(row-1,-1,-1),range(col-1,-1,-1)):
                if b[i][j]:
                    return False
            for i,j in zip(range(row-1,-1,-1),range(col+1,n)):
                if b[i][j]:
                    return False
            return True
        def solve(b,row):
            if row==n:
                sol=[]
                for i in range(n):
                    for j in range(n):
                        if b[i][j]:
                            sol.append(j+1)
                sols.append(sol)
                return True
            for col in range(n):
                if issafe(b,row,col):
                    b[row][col]=True
                    solve(b,row+1)
                    b[row][col]=False
            return False
        b=[[False]*n for _ in range(n)]
        sols=[]
        solve(b,0)
        return sols
                    
                
        
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        ob = Solution()
        ans = ob.nQueen(n)
        if(len(ans) == 0):
            print("-1")
        else:
            for i in range(len(ans)):
                print("[",end="")
                for j in range(len(ans[i])):
                    print(ans[i][j],end = " ")
                print("]",end = " ")
            print()
                
        print("~")
# } Driver Code Ends