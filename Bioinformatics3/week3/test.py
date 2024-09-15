# -*- coding: utf-8 -*-
import math

GAP = -3
MATCH = 8
GAPOPEN = -4
MISMATCH = -5

def align_with_affine_gap_penalty(seqA, seqB):
    # create and clean matrices
    matD = [[-math.inf for _ in range(len(seqB)+1)] for _ in range(len(seqA)+1)] #lower
    matI = [[-math.inf for _ in range(len(seqB)+1)] for _ in range(len(seqA)+1)] #upper
    matS = [[-math.inf for _ in range(len(seqB)+1)] for _ in range(len(seqA)+1)] #mid

    # initialization
    matS[0][0] = 0
    matD[0][0] = matI[0][0] = GAPOPEN
    for i in range(1, len(seqA)+1):
        matD[i][0] = matD[i-1][0] + GAP
        matS[i][0] = matD[i][0]
    for j in range(1, len(seqB)+1):
        matI[0][j] = matI[0][j-1] + GAP
        matS[0][j] = matI[0][j]

    # DP
    for i in range(1, len(seqA)+1):
        for j in range(1, len(seqB)+1):
            matD[i][j] = max(matD[i-1][j] + GAP, matS[i-1][j] + GAPOPEN + GAP)
            matI[i][j] = max(matI[i][j-1] + GAP, matS[i][j-1] + GAPOPEN + GAP)
            matS[i][j] = max(matS[i-1][j-1] + (MATCH if seqA[i-1] == seqB[j-1] else MISMATCH), max(matD[i][j], matI[i][j]))

    # print matrics
    seqB = "-" + seqB
    seqA = "-" + seqA
    for (mat_name, mat) in zip(['D', 'I', 'S'], [matD, matI, matS]):
        print(" {} =".format(mat_name))
        print("  A\B", end="")
        print(''.join(['{:>5}'.format(b) for b in seqB]))

        for i, row in enumerate(mat):
            row = ['{:5d}'.format(x) if x > -math.inf else "   -∞" for x in row]
            row = ['{:>5}'.format(seqA[i])] + row
            print(''.join(row))

if __name__ == '__main__':
    align_with_affine_gap_penalty("CAATTGA", "GAATCTGC")