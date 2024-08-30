def solution(arr):
    answer = []
    for aph in arr:
        if aph >= 50 and aph % 2 == 0:
            answer.append(aph / 2)
        elif aph < 50 and aph % 2 != 0:
            answer.append(aph * 2)
        else:
            answer.append(aph)
    return answer