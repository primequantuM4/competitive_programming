def findMaxAttackPoint(board):
    maxPoint = 0
    for row in range(len(board)):
        for col in range(len(board[0])):
            if (row, col) not in diagonal:
                calculateSum(row, col, board, True)

            if (row, col) not in anti_diagonal:
                calculateSum(row, col, board, False)

            drow, dcol = diagonal[(row, col)]
            arow, acol = anti_diagonal[(row, col)]
            maxPoint = max(maxPoint, diagonal_sum[(drow, dcol)] + anti_diagonal_sum[(arow, acol)] - board[row][col])

    return maxPoint


def calculateSum(row, col,board, isDiagonal):
    og_row, og_col = row, col
    points = 0 

    if isDiagonal:
        while row < len(board) and col < len(board[0]):
            points += board[row][col]
            diagonal[(row, col)] = (og_row, og_col)
            row += 1
            col += 1
        diagonal_sum[(og_row, og_col)] = points

    else:
        while row <len(board) and col >= 0:
            points += board[row][col]
            anti_diagonal[(row, col)] = (og_row, og_col)
            row += 1
            col -= 1

        anti_diagonal_sum[(og_row, og_col)] = points


test_cases = int(input())
for _ in range(test_cases):
    row, col = list(map(int, input().split()))
    board = []
    for points in range(row):
        board.append(list(map(int, input().split())))

    diagonal = {}
    anti_diagonal = {}
    diagonal_sum = {}
    anti_diagonal_sum = {}

    print(findMaxAttackPoint(board))
