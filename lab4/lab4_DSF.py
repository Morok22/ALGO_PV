import json
import runpy as np

graphStr = ""
graph = []
i = 0;

f = open("data.txt", "r")
for line in f:
    if i == 0:
        graphStr = line
        i += 1;
    if i == 1:
        touch = line.split("->")

f = touch[0]
t = touch[1]

graph = json.loads(graphStr)


# візит до кожної точки графу використовючи DSF
def dfs(graph, start):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(np.array(graph[vertex]) - np.array(visited))
    return visited

dfs(graph, '1')

def dfs_paths(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                stack.append((next, path + [next]))

result = list(dfs_paths(graph, '1', '6'))


for element in result:
    print(element)