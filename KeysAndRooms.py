class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        queue = deque([0])
        rooms_visited = {0}

        while queue:
            current_room = queue.popleft()
            rooms_visited.add(current_room)
        
            for room in rooms[current_room]:
                if room not in rooms_visited:
                    queue.append(room)


        return  len(rooms_visited) == len(rooms)
