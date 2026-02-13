# 순서쌍의 개수
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120836
# 알고리즘: 기초
# 작성자: 안진식
# 작성일: 2026. 02. 13. 09:40:58

# def solution(n):
#     i=0
#     for a in range(1,n+1):
#         if n%a==0:
#             i+=1
#     return i
def solution(n):
    return len([number for number in range(1,n+1) if n%number==0])