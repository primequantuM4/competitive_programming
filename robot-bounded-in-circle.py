class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        direction = {"L": -1, "R": 1}
                        #North  #East   #South    #West
        cardinal_dir = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        index = 0
        visited = {(0, 0)}
        row, col = 0, 0
        for instruction in instructions:
            if instruction == "G":
                row += cardinal_dir[index][0]
                col += cardinal_dir[index][1]
            
            else:
                index = (4 + index + direction[instruction]) % 4
        
        return (row == 0 and col == 0) or index != 0
                