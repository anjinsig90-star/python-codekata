# 숨어있는 숫자의 덧셈 (1)
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120851
# 알고리즘: 기초
# 작성자: 안진식
# 작성일: 2026. 02. 26. 09:46:38

def solution(my_string):
    sum=0
    for i in my_string:
        if '0'<=i<='9':
            sum+=int(i)
    return sum