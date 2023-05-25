n = int(input())

if not n:
    print(0)
    exit(0)

num_A, num_B = 0, 1

for i in range(n - 1):
    num_A, num_B = num_B % 1000000007, (num_A + num_B) % 1000000007

print(num_B)