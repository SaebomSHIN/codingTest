def solution(num_list, n):
    answer = []
    for char in range(0, len(num_list), n):
        answer.append(num_list[char])
    return answer