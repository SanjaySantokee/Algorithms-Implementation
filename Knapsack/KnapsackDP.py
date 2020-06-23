"""
    /*
        Full Name: Sanjay Santokee
        Email: sanjay.santokee@my.uwi.edu
    */  
    Given n items of known weights w1,...,wn and values v1,...,vn and a knapsack of capacity W, it finds the most
    valuable subset of the items that fit into the knapsack.
"""


# (a)
def Knapsack_DP(w: list, v: list, W: int):
    n_items, capacity = len(v) + 1, W + 1

    # Creating and initializing the F table (array)
    F = []
    for i in range(n_items):
        F.append(
            [float(0.00) for j in range(capacity)])  # Float value because value can be in terms of dollars and cents

    for i in range(1, n_items):
        k = i - 1
        for j in range(1, capacity):
            if w[k] > j:
                F[i][j] = F[i - 1][j]
            else:
                F[i][j] = max(v[k] + F[i - 1][j - w[k]], F[i - 1][j])
    return F


# (b)
def backtrack(F: list, weights_arr: list, n_items: int, capacity: int, solutions_list: list):
    k = n_items - 1
    if n_items == 0 or capacity == 0:
        return
    if F[n_items][capacity] == F[k][capacity]:
        backtrack(F, weights_arr, k, capacity, solutions_list)
    else:
        backtrack(F, weights_arr, k, capacity - weights_arr[k], solutions_list)
        solutions_list.append(n_items)


if __name__ == "__main__":
    solutions = []
    values = []
    weights = []

    knapsack_data = open('knapsack.txt', 'r')

    # Read W (capacity)
    W = int(knapsack_data.readline())

    # Read weights and values
    for row in knapsack_data:
        weights.append(int(row.split()[0]))
        values.append(float(row.split()[1]))

    # Get number of items, n.
    n = len(weights)

    F_table = Knapsack_DP(weights, values, W)
    backtrack(F_table, weights, n, W, solutions)

    print("The selected items are: ", solutions)
