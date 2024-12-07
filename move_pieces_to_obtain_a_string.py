class Solution:
    def canChange(self, start: str, target: str) -> bool:
        start_queue, target_queue = deque([]), deque([])

        # populate the queues
        for i in range(len(start)):
            if start[i] != "_":
                start_queue.append(i)
            
            if target[i] != "_":
                target_queue.append(i)

        if len(start_queue) != len(target_queue):
            return False
        
        while start_queue:
            start_idx, target_idx = start_queue.popleft(), target_queue.popleft()

            if (
                start[start_idx] != target[target_idx]
                or (start[start_idx] == 'L' and start_idx < target_idx)
                or (start[start_idx] == 'R' and start_idx > target_idx)
            ):
                return False


        return True


        

        
