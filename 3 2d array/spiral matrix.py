class Solution:
    
    @staticmethod
    def spiralMatrix(matrix):
        
        startRow = 0
        startCol = 0
        endRow = len(matrix)-1
        endCol = len(matrix[0])-1
        res = []
        while startRow <= endRow and startCol <= endCol:
            # top
            for j in range(startCol,endCol+1):
                res.append(matrix[startRow][j])
                
            # right
            for i in range(startRow+1,endRow+1):
                res.append(matrix[i][endCol])
                
            # bottom    
            for j in range(endCol-1,startCol-1,-1):
                if startRow == endRow:
                    break
                res.append(matrix[endRow][j])
    
            # left    
            for i in range(endRow-1,startRow,-1):
                if startCol == endCol:
                    break
                res.append(matrix[i][startCol])
             
            startRow += 1
            startCol += 1
            endRow -= 1
            endCol -= 1   
    
        return res         

    def matrixDiagnoalSum(matrix):
        sum = 0
        # Brute Force 
        # for i in range(len(matrix)):
        #     for j in range(len(matrix[0])):
        #         if i == j :                  #For primary diagnoal i == j 
        #             sum += matrix[i][j]
        #         if (i+j) == (len(matrix)-1):  #For secondary diagnoal i+j = n-1
        #             sum += matrix[i][j]    
        
        # Optimal Code 
        for i in range(len(matrix)):
            # primary Diagonal
            sum += matrix[i][i]
            
            # secondary Diagnoal 
            sum += matrix[i][len(matrix)-1-i]
        return sum            
 
    def searchInSortedMatrix(matrix,key):
        
        if not matrix :
            return [-1,-1]
        
        i = 0
        j = len(matrix[0])-1
        
        while i < len(matrix) and j>= 0:
            
            if matrix[i][j] == key:
                return [i,j]
            elif key < matrix[i][j]:
                j -= 1  # Left
            else:
                i += 1  # Bottom

        return [-1 , -1]  
        

matrix = [[1,2,3],[4,5,6],[7,8,9]]    

# print(Solution.matrixDiagnoalSum(matrix))    
# print(Solution.spiralMatrix(matrix)) 

arr = [[10,20,30,40],[15,25,35,45],[27,29,37,48],[32,33,39,50]] 
key = 33
print(Solution.searchInSortedMatrix(arr,key))  