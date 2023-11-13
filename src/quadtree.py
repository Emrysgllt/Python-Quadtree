"""
@author Emrys GUILLOTEAU
"""

from __future__ import annotations
class QuadTree:
    NB_NODES: int = 4
    def __init__(self, hg: bool | QuadTree, hd: bool | QuadTree, bd: bool | QuadTree, bg: bool | QuadTree):
        self.hg = hg
        self.hd = hd
        self.bd = bd
        self.bg = bg

    @property
    def depth(self) -> int:
        """Recursion depth of the quadtree
        La profondeur de récursion est définie comme la profondeur maximale
        parmi les quadrants enfants (hg, hd, bd, bg).

        Retourne:
        --------
        int: La profondeur de récursion de l'arbre quadtree
        """
        return 1 + max(

            child.depth if isinstance(child, QuadTree) else 0
            for child in [self.hg, self.hd, self.bd, self.bg]

        )

    @staticmethod
    def fromFile(filename: str) -> QuadTree:

        """ Open a given file, containing a textual representation of a list
        Crée un arbre quadtree correspondant.
        :arguments:
            filename (str): Le nom du fichier à ouvrir.
            --------
        Returns:
            QuadTree: Un objet QuadTree créé à partir des données du fichier.
            --------
        """
        with open(filename, 'r') as f:
            data_list = f.read().strip().strip('[]')
            data = list(map(int, data_list.split(',')))
            return QuadTree(*data)

    @staticmethod
    def fromList(data: list) -> QuadTree:
        """Generates a Quadtree from a list representation
         :arguments:
            data (list): Une liste représentant les données nécessaires pour créer un QuadTree.
            -----------
        Returns:
            QuadTree: Un objet QuadTree créé à partir de la liste fournie.
            --------
        Raises:
            ValueError: Si la longueur de la liste 'data' n'est pas égale à QuadTree.NB_NODES.
            ----------
            Cela indique une erreur dans les données.

        """
        if len(data) != QuadTree.NB_NODES:
            raise ValueError("Erreur des données")
        return QuadTree(*data)

class TkQuadTree(QuadTree):
    pass