import sys
import chess

if len(sys.argv) != 9:
    print("Usage: python main.py row1 col1 row2 col2 ... row8 col8")
    sys.exit(1)

positions = [(int(sys.argv[i]), int(sys.argv[i+1])) for i in range(1, len(sys.argv), 2)]

if chess.are_queens_safe(positions):
    print("True")
else:
    print("False")