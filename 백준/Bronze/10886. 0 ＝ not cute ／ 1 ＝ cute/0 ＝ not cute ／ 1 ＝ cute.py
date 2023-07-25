N = int(input())

searches = [int(input()) for _ in range(N)]

num1 = searches.count(1)
num0 = searches.count(0)

print("Junhee is not cute!") if num0 > num1 else print("Junhee is cute!")