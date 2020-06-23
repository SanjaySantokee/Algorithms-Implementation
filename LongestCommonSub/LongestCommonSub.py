"""
    /*
        Full Name: Sanjay Santokee
        Email: sanjay.santokee@my.uwi.edu
    */  

    Given two sequences, find the length k of longest subsequence present in both of them.
    A subsequence is a sequence that appears in the same relative order,
    but not necessarily contiguous from both A and B.
    For example, “abc”, “abg”, “bdf”, “aeg”, ‘”acefg”, and more are subsequences of “abcdefg”

"""


def LCS(A: str, B: str):
    m, n = len(A) + 1, len(B) + 1

    L = []

    # Initialize all values to 0
    for i in range(m):
        L.append(
            [0 for j in range(n)])

    for i in range(1, m):
        for j in range(1, n):
            if A[i - 1] == B[j - 1]:
                L[i][j] = L[i - 1][j - 1] + 1
            else:
                L[i][j] = max(L[i][j - 1], L[i - 1][j])
    return L


def printLCS(A: str, B: str, L: list):
    # Begin at the bottom-right corner of the LCS table and
    # work your way up to the top (value by value)
    i, j = len(A), len(B)

    # Create a list to hold the final LCS string
    C = []
    while i > 0 and j > 0:
        if A[i - 1] == B[j - 1]:
            # It is inserted at 0 since it traverses in a reverse way and needs
            # to store it in the reversed fashion by pushing everything into
            # the list C backwards.
            C.insert(0, A[i - 1])  # Put the character in the list
            # reduce values of i and j
            i -= 1
            j -= 1

        else:
            # If it is not the same, find the number larger in size (of the two)
            # And proceed to go in the path of that number which is larger
            if L[i - 1][j] > L[i][j - 1]:
                i -= 1  # remove last character of A
            else:
                j -= 1  # remove last character of  B

    print('The length of LCS is ', len(C))
    print('The LCS C is "', ''.join(C), '"')


if __name__ == "__main__":
    with open('lcs.txt') as file:
        strings = file.readline().strip('\n').split(' ')
    table = LCS(strings[0], strings[1])

    print('LCS of: ', strings[0], ', ', strings[1])
    printLCS(strings[0], strings[1], table)
