class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        #change it to a tuple with process time as the 0th index
        for i in range(len(tasks)):
            tasks[i].append(i)
        next_task, task_order = [], []
        tasks.sort()
        task_index = 0

        time_to_complete = 0
        while task_index < len(tasks) or next_task:
            if not next_task and time_to_complete < tasks[task_index][0]:
                time_to_complete = tasks[task_index][0]

            while task_index < len(tasks) and time_to_complete >= tasks[task_index][0]:
                _, process_time, index = tasks[task_index]
                heappush(next_task, (process_time, index))
                task_index += 1
            
            process_time, curr_index = heappop(next_task)

            time_to_complete += process_time
            task_order.append(curr_index)


        return task_order
