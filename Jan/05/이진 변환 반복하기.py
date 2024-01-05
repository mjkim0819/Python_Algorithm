def solution(s):
    answer = []
    cnt = 0     
    zero = 0
    
    while True:
        if s == "1":
            break
            
        zero += s.count("0")  #문자열의 0의 개수 세기
        s = s.replace('0', '')
        s = bin(len(s))[2:]      #2진수로 변환
        
        cnt +=1
        
    answer = [cnt, zero]    
    return answer
