def solution(my_string):
    answer = ''
    vowel = ['a', 'e', 'i', 'o' ,'u']
    
    for item in vowel:
        my_string = my_string.replace(item, '')
        answer = my_string
        
    return answer