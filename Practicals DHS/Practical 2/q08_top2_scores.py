# Finding the two highest scores

num = int(input("Number of students: "))
students = {}
scores = []
for i in range(num):
    name = input("Name: ")
    score = int(input("Score: "))
    if score in students:
        students[score].append(name)
    else:
        students[score] = []
        students[score].append(name)
    scores.append(score)
scores.sort()
highest = students[scores[len(scores)-1]]
x = len(highest)
second = students[scores[len(scores)-(x+1)]]
print ("Highest score: {0}".format(' and '.join(highest)))
print ("Second highest score: {0}".format(' and '.join(second)))
