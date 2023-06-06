A = list(map(int, input()))
B = list(map(int, input()))

love = [0] * 16

for i in range(16):
    if not i % 2:
        love[i] = A[i//2]
    else:
        love[i] = B[i//2]

while len(love) != 2:
    ans = []
    for i in range(len(love)-1):
        num = (love[i]+love[i+1]) % 10
        ans.append(num)
    love = ans

print(*love, sep="")