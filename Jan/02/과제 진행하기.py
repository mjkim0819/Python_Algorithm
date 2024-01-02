def solution(plans):
    answer = []
    for i in range(len(plans)):
        h, m = map(int, plans[i][1].split(':'))
        plans[i][1] = h*60+m # 분으로 계산 변경
        plans[i][2] = int(plans[i][2])
        
    plans.sort(key=lambda x:x[1]) # 시작 시간으로 정렬
    stack = [] # 중간에 그만 둔 plan 저장
    for i in range(len(plans)):
        if i == len(plans)-1:
            stack.append(plans[i])
            break
        
        sub, st, t = plans[i]
        nsub, nst, nt = plans[i+1]
        if st + t <= nst:
            answer.append(sub)
            temp_time = nst - (st+t)
            
            while temp_time != 0 and stack:
                tsub, tst, tt = stack.pop()
                if temp_time >= tt:
                    answer.append(tsub)
                    temp_time -= tt
                else:
                    stack.append([tsub, tst, tt - temp_time])
                    temp_time = 0
            
        else:
            plans[i][2] = t - (nst - st)
            stack.append(plans[i])
        
    while stack:
        sub, st, tt = stack.pop()
        answer.append(sub)

    return answer
