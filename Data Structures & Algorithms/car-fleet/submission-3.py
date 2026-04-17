class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        car_stack = []
        pos_speed = []
        prev = tuple()
        for i in range(len(position)):
            pos_speed.append((position[i], speed[i]))
        pos_speed = sorted(pos_speed, key= lambda v:v[0], reverse=True)
        for i in range(len(pos_speed)):
            car_stack.append(pos_speed[i])
            if len(car_stack) >= 2:
                if (target - car_stack[-2][0])/car_stack[-2][1] >= (target - pos_speed[i][0])/pos_speed[i][1]:
                    car_stack.pop()
        
        return len(car_stack)


            
            