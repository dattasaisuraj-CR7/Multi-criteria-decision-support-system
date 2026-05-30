from collections import deque
import heapq
import time

# ==========================================================
# GRAPH REPRESENTATION
# ==========================================================

graph = {

    "Laptop A": ["Laptop B", "Laptop C"],

    "Laptop B": ["Laptop D", "Laptop E"],

    "Laptop C": ["Laptop F"],

    "Laptop D": ["Laptop G"],

    "Laptop E": [],

    "Laptop F": ["Laptop G"],

    "Laptop G": []
}


# ==========================================================
# HEURISTIC VALUES
# ==========================================================

heuristic = {

    "Laptop A": 7,
    "Laptop B": 5,
    "Laptop C": 4,
    "Laptop D": 3,
    "Laptop E": 6,
    "Laptop F": 2,
    "Laptop G": 0
}


# ==========================================================
# BFS SEARCH
# ==========================================================

def bfs(start):

    print("\n========== BFS SEARCH ==========")

    visited = set()

    queue = deque()

    queue.append(start)

    visited.add(start)

    while queue:

        node = queue.popleft()

        print("Visited :", node)

        for neighbor in graph[node]:

            if neighbor not in visited:

                visited.add(neighbor)

                queue.append(neighbor)


# ==========================================================
# DFS SEARCH
# ==========================================================

def dfs(node, visited):

    visited.add(node)

    print("Visited :", node)

    for neighbor in graph[node]:

        if neighbor not in visited:

            dfs(neighbor, visited)


# ==========================================================
# UNIFORM COST SEARCH
# ==========================================================

def ucs(start, goal):

    print("\n========== UNIFORM COST SEARCH ==========")

    pq = []

    heapq.heappush(pq, (0, start))

    visited = set()

    while pq:

        cost, node = heapq.heappop(pq)

        if node in visited:
            continue

        visited.add(node)

        print(f"Node : {node}  Cost : {cost}")

        if node == goal:

            print("Goal Found")

            return

        for neighbor in graph[node]:

            heapq.heappush(
                pq,
                (cost + 1, neighbor)
            )


# ==========================================================
# GREEDY SEARCH
# ==========================================================

def greedy_search(start, goal):

    print("\n========== GREEDY SEARCH ==========")

    pq = []

    heapq.heappush(
        pq,
        (heuristic[start], start)
    )

    visited = set()

    while pq:

        h, node = heapq.heappop(pq)

        print(
            f"Selected : {node} "
            f"Heuristic = {h}"
        )

        if node == goal:

            print("Goal Reached")

            return

        visited.add(node)

        for neighbor in graph[node]:

            if neighbor not in visited:

                heapq.heappush(
                    pq,
                    (heuristic[neighbor], neighbor)
                )


# ==========================================================
# A* SEARCH
# ==========================================================

def a_star(start, goal):

    print("\n========== A* SEARCH ==========")

    open_set = []

    heapq.heappush(open_set, (0, start))

    g_cost = {

        start: 0
    }

    closed_set = set()

    while open_set:

        current_f, current_node = heapq.heappop(open_set)

        if current_node in closed_set:
            continue

        print(
            f"Evaluating : {current_node}"
        )

        if current_node == goal:

            print("Goal Found")

            return

        closed_set.add(current_node)

        for neighbor in graph[current_node]:

            temp_g = g_cost[current_node] + 1

            f_value = temp_g + heuristic[neighbor]

            if neighbor not in g_cost or temp_g < g_cost[neighbor]:

                g_cost[neighbor] = temp_g

                heapq.heappush(
                    open_set,
                    (f_value, neighbor)
                )

                print(
                    f"Added {neighbor} "
                    f"with f(n) = {f_value}"
                )


# ==========================================================
# EMPIRICAL PROFILING
# ==========================================================

start_time = time.time()

bfs("Laptop A")

print("\n========== DFS SEARCH ==========")

dfs("Laptop A", set())

ucs("Laptop A", "Laptop G")

greedy_search("Laptop A", "Laptop G")

a_star("Laptop A", "Laptop G")

end_time = time.time()

print("\n========== PERFORMANCE ==========")

print(
    "Execution Time :",
    end_time - start_time,
    "seconds"
)
