def solution(array):
    array.sort()
    length = len(array)
    
    if length % 2 == 0:
        # 배열의 길이가 짝수인 경우
        # 중앙 두 값의 평균을 반환
        middle1 = array[length//2 - 1]
        middle2 = array[length//2]
        answer = (middle1 + middle2) / 2
    else:
        # 배열의 길이가 홀수인 경우
        # 중앙 값을 반환
        answer = array[length//2]
    
    return answer