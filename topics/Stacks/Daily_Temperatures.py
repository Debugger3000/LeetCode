class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        leng = len(temperatures)
        answer = [0] * leng
        stack = []

        for i, temp in enumerate(temperatures):
            # Compare current temp with the last stored temp in the stack
            while stack and temp > temperatures[stack[-1]]:
                prev_day = stack.pop()
                answer[prev_day] = i - prev_day
            stack.append(i)
        return answer

# enumerate - just useful to grab value and index

# Use array to store answers
# Use stack to store indices
