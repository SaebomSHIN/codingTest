def solution(rsp):
    answer = ''
    for game in rsp:
        if game == '0':
            answer += '5'
        elif game == '2':
            answer += '0'
        elif game ==  '5':
            answer += '2'
    return answer