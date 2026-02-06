# 양꼬치
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120830
# 알고리즘: 기초
# 작성자: 안진식
# 작성일: 2026. 02. 06. 09:52:50

def solution(n, k):
    dc=0
    if n>=10:
        dc = int(n/10)
    result = (n*12000)+((k-dc)*2000)
    return result