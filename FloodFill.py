class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        inBound = lambda r,c : 0 <= r < len(image) and 0 <= c < len(image[0])
        neededColor = image[sr][sc]

        stack = []
        image[sr][sc] = color
        stack.append((sr, sc))
        visited = set()

        directions = [(1,0), (0,1), (-1,0), (0, -1)]
        while stack:
            row, col = stack.pop()

            for r, c in directions:
                new_row = r + row
                new_col = c + col
                not_visited = (new_row, new_col) not in visited

                if not_visited and inBound(new_row, new_col) and image[new_row][new_col] == neededColor:
                    image[new_row][new_col] = color
                    stack.append((new_row, new_col))

                visited.add((row, col))

        return image
                
        
