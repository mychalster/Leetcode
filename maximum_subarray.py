class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxSubArray(self, A):
        if len(A)==1: return A
        s=[]
        addsum=0
        for i in A:
            addsum=addsum+i
            s.append(addsum)
        p=s.index(min(s))
        q=s.index(max(s))
        
        if p<q:
            l=[]
            for j in range(p+1,q+1):
                l.append(A[j])
            return l
            
        if p>q:
            A1=A[p:]
            A2=A[:q+1]
            if sum(self.maxSubArray(A1))>sum(self.maxSubArray(A2)):
                return self.maxSubArray(A1)
            else:
                return self.maxSubArray(A2)


