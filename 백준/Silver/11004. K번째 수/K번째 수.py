import sys
input = sys.stdin.readline

N, K = map(int, input().split())

nums = list(map(int, input().split()))

print(sorted(nums)[K-1])