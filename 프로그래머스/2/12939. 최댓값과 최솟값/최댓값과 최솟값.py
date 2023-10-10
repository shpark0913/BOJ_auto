def solution(s):
    list_s = list(map(int, s.split()))
    list_s.sort()
    ans = ""
    ans += str(list_s[0])
    ans += " "
    ans += str(list_s[-1])
        
    return ans