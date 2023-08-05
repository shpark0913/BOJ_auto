passwords = [input() for _ in range(int(input()))]

for password in passwords:
    if password[::-1] in passwords:
        print(len(password), password[len(password)//2])
        break