def solution(n):
    answer = 0
    tmp = n ** (1/2)
    if round(tmp, 1) == tmp:
        answer = 1
    else:
        answer = 2
    
    return answer