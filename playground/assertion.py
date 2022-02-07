def avg(marks: list):
    assert len(marks) != 0, "Empty List"
    return sum(marks)/len(marks)


marks_1 = []
marks_2 = [10, 20]
print("Average:", avg(marks_2))