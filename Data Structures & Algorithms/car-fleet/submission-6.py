class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        sorted_pos = [(position[i], speed[i]) for i in range(len(position))]
        sorted_pos.sort()
        stack = []
        if len(position) == 1:
            return 1
        for i in range(len(sorted_pos) - 1, -1, -1):
            if len(stack) == 0:
                stack.append(sorted_pos[i])
            else:
                final = stack[-1]
                pos, vel = final
                time_at_target_final = (target - pos)/vel
                time_at_target_current = (target - sorted_pos[i][0])/sorted_pos[i][1]
                if time_at_target_current > time_at_target_final:
                    stack.append(sorted_pos[i])
                else:
                    stack[-1] = max(sorted_pos[i], stack[-1])
        
        return len(stack)