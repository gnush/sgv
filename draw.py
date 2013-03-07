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
if len(l) > 1:
    try:
        width = int(l[0])
        height = int(l[1])
        scale = int(l[2])
    except ValueError:
        exit(2)
    except IndexError:
        scale = 1
else:
    exit(2)

for line in f:
    l = line.split()

    if len(l) == 0:
        continue

    if l[0] == "Node":
        try:
            x = int(l[1])
            y = int(l[2])
#            b = str_to_bool(l[3])
        except (ValueError, IndexError):
            print("Cannot parse node")

        weight = 1
        b = False
        if len(l) > 4:
            weight = l[3]
            b = str_to_bool(l[4])
        elif len(l) > 3:
            try:
                weight = int(l[3])
            except ValueError:
                b = str_to_bool(l[3])

        nodes.append(Node(x, y, weight, b, scale))
    elif l[0] == "Edge":
        try:
            i = int(l[1])
            j = int(l[2])
        except (ValueError, IndexError):
            print("Cannot parse edge")

        weight = 1
        b = False
        if len(l) > 4:
            weight = int(float(l[3]))
            b = str_to_bool(l[4])
        elif len(l) > 3:
            try:
                weight = int(float(l[3]))
            except ValueError:
                b = str_to_bool(l[3])

        edges.append(Edge(nodes[i], nodes[j], weight, visited=b))
    elif l[0] == "Obstacle":
        if len(l) < 7 | len(l) % 2 != 0:
            print("Cannot parse obstacle")
            continue

        obstacles.append(Obstacle(l[1:], scale))


root = Tk()

w = Canvas(root, width=width*scale, height=height*scale)
w.pack()

for e in edges:
    e.draw(w)

for n in nodes:
    n.draw(w)

for o in obstacles:
    o.draw(w)

root.mainloop()
