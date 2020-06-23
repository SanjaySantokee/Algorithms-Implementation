"""
    /*
        Full Name: Sanjay Santokee
        Email: sanjay.santokee@my.uwi.edu
    */  

    Given a number of beads on a wire, bw, sequenced 1, 2, 3, .., etc. and boxes to place the beads, bx, sequenced 1,
    2, 3, 4, ..., etc., where bx ≥ bw, such that placing the beads in certain boxes increases the aesthetic value.
    The beads must be placed sequentially in the boxes up until the last box. """


def bead_DP(A: list):
    for i in range(1, beads + 1):
        for j in range(1, boxes + 1):
            if i == 0 or j == 0:
                A[i][j] = 0
            if i == j and i > 0 and j > 0:
                A[i][j] = A[i - 1][j - 1] + A[i][j]
            if j > i > 0 and j > 0:
                A[i][j] = max(A[i][j - 1], A[i - 1][j - 1] + A[i][j])
    return A


def backtrack_beads(i: int, j: int, B: list):
    if i == 0 or j == 0:
        return
    if i == j:
        backtrack_beads(i - 1, j - 1, B)
        print('The Bead ', i, ' is put into the Box ', j)
    elif B[i][j] > B[i][j - 1] and B[i][j] > B[i][j - 1]:
        backtrack_beads(i - 1, j - 1, B)
        print('The Bead ', i, ' is put into the Box ', j)
    elif B[i][j] == B[i][j - 1]:
        backtrack_beads(i, j - 1, B)


if __name__ == "__main__":

    with open('beads.txt') as file:
        beads, boxes = list(map(int, file.readline().strip('\n').split()))

        aesthetics = []
        for row in range(beads + 1):
            aesthetics.append([0 for col in range(boxes + 1)])

        row = 1
        for line in file:
            data = line.split()
            for col in range(1, boxes + 1):
                aesthetics[row][col] = int(data[col - 1])
            row += 1

    # Computing beads table
    B_table = bead_DP(aesthetics)

    # Backtracking to output beads and its placement
    backtrack_beads(beads, boxes, B_table)
