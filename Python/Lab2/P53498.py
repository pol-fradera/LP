import queue
class Tree:
    def __init__(self, x):
        self.rt = x
        self.child = []
 
    def __iter__(self):
        q = queue.Queue()
        t = self
        yield t.rt
        q.put(t)
        while not q.empty():
            t = q.get()
            if t.numChildren() > 0:
                tl = t.ithChild(0)
                q.put(tl)
                yield tl.rt
            if t.numChildren() == 2:
                tr = t.ithChild(1)
                q.put(tr)
                yield tr.rt


    def addChild(self, a):
        self.child.append(a)

    def root(self):
        return self.rt

    def ithChild(self, i):
        return self.child[i]

    def numChildren(self):
        return len(self.child)