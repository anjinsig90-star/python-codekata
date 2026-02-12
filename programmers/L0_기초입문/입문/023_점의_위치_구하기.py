# 점의 위치 구하기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120841
# 알고리즘: 기초
# 작성자: 안진식
# 작성일: 2026. 02. 12. 09:49:19

def solution(dot):
    if dot[0]> 0:
        if dot[1]>0 :
            return 1
        else : return 4
    if dot[0]< 0:
        if dot[1]>0 :
            return 2
        else : return 3
        