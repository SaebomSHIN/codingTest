def solution(n):
    result = 0
    for i in range(1,n+1):
        if i % 2 == 0:
            result += i
        else:
            result

    return result

print(solution(10))
print(solution(4))