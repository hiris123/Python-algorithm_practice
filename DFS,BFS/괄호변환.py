def correct_str(x): # 올바른 괄호 문자열인지 확인
    a  = []
    for i in x:
        if i == '(':
            a.append(i)
        else: # i == ')'
            if not a: # a가 비어있다면
                return False # 짝이 안 맞으니까
        	a.pop() # 짝이 맞으면, pop
    return True

def balance_str(x): # 균형잡힌 괄호 문자열인지 확인: u와 v를 가르는 인덱스를 구하자
    left, right = 0, 0
    for i in range(len(x)):
        if x[i] == '(':
            left += 1
        else:
            right += 1
        if left == right:
            return x[:i + 1], x[i + 1:]
        
def stage_4_4(x): # 4-4 단계 함수
    x_4_4 = ''
    for i in x[1:-1]:
        if i == '(':
            x_4_4 += ')'
        else:
            x_4_4 += '('
    return x_4_4

answer = ''
def solution(p):
    global answer
    if not p or correct_str(p): # 1. 빈 문자열이거나 올바른 괄호인 경우, 그대로 반환
        return p
    u, v = balance_str(p) # 2. u, v로 나눔
    if correct_str(u): # 3-1.
        return u + solution(v)
    else: # 4.
        answer +='(' + solution(v) + ')'+ stage_4_4(u)
    return answer