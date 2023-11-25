board = [[" "]*3 for _ in range(3)]
player = "X"

while True:
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

    print(f"Player {player}'s turn")

    move = input("Enter row and column (e.g., 0 1): ").split()
    if len(move) != 2:
        print("Invalid input. Please enter two values.")
        continue

    try:
        row, col = int(move[0]), int(move[1])
    except ValueError:
        print("Invalid input. Please enter valid integers.")
        continue

    if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == " ":
        board[row][col] = player

        if any(all(board[i][j] == player for j in range(3)) for i in range(3)) or \
           any(all(board[j][i] == player for j in range(3)) for i in range(3)) or \
           all(board[i][i] == player for i in range(3)) or \
           all(board[i][2 - i] == player for i in range(3)):
            print(f"Player {player} wins!")
            break

        if all(cell != " " for row in board for cell in row):
            print("It's a draw!")
            break

        player = "O" if player == "X" else "X"
    else:
        print("Invalid move. Try again.")
