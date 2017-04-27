import numpy as np
import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches
from matplotlib.artist import setp

def plot_grid(n, figsize=(3,3)):
    fig = plt.figure(figsize=figsize)
    ax = fig.add_subplot(111)
    for i in range(n + 1):
        ax.plot((0, n), (i, i), color='black')
        ax.plot((i, i), (0, n), color='black')
    ax.set_aspect('equal', 'datalim')
    ax.axis('off')
    return ax

def plot_square(bottom_left, size, ax, color='black'):
    x = bottom_left[0]
    y = bottom_left[1]
    lines = ax.plot((x,x+size,x+size,x,x), (y,y,y+size,y+size,y), color=color)
    setp(lines, linewidth=5)

def plot_filled_square(bottom_left, ax):
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
    ax.add_patch(patch)
