def knapsackRec(W, val, wt, n):
    # Base Case
    if n == 0 or W == 0:
        return 0

    pick = 0
    # Pick nth item if it does not exceed the capacity
    if wt[n - 1] <= W:
        pick = val[n - 1] + knapsackRec(W - wt[n - 1], val, wt, n - 1)

    # Don't pick the nth item
    notPick = knapsackRec(W, val, wt, n - 1)

    # Return the best of the two choices
    return max(pick, notPick)


def knapsack(W, val, wt):
    n = len(val)
    return knapsackRec(W, val, wt, n)


# ---------- MAIN PROGRAM ----------
if __name__ == "__main__":
    print("Press Ctrl+C to stop the program.\n")

    while True:
        try:
            n = int(input("Enter number of items: "))
            val = list(map(int, input("Enter values of items (space-separated): ").split()))
            wt = list(map(int, input("Enter weights of items (space-separated): ").split()))
            W = int(input("Enter maximum weight capacity: "))

            if len(val) != n or len(wt) != n:
                print("Number of values/weights must match number of items!\n")
                continue

            max_value = knapsack(W, val, wt)
            print(f"Maximum value that can be carried: {max_value}\n")

        except KeyboardInterrupt:
            print("\nProgram terminated by user.")
            break
        except Exception as e:
            print(f"Error: {e}\n")
