import numpy
import numpy as np


class Cell:
    def __init__(self, id, number):
        self.id = int(id)
        self.number = int(number)
        self.neighbours = []
        self.group = None

    def __str__(self):
        return ("id is " + str(self.id)
                + " number is " + str(self.number))

    def update(self, number):
        self.number = number

    def __contains__(self, item):
        a: set = self.group.cells
        return a.__contains__(item.group.cells)

    def addNeighbour(self, cell):
        self.neighbours.append(cell)

    def addNeighbours(self, cells):
        for cell in cells:
            self.neighbours.append(cell)

    def set_group(self, groups):
        if self.group is None:
            new_group = Group()
            new_group.add_cells(self.neighbours)
            new_group.mines = self.number
            groups.append(new_group)
            self.group = new_group


class Board:
    def __init__(self, size):
        self.size = size
        self.data = [None] * size
        self.dictionary = {}

    def addcell(self, cell):
        self.data[cell.id] = cell

    def endBuild(self):

        arr = np.array([i for i in self.data])
        self.arr2d = arr.reshape(9, 9)

        self.friends = self._neighbors(self.arr2d)

        for i, j in enumerate(self.friends, 0):
            self.getCellById(i).addNeighbours(j)

        print(self.friends)

    def getCellById(self, cellId) -> Cell:
        return self.data[cellId]

    def __str__(self):
        # print(self.arr2d[0][1]) - первый ряд 2 столбик
        a = self.arr2d
        b = [[j.number for j in i] for i in a]

        return str(b)

    def getActiveCells(self):
        return [i for i in self.data if i.number in range(1, 8)]

    def _neighbors(self, x):
        def in_bounds(i, j, x):
            return 0 <= i < len(x) and 0 <= j < len(x[0])

        return [[x[i + di][j + dj] for di in (-1, 0, 1)
                 for dj in (-1, 0, 1)
                 if in_bounds(i + di, j + dj, x) and (di != 0 or dj != 0)]
                for i in range(len(x))
                for j in range(len(x[0]))]

    def _f(self,l):
        n = []
        for i in l:
            if i not in n:
                n.append(i)
        return n

    def calculate(self):
        groups = []
        a = self.getActiveCells()
        for i in a:
            i.set_group(groups)
        repeat = True

        while repeat:
            repeat = False
            groups = self._f(groups)
            for i in range(len(groups) - 1):
                groupI = groups[i]
                for j in range(i + 1, len(groups) - 2):
                    groupJ = groups[j]

                    parent, child = (groupI, groupJ) if groupI.size() > groupJ.size() else (groupJ, groupI)
                    if parent.contains(child):
                        parent.subtraction(child)
                        repeat = True
                    elif parent.overlaps(child):
                        if parent.get_mines() > child.get_mines():
                            parent, child = groupI, groupJ
                        else:
                            parent, child = groupJ, groupI
                        overlap = parent.get_overlap(child)
                        if overlap:
                            groups.append(overlap)
                            parent.subtraction(overlap)
                            child.subtraction(overlap)
                            repeat = True
        return groups


'''
                        if parent.get_mines() > child.get_mines():
                            parent, child = groupI, groupJ
                        else:
                            parent, child = groupJ, groupI
                        overlap = parent.get_overlap(child)
                        if overlap:
                            groups.append(overlap)
                            parent.subtraction(overlap)
                            child.subtraction(overlap)
                            repeat = True

        return groups

'''


class Group:
    def __init__(self):
        self.cells = set()
        self.mines = 0

    def __eq__(self, other):

        return self.cells == other.cells

    def __str__(self):
        str = [i.id for i in self.cells]
        return f"{str} --- {self.mines}"

    def add_cell(self, cell):
        self.cells.add(cell)

    def add_cells(self, cells):
        for cell in cells:
            self.cells.add(cell)

    def remove_cell(self, cell):
        self.cells.remove(cell)

    def size(self):
        return len(self.cells)

    def contains(self, other):
        a = self.cells.__contains__(other.cells)

        return a

    def overlaps(self, other):
        return len(self.cells.intersection(other.cells))

    def get_overlap(self, other):
        overlap = Group()
        for cell in self.cells.intersection(other.cells):
            overlap.add_cell(cell)
        overlap.mines = self.get_mines() - other.get_mines()
        return overlap if overlap.size() > 0 else None

    def subtraction(self, other):
        self.mines -= other.get_mines()
        for cell in other.cells:
            self.remove_cell(cell)

    def get_mines(self):
        return self.mines


'''
 groups = []
        for i in self.data:
            if i.number in range(1, 9):
                i.set_group(groups)

        repeat = True
        while repeat:
            repeat = False
            for i in range(len(groups) - 1):
                if i >= len(groups) - 1:
                    continue
                groupI = groups[i]
                for j in range(i + 1, len(groups) - 2):
                    groupJ = groups[j]
                    if groupI == groupJ:
                        groups.pop(j)
                        break
            for i in range(len(groups) - 1):

                groupI = groups[i]
                for j in range(i + 1, len(groups) - 2):
                    groupJ = groups[j]
                    parent, child = (groupI, groupJ) if groupI.size() > groupJ.size() else (groupJ, groupI)

                    if parent.contains(child):
                        parent.subtraction(child)
                        repeat = True
                    elif parent.overlaps(child) > 0:
                        if parent.get_mines() > child.get_mines():
                            parent, child = groupI, groupJ
                        else:
                            parent, child = groupJ, groupI
                        overlap = parent.get_overlap(child)
                        if overlap:
                            groups.append(overlap)
                            parent.subtraction(overlap)
                            child.subtraction(overlap)
                            repeat = True

        return groups

'''
