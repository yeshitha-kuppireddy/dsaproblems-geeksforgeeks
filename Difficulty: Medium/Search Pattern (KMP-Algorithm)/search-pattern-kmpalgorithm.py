#User function Template for python3

class Solution:
    def search(self, pat, txt):
        # code here
        cur=txt[:len(pat)]
        ocs=[]
        if cur==pat:
            ocs.append(0)
        for i in range(len(pat),len(txt)):
            cur = cur[1:] + txt[i]
            if cur == pat:
                ocs.append(i - len(pat) + 1)
        return ocs


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input().strip()
        patt = input().strip()
        ob = Solution()
        ans = ob.search(patt, s)
        if len(ans) == 0:
            print("[]", end="")
        for value in ans:
            print(value, end=' ')
        print()

# } Driver Code Ends