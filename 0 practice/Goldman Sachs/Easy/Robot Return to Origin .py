class Solution:
    def judgeCircle( moves: str) -> bool:
        return moves.count("U") == moves.count("D") and moves.count("L") == moves.count('R')
        
print(Solution.judgeCircle("UDD"))        