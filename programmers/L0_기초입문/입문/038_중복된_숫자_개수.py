# 중복된 숫자 개수
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120583
# 알고리즘: 기초
# 작성자: 안진식
# 작성일: 2026. 02. 27. 09:32:13

def solution(array, n):
    sum=0
    for i in array:       
        if i==n:
            sum+=1
    return sum