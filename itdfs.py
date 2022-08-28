graph = { 
    'A':['B','C'],
    'B':['A','D'],
    'C':['A','D'],
    'D':['C','B']
    }

def dls(graph,src,goal,depth):

    visited= set()
    if src not in graph:
        print("Node is Not found ;)")
        return
    d = 0
    stack = []
    stack.append(src)
    path = []
    while stack:
        current = stack.pop()
        path.append(current)
        if current == goal:
            return path
        if current not in visited:
            print(current,end=" ")
            visited.add(current)
            for i in graph[current]:
                if d<depth:
                    stack.append(i)
                    d += 1
    return 0
                

def iddfs(graph,src, target, maxDepth):
     for i in range(maxDepth): 
        print(dls(graph,src,target,i))
            
print(iddfs(graph,'A','C',2))
