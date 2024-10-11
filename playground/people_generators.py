import psutil
import os
import random
import time
from itertools import islice

names = ["Riaz", "Fiaz", "Sarah", "Umma"]
majors = ["Mechanical", "Electrical", "Education", "Home Science"]

memory_before = psutil.Process(os.getpid()).memory_info().rss / (1024 ** 2)

print("Memory Before: {} Mb".format(memory_before))


def people_list(num_people):
    result = []
    for i in range(num_people):
        person = {
            'id': i,
            'name': random.choice(names),
            'major': random.choice(majors)
        }
        result.append(person)
    return result


def people_generator(num_people):
    for i in range(num_people):
        person = {
            'id': i,
            'name': random.choice(names),
            'major': random.choice(majors)
        }
    yield person


# t1 = time.process_time()
# people = people_list(1000000)
# t2 = time.process_time()

t1 = time.process_time()
# people = list()
t2 = time.process_time()
index = 5
next(islice(people_generator(1000000), index, None))
# print(people)
memory_after = psutil.Process(os.getpid()).memory_info().rss / (1024 ** 2)

print("Memory (After): {} Mb".format(memory_after))
print("Took {} seconds".format(t2 - t1))
