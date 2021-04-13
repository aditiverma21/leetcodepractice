
def oddCells(n, m, indices):
        matrix=[[0 for x in range(m)] for y in range(n)]
        print(matrix)
        for i in range(len(indices)):
            r=indices[i][0]
            c=indices[i][1]
            for j in range(m):
                print(str(matrix[r][j]))
                matrix[r][j]+=1
            
            for k in range(n):
                matrix[k][c]+=1
        count=0
        for i in range(n): 
            for j in range(m):
                if matrix[i][j]%2!=0:
                    count+=1
        return count
        
res=oddCells(2,3,[[0,1],[1,1]])
print(res)