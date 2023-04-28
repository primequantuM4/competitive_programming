class Solution:
    def racecar(self, target: int) -> int:
        queue = deque([(0, 1, 0)])
        visited = {(0, 1)}

        while queue:
            cur_position, cur_speed, level = queue.popleft()
            reverse_speed = -1 if cur_speed > 0 else 1
            if cur_position == target:
                return level

            if (cur_position, reverse_speed) not in visited:
                visited.add((cur_position, reverse_speed))
                queue.append((cur_position, reverse_speed, level + 1))

            if (cur_position + cur_speed, cur_speed * 2) not in visited:
                visited.add((cur_position + cur_speed, cur_speed * 2))
                queue.append((cur_position + cur_speed, cur_speed * 2, level + 1))

        return -1
