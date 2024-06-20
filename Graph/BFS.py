from collections import deque
def bfs(adjList, startpoint, visited):
    q= deque()
    visited[startpoint]= True
    q.append(startpoint)

    while q:
        currentpoint= q.popleft()
        print(currentpoint, end= " ")

        for neighbour in adjList[currentpoint]:
            if not visited[neighbour]:
                visited[neighbour]= True
                q.append(neighbour)

def addEdge(adjList, u, v):
    adjList[u].append(v)

def main():
    vertices= 5

    adjList=[[] for _ in range(vertices)]

    addEdge(adjList, 0, 1)
    addEdge(adjList, 0, 2)
    addEdge(adjList, 1, 3)
    addEdge(adjList, 1, 4)
    addEdge(adjList, 2, 4)

    visited= [False] * vertices

    print("The BFS of the Graph for vertex 3:-", end= " ")
    bfs(adjList, 0, visited)

if __name__=="__main__":
    main()
