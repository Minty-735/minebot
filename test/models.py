import math

import numpy as np


class Cell:
    def __init__(self, id, number):
        self.id = int(id)
        self.number = int(number)
        self.neighbours = []

    def __str__(self):
        return ("id - " + str(self.id)
                + " number - " + str(self.number))

    def __hash__(self):
        return super().__hash__()

    def update(self, number):
        self.number = number

    def addNeighbour(self, cell):
        self.neighbours.append(cell)

    def addNeighbours(self, cells):
        for cell in cells:
            self.neighbours.append(cell)
    def getNeighbours(self) -> list[...]:
        return self.neighbours

    def removeNeighbours(self,neighbour):
        self.neighbours.remove(neighbour)
    def getUnOpenedNeighbours(self):
        return [i for i in self.neighbours if i.number == 9]





class Group:
    def __init__(self):
        self.mines = 0
        self.cells = set()  # id

    def __hash__(self):
        return super().__hash__()

    def addCell(self, cell):
        self.cells.add(cell)

    def addCells(self, cells):
        for cell in cells:
            self.cells.add(cell)

    def removeContaining(self, other):
        self.mines -= other.mines
        for i in other.cells:
            self.cells.remove(i)

    def isOverlapping(self, other) -> bool:
        return True if len(self.cells.intersection(other.cells)) else False

    def getOverlap(self, other):
        return self.cells.intersection(other.cells)

    def size(self):
        return len(self.cells)
    def __str__(self):
        a = [str(i) for i in self.cells]
        return f"{a} --- {self.mines}"

    def haveInside(self, child):
        a = (self.cells).copy()
        b = (child.cells).copy()

        c = True
        for i in b:
            try:
                a.remove(i)
            except:
                c = False
        # print()
        return c












class Board:
    def __init__(self, size):
        self.size = size
        self.data = [None] * size

    def addcell(self, cell:Cell):
        self.data[cell.id] = cell

    def endBuild(self):
        arr = np.array([i for i in self.data])
        a =int(math.sqrt(self.size))
        self.arr2d = arr.reshape(a,a)
        self.friends = self._neighbors(self.arr2d)

        for i, j in enumerate(self.friends, 0):
            self.getCellById(i).addNeighbours(j)

    def getCellById(self, cellId) -> Cell:
        return self.data[cellId]

    def __str__(self):
        # print(self.arr2d[0][1]) - первый ряд 2 столбик
        a = self.arr2d
        b = [[j.number for j in i] for i in a]
        # print([[j.id for j in i] for i in self.friends])
        answer = ""
        for i in b:
            for j in i:
                answer+= f" {j}"
            answer += "\n"


        return answer

    def __hash__(self):
        return super().__hash__()

    def getActiveCells(self) -> list[Cell]:
        return [i for i in self.data if i.number in range(1, 8)]

    def _neighbors(self, x):
        def in_bounds(i, j, x):
            return 0 <= i < len(x) and 0 <= j < len(x[0])

        return [[x[i + di][j + dj] for di in (-1, 0, 1)
                 for dj in (-1, 0, 1)
                 if in_bounds(i + di, j + dj, x) and (di != 0 or dj != 0)]
                for i in range(len(x))
                for j in range(len(x[0]))]

    def get100mines(self):
        popa = []
        for i in self.getActiveCells():
            if i.number == len(i.getUnOpenedNeighbours()):
                for j in i.getUnOpenedNeighbours():
                    popa.append(j)
        return list(set(popa))

    def createGroup(self) -> list[Group]:
        groups = []
        for i in self.getActiveCells():
            group = Group()
            group.addCells(i.getUnOpenedNeighbours())
            group.mines = i.number
            groups.append(group)
        repeat = True
        while repeat:
            repeat = False


            groupsCopy = groups.copy()
            # print(*groupsCopy)

            for _ in "12345":
                try:
                    for i in range(len(groupsCopy)-1):
                        for j in range(i+1,len(groupsCopy)-1):

                            if groupsCopy[i].cells == groupsCopy[j].cells and  groupsCopy[i].mines == groupsCopy[j].mines:
                                    groupsCopy.remove(groupsCopy[i])
                except Exception as e:
                    print("remove error")
                    print(e)
            print(*groupsCopy)



            for i in groupsCopy:
                # print(groupsCopy)
                groupsCopy.remove(i)
                for j in groupsCopy:

                    # print(*groupsCopy)
                    groupI = i
                    groupJ = j

                    parent, child = (groupI, groupJ) if groupI.size() > groupJ.size() else (groupJ, groupI)
                    if parent.haveInside(child):
                        parent.removeContaining(child)

                        # print(f"{parent.cells} - {child.cells}")
                        repeat = True
                    # elif parent.isOverlapping(child):
                    #     if parent.cells == child.cells:
                    #         continue
                    #     if parent.mines == child.mines:
                    #         continue
                    #
                    #
                    #     if parent.mines < child.mines: parent, child = child, parent
                    #
                    #     group = Group()
                    #     group.addCells(parent.getOverlap(child))
                    #     group.mines = parent.mines - child.mines
                    #     groups.append(group)
                    #     parent.removeContaining(group)
                    #     child.removeContaining(group)
                    #     print("parent.isOverlapping(child)")
                    #     repeat = True

        return groupsCopy


    def calculate(self):
        a = self.createGroup()
        allTrue = []
        allFalse = []
        for i in a:
            if len(i.cells) == i.mines:
                for j in i.cells:
                    print(f"100% - {str(j.id)}")
                    allTrue.append(j.id)
            elif i.mines == 0:
                for j in i.cells:
                    print(f"0% - {str(j.id)}")
                    allFalse.append(j.id)

        return list(set(allTrue)),list(set(allFalse))



    def updateinfo(self):
        for i in self.data:
            # i:Cell
            for neighbour in i.getNeighbours():
                # neighbour:Cell
                if neighbour.number == -1:
                    i.removeNeighbours(neighbour)
                    i.update(i.number-1)





