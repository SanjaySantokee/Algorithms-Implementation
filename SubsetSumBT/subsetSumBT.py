"""

    /*
        Full Name: Sanjay Santokee
        Email: sanjay.santokee@my.uwi.edu
    */  


    The subset-sum problem is to find a subset(s) of a given set S = {a1, ..., an}
    of n positive integers whose sum is equal to a given positive integer d.
    An assumption is that the elements a1 … an are in increasing order.
"""


def BacktrackIter(X: list, d: int):
    """
        Finds a subset of a given set A = {a1, ..., an} (or S = {s1, ..., sn})
        of n positive integers whose sum is equal to a given positive integer d

        :param X: List of Integers
        :param d: Integer Sum to Search For
        :return: List of Solutions
    """

    k = 0
    v = []  # Empty list
    flag = False
    sets_of_X = []
    final_solutions = []
    resetter = []

    # Making space for enough elements to fit in computing subsets
    for x in range(len(X)):
        v.append(0)

    # Making a set of all subsets
    for x in range(len(X)):
        sets_of_X.append(X.copy())
        resetter.append(X.copy())
        X.pop(0)

    while k >= 0:
        while sets_of_X[k]:  # while the Xk is not exhausted
            v[k] = sets_of_X[k].pop(0)  # get the next element in Xk and append to v

            if sum(v) == d:  # If v is a final solution
                final_solutions.append(v.copy())    # hard copy v is appended to final_solutions
                flag = True
                v[k] = 0

            if sets_of_X[k]:  # if Xk is not exhausted
                inequality_1 = (sum(v) + int(sets_of_X[k][0]))  # popped off k, so k[0] is a(i+1)
                inequality_2 = (sum(v) + sum(sets_of_X[k]))

                if inequality_1 <= d and inequality_2 >= d:  # If v is partial solution
                    k += 1  # {Advance}

        v[k] = 0
        # Reset Xk so that the next element is the first
        resetter[k].pop(0)
        sets_of_X[k] = resetter[k].copy()
        k -= 1  # {Backtrack}

    if flag:
        # Printing Answers
        # Since subset sum only deals with numbers that are positive,
        # it is safe to remove all 0's from the sets and output answers

        final_solutions_output = []
        for index, sol in enumerate(final_solutions):
            sol = [x for x in sol if x != 0]
            final_solutions_output.append(sol)

        print('Answer found: ', final_solutions_output)
    else:
        print("No Solution")


if __name__ == '__main__':
    # Reading in the data from the input file
    with open('subsetSum.txt') as file:
        X = list(map(int, file.readline().strip('\n').split()))
        d = int(file.readline().strip('\n'))

    print('Subset-Sum for: ')
    print("X: ", X)
    print("d: ", d)

    # Calling the BacktrackIter function
    BacktrackIter(X, d)
