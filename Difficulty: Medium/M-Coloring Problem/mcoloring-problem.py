# User function Template for python3

class Solution:
    def graphColoring(self, v, edges, m):
        # code here
        graph={node:[] for node in range(v)}
        for n,nbr in edges:
            graph[n].append(nbr)
            graph[nbr].append(n)
        def issafe(ve,ca,c):
            for nbr in graph[ve]:
                if ca[nbr]==c:
                    return False
            return True
        def solve(ve,ca):
            if ve==v:
                return True
            for i in range(m):
                if issafe(ve,ca,i):
                    ca[ve]=i
                    if solve(ve+1,ca):
                        return True
                    ca[ve]=-1
            return False
        ca=[-1]*v
        return solve(0,ca)
        


#{ 
 # Driver Code Starts
def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        edges_input = list(map(int, input().split()))
        m = int(input())
        edges = []

        # Populate the edges list with edge pairs
        for i in range(0, len(edges_input), 2):
            edges.append((edges_input[i], edges_input[i + 1]))

        solution = Solution()
        print("true" if solution.graphColoring(n, edges, m) else
              "false")  # Call the graph coloring function
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends