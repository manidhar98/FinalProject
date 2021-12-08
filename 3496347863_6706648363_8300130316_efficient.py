import re
import sys
import time

import psutil as psutil

import Constants;
from Constants import *;
from StringGenerator import *;

class MemoryEfficient:

    def __init__(self) -> None:
        self.final_seq_x = ""
        self.final_seq_y = ""
        self.min_cost = 0

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


    def space_efficient_alignment(self, X, Y):
        
        m = len(X)+1
        n = len(Y)+1

        # print('serving for:', X, Y)
        dp = [[0 for i in range(n)] for i in range(2)]


        for j in range(n):
            dp[0][j] = j*Constant.gap_penalty

        for i in range(1,m):
            dp[i%2][0] = i*Constant.gap_penalty

            for j in range(1,n):
                dp[i%2][j] = dp[i%2][j-1] + Constant.gap_penalty
                dp[i%2][j] = min(dp[i%2][j], dp[(i-1)%2][j] + Constant.gap_penalty)
                dp[i%2][j] = min(dp[i%2][j], dp[(i-1)%2][j-1] + Constant.mismatch_cost[Constant.chars[X[i-1]]][Constant.chars[Y[j-1]]])

        return dp[(m-1)%2]



    def divide_conquer_alignment(self, X, Y):
        
        m = len(X)
        n = len(Y)

        if m<=2 or n <=2:
            min_cost, X1, Y1 =  self.alignment(X, Y)

            global final_seq_x, final_seq_y
            self.final_seq_x += X1
            self.final_seq_y += Y1
            self.min_cost += min_cost
            return

        x_split_pos = m//2

        y1_seq = self.space_efficient_alignment(X[:x_split_pos], Y)
        y2_seq = self.space_efficient_alignment(X[:x_split_pos - 1:-1], Y[::-1])[::-1]

        y_split_pos = 0
        min_seq = y1_seq[0] + y2_seq[0]
        for i in range(1, n):
            temp = y1_seq[i] + y2_seq[i]
            if (y1_seq[i] + y2_seq[i]) < min_seq:
                y_split_pos = i
                min_seq = y1_seq[i] + y2_seq[i]

        self.divide_conquer_alignment(X[:x_split_pos], Y[:y_split_pos])
        self.divide_conquer_alignment(X[x_split_pos: ], Y[y_split_pos:])

if __name__ == '__main__':
    strings = []
    indices_x = []
    indices_y = []
    index = 1
    pattern = re.compile("[A-Za-z]+")

    file = open(sys.argv[1], 'r');
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
    start_memory = P2.memory_info().rss / 1024
    start_time = time.process_time()

    efficient.divide_conquer_alignment(final[0], final[1])

    min_cost, final_x, final_y =  efficient.min_cost, efficient.final_seq_x, efficient.final_seq_y
    
    end_memory = P2.memory_info().rss / 1024
    end_time = time.process_time()

    # writing into the file
    file = open('output.txt', 'w')

    file.writelines(final_x[0:50]+" "+final_x[-50:]+"\n")
    file.writelines(final_y[0:50]+" "+final_y[-50:]+"\n")
    file.writelines(str(float(min_cost))+"\n")
    file.writelines(str(end_time - start_time)+"\n")
    file.writelines(str(end_memory-start_memory))

    file.close()