# -*- coding:utf-8 -*-
from .combinatorics import (
    xunique_combinations
)
from .compat import xrange


class Node(object):
    def __init__(self, id):
        self.id = id
        self.counter = 0
        self.in_ = set()
        self.out = set()

    def __str__(self):
        return str(self.__dict__)


def hashlize(items):
    return "->".join([x.id for x in items])


class PairsStorage(object):
    def __init__(self, n):
        self.n = n
        self.nodes = {}
        self.combs_arr = []
        for i in xrange(n):
            self.combs_arr.append(set())

    def add(self, comb):
        n = len(comb)
        assert(n > 0)

        self.combs_arr[n - 1].add(hashlize(comb))
        if n == 1 and comb[0].id not in self.nodes:
            self.nodes[comb[0].id] = Node(comb[0].id)
            return

        ids = [x.id for x in comb]
        for i, id in enumerate(ids):
            curr = self.nodes[id]
            curr.counter += 1
            curr.in_.update(ids[:i])
            curr.out.update(ids[i + 1:])

    def add_sequence(self, seq):
        for i in xrange(1, self.n + 1):
            for comb in xunique_combinations(seq, i):
                self.add(comb)

    def get_node_info(self, item):
        return self.nodes.get(item.id, Node(item.id))

    def get_combs(self):
        return self.combs_arr

    def __len__(self):
        return len(self.combs_arr[-1])

    def count_new_combs(self, seq):
        s = set([hashlize(z) for z in xunique_combinations(seq, self.n)]) - self.combs_arr[-1]
        return len(s)
