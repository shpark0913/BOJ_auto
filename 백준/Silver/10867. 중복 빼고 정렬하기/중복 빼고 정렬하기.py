N = int(input())

numbers = set(map(int, input().split()))

numbersList = sorted(list(numbers))

print(*numbersList)