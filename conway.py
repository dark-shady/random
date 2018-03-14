import numpy as np
import os
import time
import sys

clear = lambda: os.system('cls')
clear()
def test():
    test_board = np.array([[1,0,1,0], [0,1,0,1], [1,1,1,1], [0,0,0,0]])
    assert(print_board(test_board) == ("1 0 1 0\n"
                                      "0 1 0 1\n"
                                      "1 1 1 1\n"
                                      "0 0 0 0"))

    assert(find_neighbors(0, 0, test_board) == [(1, 0), (0, 1), (1, 1)])
    assert(find_neighbors(1, 0, test_board) == [(0, 0), (2, 0), (0, 1), (1, 1), (2, 1)])
    assert(find_neighbors(1, 1, test_board) == [(0, 0), (1, 0), (2, 0), (0, 1), (2, 1), (0, 2), (1, 2), (2, 2) ])

    assert(deadoralive(1,1) == 0)
    assert(deadoralive(1,2) == 1)
    assert(deadoralive(1,4) == 0)
    assert(deadoralive(0,3) == 1)
    assert(deadoralive(0,2) == 0)


def print_board(array):
    '''
    in:
    array - numpy array of board

    output: prints the board, each cell joined by ' ' and each row joined by '\n'

    '''
    return '\n'.join(' '.join('o' if cell else '.' for cell in row) for row in array)


def find_neighbors(x, y, board):
    '''
    in:
    array - numpy array of board
    cell - tuple of cell position on board (x, y)

    out:
    neighbors - list of tuples of cells surrounding input cell
    '''

    '''
    //  column, row
    cell = (0,0)
    expected =  xxx   (1,0)
               (0,1)  (1,1)



    cell = (1, 1)
    expected = (0,0) (1,0)  (2,0)
               (0,1) xxxxx  (2,1)
               (0,2) (1,2)  (2,2)

    '''
    array_size = board.shape
    return [(xx,yy) for yy in range(y-1,y+2) for xx in range(x-1,x+2) if (xx,yy) != (x,y) and -1 not in (xx,yy) and xx < array_size[0] and yy < array_size[1]]


def sum_neighbors(neighbors, board):
    return sum(board[x][y] for x,y in neighbors)


def deadoralive(current_state, sum_of_neighbors):
    if current_state == 1:
        if sum_of_neighbors < 2 or sum_of_neighbors > 3:
            return 0
        else:
            return 1
    elif current_state == 0:
        if sum_of_neighbors == 3:
            return 1
        else:
            return 0



if len(sys.argv) > 2:
    x, y = int(sys.argv[1]), int(sys.argv[2])
else:
    x, y = 25, 25

current_board = np.random.randint(2, size=(x, y))
old_board = np.empty([x, y])
print(print_board(current_board))

while True:
    time.sleep(1)
    clear()
    old_board = np.copy(current_board)
    for index, value in np.ndenumerate(old_board):
        neighbors = find_neighbors(index[0], index[1], old_board)
        sum_of_neighbors = sum_neighbors(neighbors, old_board)
        current_board[index[0], index[1]] = deadoralive(value, sum_of_neighbors)

    print(print_board(current_board))

test()
