def solution(my_string):
    number = [int(i) for i in my_string if i.isdigit()]
    answer = sum(number)
    return answer