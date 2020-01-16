from queue import Queue
from random import seed
from random import randint
from collections import deque


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None

    def set_left_node(self, node):
        self.left = node

    def set_right_node(self, node):
        self.right = node

    def set_data(self, key):
        self.key = key


class BinaryTree:

    def __init__(self, value):
        self.root = None
        self.value = value
        self.countP = 0

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
            return

        q = []
        q.append(self.root)

        while (len(q)):
            node = q[0]
            q.pop(0)

            if node.left is None:
                node.left = Node(key)
                break
            else:
                q.append(node.left)

            if node.right is None:
                node.right = Node(key)
                break
            else:
                q.append(node.right)

    def levelorder(self):
        q = Queue()
        q.put(self.root)
        while not q.empty():
            node = q.get()
            sum = 0
            self.iterativePreorder(node, sum)
            if not (node.left is None):
                q.put(node.left)
            if not (node.right is None):
                q.put(node.right)

    def iterativePreorder(self, rootNode, summ):
        if rootNode is None:
            return
        s = [rootNode]
        preNodes = []
        sumLine = 0
        countPop = 0
        while len(s) > 0:
            node = s.pop()
            if not (node.right is None) or not (node.left is None):
                if not (node in preNodes):
                    preNodes.append(node)
                else:
                    preNodes.remove(node)
            elif node.right is None and node.left is None:
                preNodes.append(node)
                if self.height(self.root) < len(preNodes):
                    preNodes.pop(len(preNodes) - self.height(self.root))
                if len(preNodes) < 2:
                    if countPop == 2:
                        countPop = 0
                        sumLine = 0
                        preNodes.clear()
                        preNodes.append(rootNode)
                    continue
                sumLine += sum(preNode.key for preNode in preNodes)
                print([preNode.key for preNode in preNodes], end="")
                print()
                preCountElements = len(preNodes)
                print(preCountElements)
                preNodes.pop()
                countPop += 1
                if countPop == 2:
                    countPop = 0
                    preNodes.pop()
                self.checkNumber(sumLine)
                sumLine = 0
            if not (node.right is None):
                s.append(node.right)
            if not (node.left is None):
                s.append(node.left)

    def checkNumber(self, sum):
        if self.value == sum:
            self.countP += 1

    def print_tree(self):
        current_level = [self.root]
        for_print = []
        while current_level:
            for_print.append(' '.join(str(node.key) for node in current_level))
            next_level = list()
            for n in current_level:
                if n.left:
                    next_level.append(n.left)
                if n.right:
                    next_level.append(n.right)
            current_level = next_level
        countSpace = (len(for_print[len(for_print) - 1]) // 2) - 1
        for index, i in enumerate(for_print):
            print((" " * countSpace) + i)
            countSpace //= 2
        print("-------------------------------------------")

    def height(self, node):
        if node == None:
            return 0
        else:
            lheight = self.height(node.left)
            rheight = self.height(node.right)

            if lheight > rheight:
                return (lheight + 1)
            else:
                return (rheight + 1)
