# Light On Challenge:
# There is a light in a room which lights up only when someone is in the room (think motion detector).
# You are given a set of intervals in entrance and exit times as single integers, and expected to find
# how long the light has been on. When the times overlap, you need to find the time between the smallest
# and the biggest numbers in that interval.
# Author: isaacsutor
# Version: 20190101

def light_calc(enter_exit_times):
    in_out_times = enter_exit_times.split()
    in_times = []
    out_times = []
    for item in range(0, len(in_out_times) - 1, 2):
        in_times.append(in_out_times[item])
        out_times.append(in_out_times[item+1])
    # print(in_times)
    # print("\n")
    # print(out_times)

    light_on_runtime = 0
    count_out = 0
    count_in = 0
    light_on = False
    for i in range(1, 10):
        if not light_on:
            if str(i) == in_times[count_in]:
                light_on = True
                light_on_runtime += 1
            # i = in_times[count_in]
            if count_in < (len(in_times) - 1):
                count_in += 1
        else:
            if out_times[count_out] <= in_times[count_in]:
                light_on = False
            else:
                light_on_runtime += 1
            if (int(in_times[count_in]) <= i) and (count_in < (len(in_times) - 1)):
                count_in += 1
        # print("Time Step: " + str(i))
        # print("Next On Time: " + in_times[count_in])
        # print("Next Off: " + out_times[count_out])
        # print("Light runtime: " + str(light_on_runtime))
        # print()

    print(light_on_runtime)


times = "1 3 \n 2 3 \n 4 5"
# times2 = "2 4 \n 3 6 \n 1 3 \n 6 8"
# times3 = "6 8 \n 5 8 \n 8 9 \n 5 7 \n 4 7"
light_calc(times)
# light_calc(times2)
# light_calc(times3)
