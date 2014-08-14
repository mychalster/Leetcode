def merge(A, m, B, n):
        i=0;j=0
        if len(A)==0: return B
        if len(B)==0: return A
        
        while j<n and i<len(A):
            if A[i]>B[j]: 
                A.insert(i,B[j])
                j+=1
                i+=1
            else: i+=1
        if j==n: return A
        else: 
            A.extend(B[j:n])
            return A
