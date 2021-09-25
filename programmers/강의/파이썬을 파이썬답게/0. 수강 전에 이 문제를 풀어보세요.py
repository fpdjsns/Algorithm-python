# problem : https://programmers.co.kr/learn/courses/4008/lessons/13254
# time complexity : O(N). N = |mylist|

def solution(mylist):
    answer = []
    for list in mylist:
        answer.append(len(list))
    return answer
