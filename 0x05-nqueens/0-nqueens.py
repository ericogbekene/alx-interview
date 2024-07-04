#!/usr/bin/python3
"""
Solving the Nqueens problem
"""

import sys

def solve_n_queens(n:int) -> bool:
    args: list = sys.argv

    if len(args) < 2:
        print("Usage: nqueens N")
    if not isinstance(int(args[1]), int):
        print("N must be a number")
    if int(args[1]) < 4:
        print("N must be at least 4")

    n = int(args[1])

    def is_safe(board:list, row: int, col: int):
        # Check if a queen can be placed on board[row][col]
        
        # Check this row on left side
        for i in range(col):
            if board[row][i] == 1:
                return False
        
        # Check upper diagonal on left side
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j] == 1:
                return False
        
        # Check lower diagonal on left side
        for i, j in zip(range(row, n, 1), range(col, -1, -1)):
            if board[i][j] == 1:
                return False
        
        return True

    def solve(board: list, col):
        # Base case: If all queens are placed, return true
        if col >= n:
            return True
        
        # Consider this column and try placing this queen in all rows one by one
        for i in range(n):
            if is_safe(board, i, col):
                # Place this queen in board[i][col]
                board[i][col] = 1
                
                # Recur to place rest of the queens
                if solve(board, col + 1):
                    return True
                
                # If placing queen in board[i][col] doesn't lead to a solution,
                # then remove queen from board[i][col]
                board[i][col] = 0
        
        # If the queen can't be placed in any row in this column col, return false
        return False

    # Initialize the board
    board = [[0 for _ in range(n)] for _ in range(n)]
    
    # Start from the first column
    if solve(board, 0) == False:
        print("Solution does not exist")
        return False
    
    # Print the solution
    for i in range(n):
        for j in range(n):
            print(board[i][j], end=" ")
        print()
    
    return True

if __name__ == '__main__':
    n: int = int(sys.argv[1])
    #solve(n)
    solve_n_queens(n)