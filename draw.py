#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from tkinter import *
from Node import *
from Edge import *
from Obstacle import *

if len(sys.argv) < 2:
    exit(1)

def str_to_bool(s):
    return s in ["true", "True", "1", "y", "Y", "yes", "Yes"]

nodes = []
edges = []
obstacles = []

f = open(sys.argv[1])

l = f.readline().split()
try:
    width = int(l[0])
    height = int(l[1])
except (ValueError, IndexError):
    exit(2)

for line in f:
    l = line.split()

    if len(l) == 0:
        continue

    if l[0] == "Node":
        try:
            x = int(l[1])
            y = int(l[2])
            b = str_to_bool(l[3])
        except ValueError:
            print("Cannot parse node")
            continue
        except IndexError:
            b = False

        nodes.append(Node(x, y, b))
    elif l[0] == "Edge":
        try:
            i = int(l[1])
            j = int(l[2])
            b = str_to_bool(l[3])
        except ValueError:
            print("Cannot parse edge")
            continue
        except IndexError:
            b = False

        edges.append(Edge(nodes[i], nodes[j], b))
    elif l[0] == "Obstacle":
        if len(l) < 7 | len(l) % 2 != 0:
            print("Cannot parse obstacle")
            continue

        obstacles.append(Obstacle(l[1:]))


root = Tk()

w = Canvas(root, width=width, height=height)
w.pack()

for e in edges:
    e.draw(w)

for n in nodes:
    n.draw(w)

for o in obstacles:
    o.draw(w)

root.mainloop()
