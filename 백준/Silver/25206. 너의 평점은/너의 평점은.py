grades = {
    'A+': 4.5,
    'A0': 4.0,
    'B+': 3.5,
    'B0': 3.0,
    'C+': 2.5,
    'C0': 2.0,
    'D+': 1.5,
    'D0': 1.0,
    'F': 0.0,
}

chihoons = list(input().split() for _ in range(20))

sum = 0
sum_grade = 0
for elt in chihoons:
    if elt[2] != 'P':
        sum += float(elt[1])*grades[elt[2]]
        sum_grade += float(elt[1])
print(sum/sum_grade)