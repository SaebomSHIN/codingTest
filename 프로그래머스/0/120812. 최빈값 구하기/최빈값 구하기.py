def solution(array):
    # 빈도수를 저장할 딕셔너리 생성
    freq = {}
    
    # 배열의 각 원소의 빈도수를 계산
    for num in array:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    
    # 최빈값의 빈도수와 그에 해당하는 값들을 찾음
    max_freq = max(freq.values())
    modes = [num for num, count in freq.items() if count == max_freq]
    
    # 최빈값이 여러 개면 -1을 반환, 아니면 최빈값 반환
    if len(modes) > 1:
        return -1
    else:
        return modes[0]

# 테스트 케이스
print(solution([1, 2, 3, 3, 3, 4]))  # 3
print(solution([1, 1, 2, 2]))        # -1
print(solution([1]))                 # 1