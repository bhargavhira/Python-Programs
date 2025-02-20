import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
    print()

def check_winner(board, player):
    return any(all(cell == player for cell in row) for row in board) or \
           any(all(board[r][c] == player for r in range(3)) for c in range(3)) or \
           all(board[i][i] == player for i in range(3)) or \
           all(board[i][2 - i] == player for i in range(3))

def get_empty_cells(board):
    return [(r, c) for r in range(3) for c in range(3) if board[r][c] == " "]

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("Tic-Tac-Toe! You are 'X', Computer is 'O'.")
    
    for turn in range(9):
        print_board(board)
        if turn % 2 == 0:
            while True:
                try:
                    row, col = map(int, input("Enter row and column (0-2): ").split())
                    if (row, col) in get_empty_cells(board):
                        board[row][col] = "X"
                        break
                except ValueError:
                    pass
                print("Invalid move. Try again.")
        else:
            row, col = random.choice(get_empty_cells(board))
            print(f"Computer chose: {row}, {col}")
            board[row][col] = "O"
        
        if check_winner(board, "X") or check_winner(board, "O"):
            print_board(board)
            print("You win!" if check_winner(board, "X") else "Computer wins!")
            return
    
    print_board(board)
    print("It's a draw!")

if __name__ == "__main__":
    main()
