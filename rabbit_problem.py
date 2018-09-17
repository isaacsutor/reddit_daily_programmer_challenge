# The Rabbit Problem:
# Description
# Rabbits are known for their fast breeding, but how soon will they dominate the earth?
# Starting with a small population of male and female rabbits we have to figure out how
# long it will take for them to outnumber humans 2:1.
# Every month a fertile female will have 14 offspring (5 males and 9 females).
# A female rabbit is fertile when it has reached the age of 4 months, they never stop being fertile.
# Rabbits die at the age of 8 years (96 months).
# Input description
# You will be given a list of numbers as following:
# Male_rabbits Female_rabbits Rabbits_needed_alive
# The initial rabbits will always be 2 months old and fertile females will always produce 14
# offspring (5 male, 9 female)
# Every month that passes things should be done in this order:
# Fertile female reproduce	(so 7 year & 11 months old will reproduce)
# rabbits age (except newborn) (and rabbits reaching 8 years will die, the 7 year & 11 months old will die)
# Author: isaacsutor
# Version: 2018916

BUNNY_DEATH_AGE = 96
BUNNY_FERTILE_AGE = 4
BUNNY_INIT_AGE = 2
BUNNY_MALE_PER_MONTH = 4
BUNNY_FEMALE_PER_MONTH = 9


def breed(females):
    breeding_females = sum(females[BUNNY_FERTILE_AGE:])
    new_males = breeding_females * BUNNY_MALE_PER_MONTH
    new_females = breeding_females * BUNNY_FEMALE_PER_MONTH
    return new_males, new_females


def bunny_problem(init_m_bun, init_f_bun, pop_max):
    males = [0] * (BUNNY_DEATH_AGE+1)
    females = [0] * (BUNNY_DEATH_AGE+1)
    total_population = init_f_bun + init_m_bun
    while total_population < pop_max:
        breed(females)


    # 1 female = 4 males, 9 females per litter
    # fertile = 4 months
    # death age = 96 months
    # stage 1: females reproduce
    # stage 2: +1 month to age. kill 96 month
