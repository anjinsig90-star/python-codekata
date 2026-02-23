# 모음 제거
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120849
# 알고리즘: 기초
# 작성자: 안진식
# 작성일: 2026. 02. 23. 09:44:16

def solution(my_string):
    m = ['a','e','i','o','u']
    for i in m:
        my_string = my_string.replace(i,'')
    return my_string