import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    problem_size_time_usage_1 = {4096: 0.005515, 1048576: 0.482163, 524288: 0.242163, 466944: 0.214803,
                                 282112: 0.124667, 516096: 0.240603, 147456: 0.069539, 612352: 0.291462,
                                 655360: 0.253238, 81920: 0.042474, 19712: 0.010023, 78848: 0.035526, 79872: 0.041580,
                                 176640: 0.082628, 5520: 0.003410, 59392: 0.030078, 5632: 0.002662, 13376: 0.008111,
                                 9568: 0.006144, 5000: 0.003155, 1600: 0.001158}

    problem_size_time_usage_2 = {4096: 0.008833, 1048576: 1.498575, 524288: 0.75178, 466944: 0.6632,
                                 282112: 0.41098, 516096: 0.073636, 147456: 0.21471, 612352: 0.87127,
                                 655360: 0.9505, 81920: 0.12510, 19712: 0.03685, 78848: 0.11958,
                                 79872: 0.12060, 176640: 0.26050, 5520: 0.01113, 59392: 0.09452, 5632: 0.012575,
                                 13376: 0.025762, 9568: 0.019883, 5000: 0.010538, 1600: 0.00409}

    problem_size_memory_usage_1 = {4096: 48.0, 1048576: 9664.0, 524288: 4944.0, 466944: 4272.0, 282112: 2912.0,
                                   516096: 4992.0, 147456: 1920.0, 612352: 5664.0, 655360: 6208.0, 81920: 1040.0,
                                   19712: 576.0, 78848: 976.0, 79872: 1280.0, 176640: 2160.0, 5520: 176.0,
                                   59392: 832.0, 5632: 176.0, 13376: 432.0, 9568: 320.0, 5000: 176.0, 1600: 48.0}

    problem_size_memory_usage_2 = {4096: 16.0, 1048576: 192.0, 524288: 176.0, 466944: 176.0,
                                   282112: 192.0, 516096: 272.0, 147456: 48.0, 612352: 192.0, 655360: 144.0,
                                   81920: 48.0, 19712: 32.0, 78848: 32.0, 79872: 64.0, 176640: 192.0,
                                   5520: 16.0, 59392: 32.0, 5632: 16.0, 13376: 32.0, 9568: 32.0, 5000: 16.0,
                                   1600: 16.0}

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
