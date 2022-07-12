import sys
import re
import copy

sys.path.append(f'{sys.path[0]}/..')

# 常數
BOARDSIZE, EMPTY, BLACK, WHITE = 15, 0, 1, 2

# region 輔助函數

# countChain:
#
# param:
#   board: list[list[int]]
#   stone: int
#
# return: tuple(list[list[int]])
#   回傳在每個點上該顏色的連續數量，因為連續有四個方向，所以共回傳四個二維陣列


def countChain(board, stone):
    # def countChain( board : list[list[int]], stone : int = BLACK ) -> tuple[ list[list[int]], list[list[int]], list[list[int]], list[list[int]] ] :

    isYours = [[int(grid == stone) for grid in row] for row in board]
    rowChain = isYours
    colChain = copy.deepcopy(isYours)
    ldiaChain = copy.deepcopy(isYours)
    rdiaChain = copy.deepcopy(isYours)

    for i in range(BOARDSIZE):
        for j in range(BOARDSIZE):
            if (j != 0 and rowChain[i][j]):
                rowChain[i][j] = rowChain[i][j-1] + 1
            if (i != 0 and colChain[i][j]):
                colChain[i][j] = colChain[i-1][j] + 1
            if (i != 0 and j != 0 and ldiaChain[i][j]):
                ldiaChain[i][j] = ldiaChain[i-1][j-1] + 1
            if (i != 0 and j != BOARDSIZE-1 and rdiaChain[i][j]):
                rdiaChain[i][j] = rdiaChain[i-1][j+1] + 1

    for i in range(BOARDSIZE-1, -1, -1):
        for j in range(BOARDSIZE-1, -1, -1):
            if (j != BOARDSIZE-1 and rowChain[i][j] and rowChain[i][j+1]):
                rowChain[i][j] = rowChain[i][j+1]
            if (i != BOARDSIZE-1 and rowChain[i][j] and rowChain[i+1][j]):
                colChain[i][j] = colChain[i+1][j]
            if (i != BOARDSIZE-1 and j != BOARDSIZE-1 and ldiaChain[i][j] and ldiaChain[i+1][j+1]):
                ldiaChain[i][j] = ldiaChain[i+1][j+1]
            if (i != BOARDSIZE-1 and j != 0 and rdiaChain[i][j] and rdiaChain[i+1][j-1]):
                rdiaChain[i][j] = rdiaChain[i+1][j-1]
    return rowChain, colChain, ldiaChain, rdiaChain

# peek:
#
# param:
#   board: list[list[int]]
#       board.size == board[0].size == BOARDSIZE
#   (i, j):  (int, int)
#       0 <= i < BOARDSIZE
#       0 <= j < BOARDSIZE
#   stone: int
#       stone in [EMPTY, BLACK, WHITE]
#
# return: list[[int, bool]]
#   peek(board,i,j,stone).size == 8
#   從 board[i][j] 往八個方向看，看此方向有連續幾顆 stone 顏色的棋，以及在這些棋子之後是否有空位
#
# example:
#   board =
#     [[0, 0, 0, 0, 2],
#      [0, 0, 1, 1, 2],
#      [0, 1, 1, 1, 1],
#      [0, 1, 1, 1, 2],
#      [0, 1, 1, 1, 2]]
#   peek(board, 2, 2, 1) == [[1, True], [1, False], [2, False], [1, False], [2, False], [1, True], [1, True], [0, True]]


def peek(board, i, j, stone):
    # def peek( board:list[list[int]], i:int, j:int, stone:int ) -> list[list[int, bool]]

    if i < 0 or i >= BOARDSIZE or j < 0 or j >= BOARDSIZE:
        print("Invalid index to peek")
        return None

    ret = [[0, False] for _ in range(8)]

    for k in range(8):

        y = i
        x = j

        if k == 2 or k == 6:  # horizontal
            delY = 0
        else:
            delY = 1 if k > 2 and k < 6 else -1

        if k == 0 or k == 4:  # vertical
            delX = 0
        else:
            delX = 1 if k > 0 and k < 4 else -1

        while True:
            y += delY
            x += delX
            if y < 0 or y >= BOARDSIZE:
                break
            if x < 0 or x >= BOARDSIZE:
                break
            if board[y][x] != stone:
                break
            ret[k][0] += 1

        if y < 0 or y >= BOARDSIZE:
            continue
        if x < 0 or x >= BOARDSIZE:
            continue
        ret[k][1] = board[y][x] == EMPTY

    return ret

# endregion


"""
user:
    輸入目前的棋盤跟你是黑棋或白棋(1 or 2)，以及剩餘的時間
    回傳你要下的 index: (row, col)
    param:
        board: list[list[int]]
            board.size == board[0].size == BOARDSIZE
        myStone: int
            myStone in [EMPTY, BLACK, WHITE] (0, 1, 2)
        remain_time: float
            remaining time(unit: second)
    return: row, column
定義請看 variables.py
輔助函式請看 simplelib.py
整個 user 都可以改，除此之外都不要改
NOTE: 若要debug，請使用 print("message", file=sys.stderr)，不要 print 到stdout
"""


def user(board, myStone, remain_time):
    score = [[0 for j in range(BOARDSIZE)]
             for i in range(BOARDSIZE)]  # score 儲存每個格子的分數
    for i in range(BOARDSIZE):
        for j in range(BOARDSIZE):  # 遍例每個格子
            if board[i][j] is EMPTY:  # 對空的格子算分
                board[i][j] = myStone  # 試著下在這格
                """
                left blank to you
                """
                board[i][j] = EMPTY  # 試完了，拿起來

    # 取最大分數的格子回傳
    maxi = 0
    maxj = 0
    max_score = -1
    for i in range(BOARDSIZE):
        for j in range(BOARDSIZE):
            if score[i][j] > max_score:
                max_score = score[i][j]
                maxi = i
                maxj = j
    # print(maxi, maxj, max_score, file=sys.stderr)
    return maxi, maxj


# DO NOT modify code below!(請絕對不要更改以下程式碼)
# 也可以不用看
def main():
    r = re.compile(r"[^, 0-9-]")
    raw_data = input()
    raw_data = r.sub("", raw_data)
    # print(raw_data)
    user_list = [int(coord) for coord in raw_data.split(', ')]
    # print(user_list)
    input_board = [[]] * 15
    for row in range(15):
        input_board[row] = [0] * 15
    for i in range(15):
        for j in range(15):
            input_board[i][j] = user_list[i*15+j]

    input_mystone = user_list[225]
    remain_t = user_list[226]
    i, j = user(input_board, input_mystone, remain_t)
    print(i, j)


if __name__ == '__main__':
    main()
