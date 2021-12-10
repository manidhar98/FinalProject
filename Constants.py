class Utils:
    def __init__(self):
        self.min_cost = 0

    def reconstruct_sequence_alignment(self,dp, X, Y):
        i = len(X)
        j = len(Y)

        X1 = ""
        Y1 = ""

        while i != 0 and j != 0:

            if dp[i][j] == Constant.gap_penalty + dp[i][j - 1]:
                X1 += '_'
                Y1 += Y[j - 1]
                j -= 1
                self.min_cost += Constant.gap_penalty
            elif dp[i][j] == dp[i - 1][j] + Constant.gap_penalty:
                X1 += X[i - 1]
                Y1 += '_'
                i -= 1
                self.min_cost += Constant.gap_penalty
            else:
                X1 += X[i - 1]
                Y1 += Y[j - 1]
                i -= 1
                j -= 1
                self.min_cost += Constant.mismatch_cost[Constant.chars[X[i]]][Constant.chars[Y[j]]]

        while i != 0:
            X1 += X[i - 1]
            Y1 += "_"

            i -= 1
            self.min_cost += Constant.gap_penalty

        while j != 0:
            Y1 += Y[j - 1]
            X1 += "_"

            j -= 1
            self.min_cost += Constant.gap_penalty

        return dp[len(X)][len(Y)], X1[::-1], Y1[::-1]


class Constant:
    gap_penalty = 30
    chars = {
        'A': 0,
        'C': 1,
        'G': 2,
        'T': 3
    }
    mismatch_cost = [
        [0, 110, 48, 94],
        [110, 0, 118, 48],
        [48, 118, 0, 110],
        [94, 48, 110, 0]
    ]
