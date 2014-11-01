# -*- coding:utf-8 -*-

#===============================================================================
# code from http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/190465
# all (c) etc. are of the authors of this procedures, see link above
#===============================================================================

from .compat import xrange


def xunique_combinations(items, n):
    if n == 0:
        yield ()
    else:
        for i in xrange(len(items)):
            for cc in xunique_combinations(items[i + 1:], n - 1):
                yield (items[i], ) + cc
