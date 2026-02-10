# 피자 나눠 먹기 (1)
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120814
# 알고리즘: 기초
# 작성자: 안진식
# 작성일: 2026. 02. 10. 09:37:05

def solution(n):
    if n<=7 :
        result = 1
    elif n%7==0 :
        result =int(n/7)
    elif n%7!=0:
        result =int(n/7)+1
    return result