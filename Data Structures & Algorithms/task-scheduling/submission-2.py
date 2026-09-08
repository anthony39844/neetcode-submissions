class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        time = 0
        count = Counter(tasks)

        heap = [-x for x in count.values()]
        heapq.heapify(heap)

        q = deque()

        while heap or q:
            time += 1

            if q and q[0][1] == time:
                x, _ = q.popleft()
                heapq.heappush(heap, x)

            if heap:
                x = heapq.heappop(heap) + 1
                if x < 0:
                    q.append((x, time + n + 1))
            elif q:
                time = q[0][1] - 1
        
        return time
            


