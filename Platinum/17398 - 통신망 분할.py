import sys

input = sys.stdin.readline

def find(node):

    if node.parent_node == node.number:

        return node.number
    else:
        return node.set( find( graph[node.parent_node] ) )


class node:
    global expense
    def __init__(self,number):
        self.number = number
        self.parent_node = number
        self.size = 1

    def union(self,number):

        global expense

        if a == b:
            pass

        else:
            expense += self.size * graph[number].size
            graph[number].parent_node = self.number
            self.size += graph[number].size

    def set(self,number):

        self.parent_node = number

        return number



N , M , Q = map(int,input().split())

graph = ["D"]
q = ["D"]
q_disconnect = []
sum = 0
expense = 0
for i in range(1,N+1):
    graph.append(node(i))

for i in range(0,M):
    a, b = map(int, input().split())
    q.append([a,b])

for i in range(0,Q):
    index = int( input() )
    q_disconnect.append( q[index] )
    q[index] = "D"



# Main
for i in q:
    if i[0] != "D":

        a,b = find(graph[i[0]]),find(graph[i[1]])
        if a != b:
            graph[a].union(b)

expense = 0
for i in range(0,Q):
    a,b = q_disconnect.pop()
    a,b = find(graph[a]),find(graph[b])
    if a != b:
        graph[a].union(b)

print(expense)
