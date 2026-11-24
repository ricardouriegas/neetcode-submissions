class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        time_stack = []

        for i in range(len(position)):
            cars.append((position[i], speed[i]))

        cars.sort(reverse=True)

        for c, s in cars: # car position, speed
            time = (target - c) / s
            time_stack.append(time)

            if len(time_stack) > 1 and time_stack[-1] <= time_stack[-2]:
                # target = 10
                # A: 1,4 with a total time to get to the target of: 2.25
                # B; 3,2 with a total time to get to the target of: 3.5
                # stack = [B, A]
                # A will collapse with B bc its getting to the target in less time than B
                # which is close to the target 
                time_stack.pop()

        return len(time_stack)
