import numpy as np
import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches
from matplotlib.artist import setp

class Fig:
    def __init__(self, figsize=(3,3)):
        fig = plt.figure(figsize=figsize)
        self.ax = fig.add_subplot(111)
        self.ax.set_aspect('equal', 'datalim')

    def grid(self, n, figsize=(3,3), edges=False):
        for i in range(1, n):
            self.ax.plot((0, n), (i, i), color='black')
            self.ax.plot((i, i), (0, n), color='black')
        if edges:
            self.ax.plot((0, n), (0, 0), color='black')
            self.ax.plot((0, n), (n, n), color='black')
            self.ax.plot((0, 0), (0, n), color='black')
            self.ax.plot((n, n), (0, n), color='black')
        self.ax.axis('off')

    def sq(self, bottom_left, size, color='black'):
        x = bottom_left[0]
        y = bottom_left[1]
        lines = self.ax.plot((x,x+size,x+size,x,x), (y,y,y+size,y+size,y), color=color)
        setp(lines, linewidth=5)

    def fillsq(self, bottom_left):
        x = bottom_left[0]
        y = bottom_left[1]
        verts = [
            (x, y), # left, bottom
            (x, y+1), # left, top
            (x+1, y+1), # right, top
            (x+1, y), # right, bottom
            (x, y), # ignored
            ]
        codes = [Path.MOVETO,
                 Path.LINETO,
                 Path.LINETO,
                 Path.LINETO,
                 Path.CLOSEPOLY,
                 ]

        path = Path(verts, codes)
        patch = patches.PathPatch(path, facecolor='black')
        self.ax.add_patch(patch)

    def x(self, bottom_left):
        x = bottom_left[0]
        y = bottom_left[1]
        self.ax.plot((x+0.2, x+0.8), (y+0.2, y+0.8), color='black')
        self.ax.plot((x+0.2, x+0.8), (y+0.8, y+0.2), color='black')

    def o(self, bottom_left):
        x = bottom_left[0]
        y = bottom_left[1]
        circ = plt.Circle((x+0.5, y+0.5), 0.375, color='black', fill=False)
        self.ax.add_artist(circ)
