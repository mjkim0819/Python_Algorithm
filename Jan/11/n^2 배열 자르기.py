# 시간 초과
def solution(n, left, right):
  answer = []
  for row in range(1, n + 1):
    for col in range(1, n + 1):
      if col >= row:
        answer.append(row)
      else:
        answer.append(col)
  return answer[left : right + 1]
