def is_neighbour(board, row, col, letter):
    lst = []
    if row != 0:
        if board[row - 1][col] == letter:
            lst.append([row - 1, col])
    if row != len(board) - 1:
        if board[row + 1][col] == letter:
            lst.append([row + 1, col])
    if col != 0:
        if board[row][col - 1] == letter:
            lst.append([row, col - 1])
    if col != len(board[0]) - 1:
        if board[row][col + 1] == letter:
            lst.append([row, col + 1])
    return lst

def exist(board, word):
    for i in range(len(board)):
        if word[0] in board[i]:
            is_neighbour(board, i, board[i].index(word[0]), word[1])




board = [["C", "B", "C", "E"],
         ["S", "C", "C", "S"],
         ["A", "B", "E", "E"]]

print(is_neighbour(board, 0, 1, "C"))

#print(exist())

