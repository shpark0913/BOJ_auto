men = [input() for _ in range(5)]

FBI_men = []

for i in range(len(men)):
    if "FBI" in men[i]:
        FBI_men.append(i + 1)

print(*FBI_men) if len(FBI_men) else print("HE GOT AWAY!")