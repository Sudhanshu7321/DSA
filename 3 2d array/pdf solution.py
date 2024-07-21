class Solution:
    
    @staticmethod 
    def q1(matrix):
        count = 0 
        
        row = len(matrix)
        col = len(matrix[0])
        
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 7:
                    count += 1
        return count
    
    def q2(matrix):
        sum = 0
        col = len(matrix[0])
        for i in range(col):
            sum += matrix[1][i]
        return sum    
    
    def q3():
        # Transposed Matrix
        return 

    
matrix = [[4,7,8],[8,8,7],[7,6,2]]
# print(Solution.q1(matrix))   
print(Solution.q2(matrix))             