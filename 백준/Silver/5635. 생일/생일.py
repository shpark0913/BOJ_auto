students = []
young = 1990
old = 2010
old_members = []
young_members = []
oldest = ''
youngest = ''

for _ in range(N := int(input())):
    name, d, m, y = input().split()
    students.append([name, int(d), int(m), int(y)])
    if int(y) >= young:
        young = int(y)
    if int(y) <= old:
        old = int(y)


for elt in students:
    if elt[-1] == old:
        old_members.append(elt)
    if elt[-1] == young:
        young_members.append(elt)

# print(old_members)

if len(old_members) == 1:
    oldest = old_members[-1][0]
else:
    m = 12
    for elt in old_members:
        if elt[2] <= m:
            m = elt[2]
    new_old_members = []
    for elt in old_members:
        if elt[2] == m:
            new_old_members.append(elt)
    # print(new_old_members)
    if len(new_old_members) == 1:
        oldest = new_old_members[0][0]
    else:
        d = 31
        for elt in new_old_members:
            if elt[1] <= d:
                oldest = elt[0]
                d = elt[1]


if len(young_members) == 1:
    youngest = young_members[-1][0]
else:
    m = 1
    for elt in young_members:
        if elt[2] >= m:
            m = elt[2]
    new_young_members = []
    for elt in young_members:
        if elt[2] == m:
            new_young_members.append(elt)
    if len(new_young_members) == 1:
        youngest = new_young_members[0][0]
    else:
        d = 1
        for elt in new_young_members:
            if elt[1] >= d:
                youngest = elt[0]
                d = elt[1]
print(youngest)
print(oldest)