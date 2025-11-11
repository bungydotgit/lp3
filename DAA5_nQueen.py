def isSafe(mat, row, col, n):
    # Check column
    for i in range(row):
        if mat[i][col]:
            return False

    # Check upper-left diagonal
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if mat[i][j]:
            return False
        i -= 1
        j -= 1

    # Check upper-right diagonal
    i, j = row - 1, col + 1
    while i >= 0 and j < n:
        if mat[i][j]:
            return False
        i -= 1
        j += 1

    return True


def placeQueens(row, placed, k, mat, result, n):
    # Base case: if required number of queens are placed
    if placed == k:
        ans = []
        for i in range(n):
            for j in range(n):
                if mat[i][j]:
                    ans.append((i + 1, j + 1))  # store (row, col)
        result.append(ans)
        return

    # If we've filled all rows but haven't placed all queens
    if row == n:
        return

    for col in range(n):
        if isSafe(mat, row, col, n):
            mat[row][col] = 1
            placeQueens(row + 1, placed + 1, k, mat, result, n)
            mat[row][col] = 0

    # Optionally skip placing a queen in this row
    placeQueens(row + 1, placed, k, mat, result, n)


def nQueensCustom(n, k):
    mat = [[0] * n for _ in range(n)]
    result = []
    placeQueens(0, 0, k, mat, result, n)
    return result


if __name__ == "__main__":
    n = int(input("Enter size of matrix (n x n): "))
    k = int(input("Enter number of queens: "))

    result = nQueensCustom(n, k)

    if not result:
        print("\nNo possible arrangement.")
    else:
        print(f"\nPossible arrangements ({len(result)} found):")
        for idx, ans in enumerate(result, 1):
            print(f"\nArrangement {idx}:")
            board = [['.'] * n for _ in range(n)]
            for r, c in ans:
                board[r - 1][c - 1] = 'Q'
            for row in board:
                print(" ".join(row))
