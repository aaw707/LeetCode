class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
            
        # graph data structure
        # key: node
        # value: [(target, time)]
        graph = {}
        
        # add each path into graph
        for source, target, time in times:
            if source in graph:
                graph[source].append((target, time))
            else:
                graph[source] = [(target, time)]
                
        # record the time to reach each node
        # key: node i in range(1, n + 1)
        # val: minimum time to reach to this node
        t = {}
        # initialize time as inf
        for i in range(1, n + 1):
            t[i] = float('inf')                
                
        # nodes to visit
        queue = [(k, 0)]
        
        # bfs for each node to visit
        while queue:
            source, total_time = queue.pop(0)
            if total_time < t[source]:
                # update t with current min time to visit this node
                t[source] = total_time
                # bfs the targets of this node
                if source in graph:
                    for target, time in graph[source]:
                        # add each target to "to-visit" queue
                        queue.append((target, total_time + time)) # add on the time
                
        # all nodes can be visited are visited
        time_to_traverse = max(t.values())
        # if all nodes are visited
        if time_to_traverse < float('inf'):
            return time_to_traverse
        else:
            # still nodes not visited. time at default inf
            return -1
        