class Tree:
    def __init__(self, x):
        self.rt = x
        self.child = []
 
    def add_child(self, a):
        self.child.append(a)

    def root(self):
        return self.rt

    def ith_child(self, i):
        return self.child[i]

    def num_children(self):
        return len(self.child)
        

class Pre(Tree):
    def preorder(self):
        if self.num_children() == 0:
            return [self.rt]
        if self.num_children() == 1:
            return [self.rt] + self.ith_child(0).preorder()
        return  [self.rt] + self.ith_child(0).preorder() + self.ith_child(1).preorder()