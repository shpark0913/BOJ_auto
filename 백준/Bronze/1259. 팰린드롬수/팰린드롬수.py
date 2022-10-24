while 1:
    if (n := str(input())) == '0':
        break
    m = list(map(int, n))
    m_reverse = m[::-1]
    print('yes') if m == m_reverse else print('no')