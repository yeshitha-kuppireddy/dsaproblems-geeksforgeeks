from typing import List

class Solution:
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
		visited=[False]*V
		def dfs(node,parent):
		    visited[node]=True
		    for i in adj[node]:
		        if not visited[i]:
		            if dfs(i,node):
		                return True
		        elif i!=parent:
		            return True
		    return False
	    for i in range(V):
	        if not visited[i]:
	            if dfs(i,-1):
	                return True
        return False

#{ 
 # Driver Code Starts
if __name__ == '__main__':

    T = int(input())
    for i in range(T):
        V, E = map(int, input().split())
        adj = [[] for i in range(V)]
        for _ in range(E):
            u, v = map(int, input().split())
            adj[u].append(v)
            adj[v].append(u)
        obj = Solution()
        ans = obj.isCycle(V, adj)
        if (ans):
            print("1")
        else:
            print("0")
        print("~")

# } Driver Code Ends