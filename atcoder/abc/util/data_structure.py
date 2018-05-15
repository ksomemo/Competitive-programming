class Queue:
    pass


class Stack:
    pass


class Tree:
    pass


class TreeNode():
    pass


class BalanceTree:
    pass


class AvlTree:
    pass


class RedBlackTree:
    pass


class UnionFind:
    def __init__(self, par):
        self.par = par

    def root(self, x):
        if self.par[x] == x:
            return x
        # 経路圧縮
        self.par[x] = self.root(self.par[x])
        return self.par[x]

    def same(self, x, y):
        return self.root(x) == self.root(y)

    def unite(self, x, y):
        x = self.root(x)
        y = self.root(y)

        if x != y:
            self.par[y] = x


class HashTable:
    pass


class OpenHashTable:
    pass


class ClosedHashTable:
    pass
