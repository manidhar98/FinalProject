import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    problem_size_time_usage_1 = {4096: 0.005515, 1048576: 0.482163, 524288: 0.242163, 466944: 0.214803,
                                 282112: 0.124667, 516096: 0.240603, 147456: 0.069539, 612352: 0.291462,
                                 655360: 0.253238, 81920: 0.042474, 19712: 0.010023, 78848: 0.035526, 79872: 0.041580,
                                 176640: 0.082628, 5520: 0.003410, 59392: 0.030078, 5632: 0.002662, 13376: 0.008111,
                                 9568: 0.006144, 5000: 0.003155, 1600: 0.001158}

    problem_size_time_usage_2 = {4096: 0.002958, 1048576: 0.591370, 524288: 0.297005, 466944: 0.266076,
                                 282112: 0.162655, 516096: 0.290642, 147456: 0.084758, 612352: 0.349608,
                                 655360: 0.373610, 81920: 0.046167, 19712: 0.011070, 78848: 0.046036,
                                 79872: 0.052244, 176640: 0.100397, 5520: 0.003321, 59392: 0.034476, 5632: 0.004437,
                                 13376: 0.015755, 9568: 0.007012, 5000: 0.003860, 1600: 0.001235}

    problem_size_memory_usage_1 = {4096: 48.0, 1048576: 9664.0, 524288: 4944.0, 466944: 4272.0, 282112: 2912.0,
                                   516096: 4992.0, 147456: 1920.0, 612352: 5664.0, 655360: 6208.0, 81920: 1040.0,
                                   19712: 576.0, 78848: 976.0, 79872: 1280.0, 176640: 2160.0, 5520: 176.0,
                                   59392: 832.0, 5632: 176.0, 13376: 432.0, 9568: 320.0, 5000: 176.0, 1600: 48.0}

    problem_size_memory_usage_2 = {4096: 160.0, 1048576: 11680.0, 524288: 6896.0, 466944: 6752.0,
                                   282112: 3296.0, 516096: 6592.0, 147456: 3056.0, 612352: 7056.0, 655360: 7920.0,
                                   81920: 2320.0, 19712: 816.0, 78848: 2176.0, 79872: 2352.0, 176640: 3168.0,
                                   5520: 208.0, 59392: 1520.0, 5632: 240.0, 13376: 256.0, 9568: 384.0, 5000: 208.0,
                                   1600: 64.0}

    problem_size_time_usage_1 = sorted(problem_size_time_usage_1.items(), key=lambda item: item[0])
    problem_size_time_usage_2 = sorted(problem_size_time_usage_2.items(), key=lambda item: item[0])

    plt.plot(np.array([a_tuple[0] for a_tuple in problem_size_time_usage_1]),
             np.array([a_tuple[1] for a_tuple in problem_size_time_usage_1]),
             marker='o', label="time_used_by_normal_method")
    plt.plot(np.array([a_tuple[0] for a_tuple in problem_size_time_usage_2]),
             np.array([a_tuple[1] for a_tuple in problem_size_time_usage_2]),
             marker='o', label="time_used_by_memory_efficient_method")
    plt.title("problem size v/s time usage")
    plt.xlabel('problem size')
    plt.ylabel('time usage (in seconds)')
    plt.legend()
    plt.show()

    problem_size_memory_usage_1 = sorted(problem_size_memory_usage_1.items(), key=lambda item: item[0])
    problem_size_memory_usage_2 = sorted(problem_size_memory_usage_2.items(), key=lambda item: item[0])

    plt.plot(np.array([a_tuple[0] for a_tuple in problem_size_memory_usage_1]),
             np.array([a_tuple[1] for a_tuple in problem_size_memory_usage_1]),
             marker='o', label="memory_used_by_normal_method")
    plt.plot(np.array([a_tuple[0] for a_tuple in problem_size_memory_usage_2]),
             np.array([a_tuple[1] for a_tuple in problem_size_memory_usage_2]),
             marker='o', label="memory_used_by_memory_efficient_method")
    plt.title("problem size v/s memory usage")
    plt.xlabel('problem size')
    plt.ylabel('memory usage (in KiloBytes)')
    plt.legend()
    plt.show()
