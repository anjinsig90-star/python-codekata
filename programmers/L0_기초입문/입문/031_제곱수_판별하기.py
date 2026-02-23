# 제곱수 판별하기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120909
# 알고리즘: 기초
# 작성자: 안진식
# 작성일: 2026. 02. 23. 09:38:43

def solution(n):
    for i in range(1,n+1):
        if i*i==n:
            return 1
    return 2