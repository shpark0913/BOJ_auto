N = int(input())
N_binary = bin(N)[2:][::-1]
print(int(str(N_binary), 2))