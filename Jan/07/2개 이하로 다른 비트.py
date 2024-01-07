def solution(numbers):
    answer = []
    for num in numbers:
        b_num = bin(num)
        r_num = b_num[::-1]
        r_num = r_num.replace('b0', '0000b0', 1)
        if num % 2 == 0:
            r_num = r_num.replace('0','1', 1)

        else:
            r_num = r_num.replace('10', '01', 1)
            
        o_num = int(r_num[::-1], 2)
        answer.append(o_num)

    return answer