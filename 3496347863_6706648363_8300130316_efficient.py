import re
import sys
import time
import psutil as psutil
from Constants import *
from StringGenerator import *


class MemoryEfficient:
    def alignment(self, X, Y):

        m = len(X) + 1
        n = len(Y) + 1

        dp = [[0 for i in range(n)] for i in range(m)]

        for i in range(m):
            dp[i][0] = i * Constant.gap_penalty

        for i in range(n):
            dp[0][i] = i * Constant.gap_penalty

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + Constant.gap_penalty
                dp[i][j] = min(dp[i][j], dp[i][j - 1] + Constant.gap_penalty)
                dp[i][j] = min(dp[i][j], dp[i - 1][j - 1] + Constant.mismatch_cost[Constant.chars[X[i - 1]]][Constant.chars[Y[j - 1]]])
        util = Utils()
        return util.reconstruct_sequence_alignment(dp, X, Y)


if __name__ == '__main__':
    strings = []
    indices_x = []
    indices_y = []
    index = 1
    pattern = re.compile("[A-Za-z]+")

    file = open(sys.argv[1], 'r')
    data = file.readlines()
    strings.append(data[0].replace("\n", ""))
    check = False
    for x in range(1, len(data)):
        temp = data[x].replace("\n", "")
        if pattern.fullmatch(temp) is not None:
            strings.append(temp)
            check = True
        elif not check:
            indices_x.append(int(temp))
        else:
            indices_y.append(int(temp))
    sg = InputGenerator(strings)
    final = [sg.inputStringGenerator(strings[0], indices_x), sg.inputStringGenerator(strings[1], indices_y)]
    efficient = MemoryEfficient()
    P2 = psutil.Process()
    start1 = P2.memory_info().rss / 1024
    start = time.process_time()
    min_cost, final_x, final_y = efficient.alignment(final[0], final[1])
    start2 = P2.memory_info().rss / 1024
    file = open('output.txt', 'w')
    file.writelines(final_x[0:50]+" "+final_x[-50:]+"\n")
    file.writelines(final_y[0:50]+" "+final_y[-50:]+"\n")
    file.writelines(str(float(min_cost))+"\n")
    file.writelines(str(time.process_time() - start)+"\n")
    file.writelines(str(start2-start1))
    file.close()
