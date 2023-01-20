while 1:
    cnt = 0
    N = int(input())
    printPages = [0] * (N + 1)
    if not N: break
    pages = input().split(',')
    for page in pages:
        if '-' in page:
            page = page.split('-')
            if int(page[0]) < int(page[1]):
                for i in range(int(page[0]), int(page[1])+1):
                    if i <= N:
                        printPages[i] = 1
            elif int(page[0]) == int(page[1]) and int(page[0]) <= N:
                printPages[int(page[0])] = 1
        else:
            if int(page) <= N:
                printPages[int(page)] = 1
    for num_1 in printPages:
        if num_1 == 1:
            cnt += 1
    print(cnt)

