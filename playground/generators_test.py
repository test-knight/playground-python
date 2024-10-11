import os
import psutil
import time
import random
import itertools

names = ["Riaz", "Fiaz", "Umma", "Sarah"]
majors = ["Math", "Science", "Literature", "Tailoring"]
memory_before = psutil.Process(os.getpid()).memory_info().rss / (1024 ** 2)
print("Memory Before Processing: {} MB".format(memory_before))

# creating list of people without generators
def people_list(num_people):
    result = []
    for i in range(num_people):
        person = {
            "id": i,
            "name": random.choice(names),
            "major": random.choice(majors)
        }
        result.append(person)
    return result


# creating list of people with generators
def people_generator(num_people):
    for i in range(num_people):
        person = {
            "id": i,
            "name": random.choice(names),
            "major": random.choice(majors)
        }
    yield person


# t1 = time.process_time()
# people = people_list(1_000_000)
# t2 = time.process_time()

t1 = time.process_time()
print(next(itertools.islice((people_generator(1_000_000)), 11)))
t2 = time.process_time()

memory_after = psutil.Process(os.getpid()).memory_info().rss / (1024 ** 2)
print("Memory After Processing: {} MB".format(memory_after))
print("Time Taken to Process: {}s".format(t2 - t1))
