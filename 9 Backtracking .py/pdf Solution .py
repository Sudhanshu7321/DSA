def rat(maze,row,col,visited):
    # Base Case 
    if row == len(maze)-1 and col == len(maze[0])-1:
        return 1
    elif row < 0 or row >= len(maze) or col < 0 or col >= len(maze[0]) or maze[row][col] == 0 or visited[row][col] :
        return 0
    
        # Mark the cell as visited
    visited[row][col] = True
    
    r1 = rat(maze,row,col+1,visited)
    r2 = rat(maze,row+1,col,visited)
    r3 = rat(maze,row,col-1,visited)
    r4 = rat(maze,row-1,col,visited)
    
        # Unmark the cell as visited for other paths
    visited[row][col] = False
    
    return r1+r2+r3+r4

maze = [
    [1, 0, 0, 0],
    [1, 1, 0, 1],
    [0, 1, 1, 0],
    [1, 1, 1, 1]
]
# Initialize the visited matrix
visited = [[False for _ in range(len(maze[0]))] for _ in range(len(maze))]
# print(rat(maze,0,0,visited))


def q2(s):
    dic = {
        '1': '',
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz',
    }
    
    res = []
    
    if not s:
        return res
    
    def backtrack(index, path):
        if index == len(s):
            res.append(path)
            return
        
        possible_letters = dic[s[index]]
        for letter in possible_letters:
            backtrack(index + 1, path + letter)
    
    backtrack(0, "")
    return res

print(q2('23'))

        