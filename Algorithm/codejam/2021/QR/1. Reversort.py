# problem : https://codingcompetitions.withgoogle.com/codejam/round/000000000043580a/00000000006d0a5c#problem
# time complexity : O(N^2)
 
t = int(input())
for tc in range(1, t + 1):
    N = int(input())
    L = [int(s) for s in input().split(" ")]
    answer = 0

    for i in range(0, N-1):
        min_ele = min(L[i:])
        min_index = L.index(min_ele)

        answer += min_index - i + 1
        L[i:min_index+1] = list(reversed(L[i:min_index+1]))

    print("Case #{}: {}".format(tc, answer))
