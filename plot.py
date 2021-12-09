import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    problem_size_time_usage_1 = {128: 0.005515, 2048: 0.482163, 1536: 0.242163, 1376: 0.214803,
                                 1072: 0.124667, 1472: 0.240603, 832: 0.069539, 1568: 0.291462,
                                 1664: 0.253238, 576: 0.042474, 288: 0.010023, 576: 0.035526, 608: 0.041580,
                                 848: 0.082628, 152: 0.003410, 488: 0.030078, 152: 0.002662, 240: 0.008111,
                                 196: 0.006144, 250: 0.003155, 82: 0.001158}

    problem_size_time_usage_2 = {128: 0.008833, 2048: 1.498575, 1536: 0.75178, 1376: 0.6632,
                                 1072: 0.41098, 1472: 0.73636, 832: 0.21471, 1568: 0.87127,
                                 1664: 0.9505, 576: 0.12510, 288: 0.03685, 576: 0.11958,
                                 608: 0.12060, 848: 0.26050, 152: 0.01113, 488: 0.09452, 152: 0.012575,
                                 240: 0.025762, 196: 0.019883, 250: 0.010538, 82: 0.00409}

    problem_size_memory_usage_1 = {128: 48.0, 2048: 9664.0, 1536: 4944.0, 1376: 4272.0, 1072: 2912.0,
                                   1472: 4992.0, 832: 1920.0, 1568: 5664.0, 1664: 6208.0, 576: 1040.0,
                                   288: 576.0, 576: 976.0, 608: 1280.0, 848: 2160.0, 152: 176.0,
                                   488: 832.0, 152: 176.0, 240: 432.0, 196: 320.0, 250: 176.0, 82: 48.0}

    problem_size_memory_usage_2 = {128: 16.0, 2048: 192.0, 1536: 176.0, 1376: 176.0,
                                   1072: 192.0, 1472: 272.0, 832: 48.0, 1568: 192.0, 1664: 144.0,
                                   576: 48.0, 288: 32.0, 576: 32.0, 608: 64.0, 848: 192.0,
                                   152: 16.0, 488: 32.0, 152: 16.0, 240: 32.0, 196: 32.0, 250: 16.0,
                                   82: 16.0}

    problem_size_time_usage_1 = sorted(problem_size_time_usage_1.items(), key=lambda item: item[0])
    problem_size_time_usage_2 = sorted(problem_size_time_usage_2.items(), key=lambda item: item[0])

    plt.plot(np.array([a_tuple[0] for a_tuple in problem_size_time_usage_1]),
             np.array([a_tuple[1] for a_tuple in problem_size_time_usage_1]),
             marker='o', label="time_used_by_basic_version")
    plt.plot(np.array([a_tuple[0] for a_tuple in problem_size_time_usage_2]),
             np.array([a_tuple[1] for a_tuple in problem_size_time_usage_2]),
             marker='o', label="time_used_by_efficient_version")
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
