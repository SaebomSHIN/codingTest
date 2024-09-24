def solution(a, b):
    answer = 0
    sum = int(str(a) + str(b))
    mul = 2 * a * b
    
    if sum > mul:
        answer = sum
    else:
        answer = mul
    return answer