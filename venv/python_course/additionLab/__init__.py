from Tree import BinaryTree

if __name__ == '__main__':
    t = BinaryTree(25)
    t.insert(10)
    t.insert(10)
    t.insert(14)
    t.insert(11)
    t.insert(5)
    t.insert(7)
    t.insert(5)
    t.insert(-6)
    t.insert(-5)
    t.insert(3)
    t.insert(15)
    t.insert(8)
    t.insert(-79)
    t.insert(2)
    t.root.display()
    t.levelorder()
    print(t.countP)

