
# exercise 1
from collections import deque

def bfs_shortest_path(graph, start, goal):
    if start == goal:
        return [start]
    
    queue = deque([(start, [start])])
    
    visited = set()
    visited.add(start)
    
    while queue:
    
        current_node, path = queue.popleft()
        for neighbor in graph[current_node]:
            if neighbor not in visited:
                visited.add(neighbor)
                new_path = path + [neighbor]
                if neighbor == goal:
                    return new_path
                
                queue.append((neighbor, new_path))
    
    return None
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

print(bfs_shortest_path(graph, 'A', 'F')) 

# exercise 2
def detect_cycle_bfs(graph):
    visited = set()
    for start in graph:
        if start not in visited:
            queue = deque([(start, None)])
            visited.add(start)

            while queue:
                current_node, parent = queue.popleft()

                for neighbor in graph[current_node]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, current_node))
                    elif neighbor != parent:
                        return True


    return False
graph_with_cycle = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B', 'E'],
    'E': ['B', 'D'],
    'F': ['C']
}

graph_without_cycle = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A'],
    'D': ['B']
}

print(detect_cycle_bfs(graph_with_cycle))  
print(detect_cycle_bfs(graph_without_cycle))  

# exercise 3
import heapq

def dijkstra(graph, start):
    priority_queue = []
    heapq.heappush(priority_queue, (0, start))

    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0

    previous_nodes = {vertex: None for vertex in graph}
    
    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)
        
        if current_distance > distances[current_vertex]:
            continue
        for neighbor, weight in graph[current_vertex]:
            distance = current_distance + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_vertex
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances, previous_nodes

def reconstruct_path(previous_nodes, start, goal):
    path = []
    current = goal
    while current is not None:
        path.append(current)
        current = previous_nodes[current]
    path.reverse()
    return path if path[0] == start else []

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}

distances, previous_nodes = dijkstra(graph, 'A')
print("Shortest distances:", distances)
print("Shortest path from A to D:", reconstruct_path(previous_nodes, 'A', 'D'))

#exercise 4
from collections import deque

def is_bipartite(graph):
    color = {}


    for start in graph:
        if start not in color:
    
            queue = deque([start])
            color[start] = 0  
            
            while queue:
                current = queue.popleft()

                
                for neighbor in graph[current]:
                    if neighbor not in color:
                
                        color[neighbor] = 1 - color[current]
                        queue.append(neighbor)
                    elif color[neighbor] == color[current]:
                
                        return False
    
    #
    return True

graph_bipartite = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C']
}

graph_not_bipartite = {
    'A': ['B', 'C'],
    'B': ['A', 'C'],
    'C': ['A', 'B']
}

print(is_bipartite(graph_bipartite))  
print(is_bipartite(graph_not_bipartite))  

