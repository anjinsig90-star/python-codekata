# 배열의 유사도
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120903
# 알고리즘: 기초
# 작성자: 안진식
# 작성일: 2026. 02. 12. 09:55:20

def solution(s1, s2):
    total = 0
    for a in s1:
        for b in s2:
            if a==b:
                total+=1
    return total