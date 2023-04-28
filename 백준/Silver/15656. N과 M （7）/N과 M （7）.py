N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))

ans = []

def dfs():
    if len(ans) == M:
        print(*ans)
        return
    for i in range(N):
        ans.append(nums[i])
        dfs()
        ans.pop()

dfs()