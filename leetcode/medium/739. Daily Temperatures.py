
/**
 * problem : https://leetcode.com/problems/daily-temperatures/
 * time complexity : O(N)
 * data structure : stack
 */

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        st = []
        answer = []
        for idx, temp in reversed(list(enumerate(temperatures))):
            while 1:
                if not st: break
                ele = st[-1]
                if ele[0] <= temp:
                    st.pop()
                    continue;
                break;
            if st: answer.append(st[-1][1] - idx)
            else: answer.append(0)
            st.append([temp, idx])
        answer.reverse()
        return answer
