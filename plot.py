import re
import sys
import time
import psutil as psutil
from Constants import *
from StringGenerator import *
from basic import Basic

if __name__ == '__main__':
    problem_size_time_usage_1 = {}
    problem_size_memory_usage_1 = {}
    problem_size_time_usage_2 = {}
    problem_size_memory_usage_2 = {}

    for i in range(21):

        strings = []
        indices_x = []
        indices_y = []
        index = 1

        pattern = re.compile("[A-Za-z]+")
        file = open('input'+str(i)+'.txt', 'r')
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
        start1 = P2.memory_info().rss / 1024
        start = time.process_time()
        min_cost, final_x, final_y = basic.get_minimum_penalty(final[0], final[1])
        start2 = P2.memory_info().rss / 1024
        # file = open('output.txt', 'w')
        # file.writelines(final_x[0:50] + " " + final_x[-50:] + "\n")
        # file.writelines(final_y[0:50] + " " + final_y[-50:] + "\n")
        # file.writelines(str(float(min_cost)) + "\n")
        # file.writelines(str(time.process_time() - start) + "\n")
        # file.writelines(str(start2 - start1))
        # file.close()

        problem_size_time_usage_2[len(final[0]) * len(final[1])] = time.process_time() - start
        problem_size_memory_usage_2[len(final[0]) * len(final[1])] = (peak / 10 ** 3)


