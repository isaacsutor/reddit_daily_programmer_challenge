# Light On Challenge:
# There is a light in a room which lights up only when someone is in the room (think motion detector).
# You are given a set of intervals in entrance and exit times as single integers, and expected to find
# how long the light has been on. When the times overlap, you need to find the time between the smallest
# and the biggest numbers in that interval.
# Author: isaacsutor
# Version: 2018914

def light_calc(enter_exit_times):
    times_person_deliminated = enter_exit_times.split("\n")
    in_times = ""
    out_times = ""
    for lines in times_person_deliminated:
        in_out_times = lines.split(" ")
        in_times += in_out_times[0] + " "
        out_times += in_out_times[1] + " "








times = "1 3"