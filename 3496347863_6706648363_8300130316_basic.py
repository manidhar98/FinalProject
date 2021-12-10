import re
import sys
import time
import psutil as psutil

import importlib
string_generator = importlib.import_module('3496347863_6706648363_8300130316_string_generator')
utils_constants = importlib.import_module('3496347863_6706648363_8300130316_utils_constants')

Constant = utils_constants.Constant
Utils = utils_constants.Utils
InputGenerator = string_generator.InputGenerator

class Basic:

    def get_minimum_penalty(self, str1, str2):
        str1_length = len(str1)
        str2_length = len(str2)

        dp = [[0 for i in range(str2_length + 1)] for j in range(str1_length + 1)]

        for i in range(0, str1_length + 1):
            dp[i][0] = i * Constant.gap_penalty
        for i in range(0, str2_length + 1):
            dp[0][i] = i * Constant.gap_penalty

        for i in range(1, str1_length + 1):
            for j in range(1, str2_length + 1):
                if str1[i - 1] == str2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    mismatch_penalty_value = Constant.mismatch_cost[Constant.chars[str1[i - 1]]][
                        Constant.chars[str2[j - 1]]]
                    dp[i][j] = min(dp[i - 1][j - 1] + mismatch_penalty_value,
                                   dp[i - 1][j] + Constant.gap_penalty,
                                   dp[i][j - 1] + Constant.gap_penalty)
        util = Utils()
        return util.reconstruct_sequence_alignment(dp, str1, str2)


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
    
    basic = Basic()
    P2 = psutil.Process()
    
    start_memory = P2.memory_info().rss / 1024
    start_time = time.process_time()

    min_cost, final_x, final_y = basic.get_minimum_penalty(final[0], final[1])

    end_memory = P2.memory_info().rss / 1024
    end_time = time.process_time()

    # writing into the file
    file = open('output.txt', 'w')
    
    file.writelines(final_x[0:50] + " " + final_x[-50:] + "\n")
    file.writelines(final_y[0:50] + " " + final_y[-50:] + "\n")
    file.writelines(str(float(min_cost)) + "\n")
    file.writelines(str(end_memory - start_memory)+"\n")
    file.writelines(str(end_time - start_time))
    
    file.close()
