import sys, os
sys.path.append(os.path.realpath(os.path.dirname(__file__)+"/.."))

from src import QuadTree, TkQuadTree

"""
def test_sample():
    filename = 'file/quadtree.txt'
    q = QuadTree.fromFile(filename)
    assert q.depth == 4
"""

def test_single():
    filename = 'file/quadtree_easy.txt'
    q = QuadTree.fromFile(filename)
    assert q.depth == 1
