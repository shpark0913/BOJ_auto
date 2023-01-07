medals = {}
students = []

for _ in range(N := int(input())):
    nationNum, stuNum, grade = map(int, input().split())
    if nationNum not in medals.keys():
        medals[nationNum] = 0
    students.append([nationNum, stuNum, grade])

students.sort(key=lambda x: x[2])

for _ in range(3):
    person = students.pop()
    while medals[person[0]] == 2:
        person = students.pop()
    medals[person[0]] += 1
    print(person[0], person[1])