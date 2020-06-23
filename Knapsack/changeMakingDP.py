"""
    /*
        Full Name: Sanjay Santokee
        Email: sanjay.santokee@my.uwi.edu
         Solving the Change Making problem by a dynamic programming (DP) technique
    */  
"""


def changeMakingDP(D: list, V: int):
    """
    This function applies dynamic programming to find the minimum
    number of coins of denominations that add up to a given amount.

    :param D: All Coin Denominations
    :param V: Amount to give change for
    :return: Populated F-Table (Change Table)
    """

    # Initializing the F-table with all 0's
    F = [0] * (V + 1)

    # Calculating the number of unique denominations
    n = len(D)

    for i in range(1, V + 1):
        # Smallest value initialized to infinity
        smallest = float("inf")

        for j in range(0, n):
            if D[j] <= i:
                smallest = min(smallest, F[i - D[j]])
        F[i] = 1 + smallest
    return F


# def Backtrack(F):
def Backtrack(F: list, D: list, V: int):
    """
     This function finds and prints the coins of an optimal solution by backtracking on the computations
     to see which of the denominations produced the minimum-coin set (Optimal Solution).

    :param F: F table - this is the Change Table
    :param D: All Coin Denominations
    :param V: Amount to give change for
    :return: None
    """

    # List for holding the coins of the optimal solution
    optimal_solution = []

    while V > 0:
        # Coin value initialized to infinity
        coin = float('inf')
        optimal_coin, i = 0, 0

        while i <= len(D) - 1 and D[i] <= V:
            coin = min(coin, F[V - D[i]])

            if coin == F[V - D[i]]:
                optimal_coin = D[i]

            i += 1

        # Add optimal coin to the list of solutions
        optimal_solution.append(optimal_coin)
        # Reduce to only the amount of change left
        V -= optimal_coin

    print('The minimum-coin set (Optimal Solution) is:', optimal_solution)


if __name__ == "__main__":

    # Coin Change Problems
    problems = [
        [[1, 3, 4], 20],
        [[1, 5, 6], 15]
    ]

    for D, V in problems:
        F = changeMakingDP(D, V)
        print('\n______________________________________________________________')
        print('Problem: ')
        print('Denominations =', D)
        print('Amount (value) to make change for =', V)
        print('The amount of coins needed for change are:', F[V])
        Backtrack(F, D, V)
