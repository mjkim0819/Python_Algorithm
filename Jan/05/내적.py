def solution(a, b):
    answer = 0
    add = [a, b]
    for i in range(len(a)):
        answer += add[0][i] * add[1][i]
    return answer
