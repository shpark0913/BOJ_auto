import sys
input = sys.stdin.readline

N = int(input())

people = []
for _ in range(N):
    people.append(input().split())
dictionary = {}

for person in people:
    if person[0] in dictionary.keys():
        dictionary[person[0]] += 1
    else:
        dictionary[person[0]] = 1

ans = []

for a, b in dictionary.items():
    if b % 2:
        ans.append(a)

ans.sort(reverse=True)

for a in ans:
    print(a)