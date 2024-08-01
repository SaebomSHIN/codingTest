def solution(hp):
    answer = 0
    # gen = 5
    # mid_ant = 3
    # ant = 1
    
    answer = hp // 5 + (hp % 5) // 3 + ((hp % 5) % 3) // 1
    return answer