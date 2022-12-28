while 1:
    N = int(input())
    if N == 0: break
    students = {}
    tallest = 0
    for n in range(N):
        name, height = input().split()
        students[name] = float(height)
        if float(height) >= tallest:
            tallest = float(height)
    tallest_students = []
    for key, value in students.items():
        if value == tallest:
            tallest_students.append(key)
    print(*tallest_students)

