import sys

input = sys.stdin.readline

N = int(input())

books = {}

for _ in range(N):
    book = input()
    if book in books.keys():
        books[book] += 1
    else:
        books[book] = 1

books_list = sorted(books.items(), key=lambda x: (-x[1], x[0]))

print(books_list[0][0])
