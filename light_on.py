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
    # for lines in in_out_times:
        #in_out_times = lines.split(' ')
    print(in_times)
    print("\n")
    print(out_times)


        # in_times += in_out_times[0]
        # out_times += in_out_times[1]
        # in_times = int(in_times, 10)
        # light_on_time = 100
        # light_off_time = 0
        # i = 0
        # for times in in_times:
            # if times < light_on_time:
                # light_on_time = times
            # if times+1 >= out_times[i]:
                # light_off_time = out_times[i]
            # i += 1


times = "1 3 \n 2 3 \n 4 5"
light_calc(times)
