# Word Funnel Challenge:
# Given 2 strings of letters, determine whether the second can
# be made from the first by removing one letter. The remaining
# letters must stay in the same order.
# Author: isaacsutor
# Version: 2018912

# Solution Ex.
# funnel("leave", "eave") => true
# funnel("reset", "rest") => true
# funnel("dragoon", "dragon") => true
# funnel("eave", "leave") => false
# funnel("sleet", "lets") => false
# funnel("skiff", "ski") => false


def funnel(word_one, word_two):
    found_match = False
    i = 0
    for letter in word_one:
        if i-1 < len(word_one):
            compare_with = word_one[:i] + word_one[i+1:]
            i += 1
            if compare_with == word_two:
                found_match = True
    print(found_match)
    return found_match


funnel("leave", "eave")
funnel("reset", "rest")
funnel("dragoon", "dragon")
funnel("eave", "leave")
funnel("sleet", "lets")
funnel("skiff", "ski")

