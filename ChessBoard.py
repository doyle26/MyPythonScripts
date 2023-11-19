chessboard = [
     ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'],
     ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
     [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
     [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
     [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
     [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
     ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
     ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r']
 ]
 
def display_chessboard(chessboard):
     for row in chessboard:
         print(' '.join(row))
     print("\n")

display_chessboard(chessboard)
