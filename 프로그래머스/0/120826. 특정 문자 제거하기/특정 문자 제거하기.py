def solution(my_string, letter):
    answer = []
    for alpha in my_string:
        answer.append(alpha)
        if letter == alpha:
            answer.remove(alpha)
            
    answer = ''.join(answer)

    return answer