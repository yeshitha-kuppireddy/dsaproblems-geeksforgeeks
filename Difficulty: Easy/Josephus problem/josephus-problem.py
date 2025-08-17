
from collections import deque
class Solution:
    def josephus(self,n,k):
        
        l=[]
        for i in range(n):
            l.append(i+1)
        i=0
        k=k-1
        while len(l)!=1:
            i=(i+k)%len(l)
            l.remove(l[i])
            
            
        return l[0]   
        