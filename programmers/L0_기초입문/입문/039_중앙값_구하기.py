# 중앙값 구하기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120811
# 알고리즘: 기초
# 작성자: 안진식
# 작성일: 2026. 02. 27. 09:39:07

#import numpy as np
#def solution(array):
#    return np.median(array)

def solution(array):
    array.sort()
    return array[int(len(array) / 2)]
