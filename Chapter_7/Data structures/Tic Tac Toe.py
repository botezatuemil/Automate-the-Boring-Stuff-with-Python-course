theBoard = {'top-L':' ', 'top-M':' ', 'top-R':' ',
            'mid-L':' ', 'mid-M':' ', 'mid-R':' ',
            'low-L':' ', 'low-M':' ', 'low-R':' '
            }

theBoard['top-L'] = 'O'
theBoard['mid-M'] = 'X'
theBoard['low-M'] = 'X'

def printBoard(board):
    print(theBoard['top-L'] + '|' + theBoard['top-M'] + '|' + theBoard['top-R'])
    print('-----')
    print(theBoard['mid-L'] + '|' + theBoard['mid-M'] + '|' + theBoard['mid-R'])
    print('-----')
    print(theBoard['low-L'] + '|' + theBoard['low-M'] + '|' + theBoard['low-R'])

printBoard(theBoard)

print(type(42))