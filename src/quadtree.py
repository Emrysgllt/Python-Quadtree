from __future__ import annotations
class QuadTree:
    NB_NODES : int = 4
    def __init__(self, hg: bool | QuadTree, hd: bool | QuadTree, bd: bool | QuadTree,bg: bool | QuadTree):
        self.hg = hg
        self.hd = hd
        self.bd = bd
        self.bg = bg

    @property
    def depth(self) -> int:
        """Recursion depth of the quadtree"""
        return 1 + max(

            child.depth if isinstance(child, QuadTree) else 0
            for child in [self.hg, self.hd, self.bd, self.bg]

        )

    @staticmethod
    def fromFile(filename: str) -> QuadTree:
        """ Open a given file, containing a textual representation of a list"""
        with open(filename, 'r') as f:
            data_list = f.read().strip().strip('[]')
            data = list(map(int, data_list.split(',')))
            return QuadTree(*data)

    @staticmethod
    def fromList(data: list) -> QuadTree:
        if len(data) != QuadTree.NB_NODES:
            raise ValueError("Erreur problème de récupération de données")
        return QuadTree(data[0], data[1], data[2], data[3])

class TkQuadTree(QuadTree):
    pass