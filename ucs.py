import queue as Q

graph = {'a': {'b': 2, 'e': 3},
         'b': {'d': 1, 'a': 2},
         'e': {'a': 3, 'd': 4},
         'd': {'e': 4, 'b': 1}
        }

def search(graph, start, end):
    queue = Q.PriorityQueue()
    print("OL",queue.queue)
    queue.put((0, [start]))
    closed = " "
    i = 0

    while not queue.empty():

        node = queue.get()
        print(node)
        c = node[1][len(node[1]) - 1]
        closed += c
        print(closed)
        

        if end in node[1]:
            print("Path:" + str(node[1]) + ", Cost = " + str(node[0]))
            break
        else:
            print("GT Fails")

        cost = node[0]
        print("Sucess:",graph[c])
        for n in graph[c]:
            temp = node[1][:]
            temp.append(n)
            queue.put((cost + graph[c][n], temp))
            i += 1
            print("OL:",queue.queue)
            
(search(graph, 'a', 'd'))

