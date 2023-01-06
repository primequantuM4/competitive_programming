class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        filled_nodes = self.sameColors(image,sr,sc)
        for r, c in filled_nodes:
            image[r][c] = color
        return image
    def sameColors(self,image, sr, sc):
        color = image[sr][sc]
        inBound = lambda r,c: 0 <= r < len(image) and 0 <= c < len(image[0])
        stack = [(sr, sc)]
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        sameColor = set()
        while stack:
            rows, cols = stack.pop()
            sameColor.add((rows, cols))
            for r,c in directions:
                next_row = r + rows
                next_col = c + cols
                visited = (next_row, next_col) in sameColor
                if inBound(next_row, next_col) and (not visited) and image[next_row][next_col] == color:
                    stack.append((next_row, next_col))
        return sameColor
