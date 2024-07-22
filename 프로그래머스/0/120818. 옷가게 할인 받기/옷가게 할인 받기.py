def solution(price):
    if price >= 500000:
        discount = 0.2  # 20% 할인
    elif price >= 300000:
        discount = 0.1  # 10% 할인
    elif price >= 100000:
        discount = 0.05  # 5% 할인
    else:
        discount = 0  # 할인 없음
    
    answer = price - (price * discount)
    
    return int(answer)