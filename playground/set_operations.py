sample_set = {1.98, 98.9, 74.95, 2.5, 1, 6.3}
sample_set_copy = sample_set.copy()
print(sample_set)
print(sample_set_copy)

print(len(sample_set))

sample_set.update([88.1, 23.5, 5])

print(sample_set)

sample_set.add(33)

print(sample_set)

sample_set.clear()
print(sample_set)