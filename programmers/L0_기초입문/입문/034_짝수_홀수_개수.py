# 짝수 홀수 개수
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120824
# 알고리즘: 기초
# 작성자: 안진식
# 작성일: 2026. 02. 25. 09:48:19

def solution(num_list):
    J = 0
    H= 0
    for i in num_list:
        if i % 2 ==0:
            J+=1
        else : 
            H+=1
    return [J,H]