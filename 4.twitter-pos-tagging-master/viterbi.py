import numpy as np


def run_viterbi(emission_scores, trans_scores, start_scores, end_scores):
    """Run the Viterbi algorithm for decoding

    N - number of tokens (length of sentence)
    L - number of labels

    Given:
    - Emission scores, as an NxL array
    - Transition scores (Yp -> Yc), as an LxL array
    - Start transition scores (S -> Y), as an Lx1 array
    - End transition scores (Y -> E), as an Lx1 array

    Returns:
    - s is the score of the best sequence
    - y is the size N array/seq of integers representing the best sequence.
    """
    L = start_scores.shape[0]
    assert end_scores.shape[0] == L
    assert trans_scores.shape[0] == L
    assert trans_scores.shape[1] == L
    assert emission_scores.shape[1] == L
    N = emission_scores.shape[0]

    T = np.zeros((N, L)).astype(float)
    T[:,:]= float('-inf')
    back = np.zeros((N, L)).astype(int)

    y = [0 for i in range(N)]

    # Initialize with initial transitions. 
    for i in range(L):
        T[0, i] = start_scores[i] + emission_scores[0][i]

    # Recursion step
    for i in range(1, N):
        for j in range(L):
            for j0 in range(L):
                score = T[i-1][j0] + trans_scores[j0][j] + emission_scores[i,j]
                if score > T[i,j]:
                    T[i,j] = score
                    back[i,j] = j0

    # Add in the end scores
    for j in range(L):
        T[N-1,j] += end_scores[j]

    # Backtrack
    y = [np.argmax(T[-1])]
    for i in range(N-1, 0, -1):
        y.append(back[i, y[-1]])

    return (np.amax(T[-1]), y[::-1])
