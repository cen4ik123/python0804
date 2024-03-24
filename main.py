marks = input()
marks = marks.split()
sum = 0
for i in range(len(marks)):
    sum += int(marks[i])

mean = sum / len(marks)
print(print(mean))