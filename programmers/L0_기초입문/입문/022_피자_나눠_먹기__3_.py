# 피자 나눠 먹기 (3)
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120816
# 알고리즘: 기초
# 작성자: 안진식
# 작성일: 2026. 02. 12. 09:41:21

def solution(slice, n):
    if n%slice != 0 :
        return int(n/slice)+1
    elif n%slice ==0:
        return n/slice