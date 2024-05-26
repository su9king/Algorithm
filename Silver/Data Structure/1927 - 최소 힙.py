import sys
count = int(sys.stdin.readline())
stack = []
nodes = {}

class Node():

    def __init__(self,number,index):

        self.number = number
        self.parent = None
        self.child = []
        self.index = index

    def addParent(self,parent):

        self.parent = parent

    def addChild(self,child):

        self.child.append(child)

    def removeNode(self,number):

        for i in self.child:
            nodes[i][0].parent = number

        nodes[number][0].parent = None
        nodes[number][0].index = 0

def changeNode(highNode,lowNode):
    nodes[highNode][0].parent, nodes[lowNode][0].parent = lowNode, nodes[highNode][0].parent
    nodes[highNode][0].child, nodes[lowNode][0].child = nodes[lowNode][0].child, nodes[highNode][0].child
    nodes[highNode][0].index, nodes[lowNode][0].index = nodes[lowNode][0].index, nodes[highNode][0].index
    stack[nodes[highNode][0].index], stack[nodes[lowNode][0].index] = stack[nodes[lowNode][0].index], stack[
        nodes[highNode][0].index]

    for i in nodes[highNode][0].child:
        nodes[i][0].parent = highNode


def addCheckRelationship(highNode,lowNode):

    print("현재 스택 : ",stack , highNode,lowNode)

    if highNode == None: #지금 lowNode 는 RootNode 임. 고로 다 도달했다는 뜻
        return
    elif highNode > lowNode: #자식 노드가 더 숫자가 작다면 바꿔야 함.

        changeNode(highNode,lowNode)


        addCheckRelationship(nodes[lowNode][0].parent, lowNode)
    else:
        return
def removeCheckRelationship(highNode,lowNode):

    print("현재 스택 : ",stack , highNode,lowNode)

    if highNode == None: #지금 lowNode 는 RootNode 임. 고로 다 도달했다는 뜻
        return
    elif highNode > lowNode: #자식 노드가 더 숫자가 작다면 바꿔야 함.

        changeNode(highNode,lowNode)


        removeCheckRelationship(nodes[highNode][0].child[0], highNode)
    else:
        return


for i in range(count):

    number = int(input())

    if number == 0:

        if len(stack) == 0:
            print(0)
        else:
            minvalue = stack[0]
            print(minvalue)

            if len(stack) >= 3: #여기까지 완성함 일단.:
                stack[0] = stack.pop()
                nodes[minvalue][0].removeNode(stack[0])
                removeCheckRelationship(stack[0],stack[1])
            else:
                del(stack[0])

            del(nodes[minvalue][0])

    elif len(stack) == 0:

        nodes[number] = [Node(number,0)]
        stack.append(number)

    else:
        index = int(len(stack)/2) # 현재 자식노드를 채워야 하는 노드의 Stack 인덱스
        new_node = Node(number, len(stack))

        if number in nodes:
            nodes[number].append(new_node)  # 기존 키에 추가
        else:
            nodes[number] = [new_node]  # 새로운 키 생성


        stack.append(number)
        new_node.addParent(stack[index])
        nodes[stack[index]][-1].addChild(number)


        addCheckRelationship(stack[index],number)















