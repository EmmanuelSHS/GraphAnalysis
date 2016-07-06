#!/usr/bin/env python
# coding=utf-8

import sys
import datetime

class Node:
    def __init__(self, n, t):
        self.__dependents = {}
        self.__ndependents = 0
        self.__timestamp = t
        self.__name = n

    def __str__(self):
        return self.__name

    def addDependent(self, other):
        # TODO: if other is already in, what happens to degree?
        if str(other) not in self.__dependents:
            self.__dependents[str(other)] = other
            self.__ndependents += 1

    def delDependent(self, other):
        if str(other) in self.__dependents:
            del self.__dependents[str(other)]
            self.__ndependents -= 1

    def getNDependents(self):
        return self.__ndependents

    def getDependents(self):
        return self.__dependents

    def getTimestamp(self):
        return self.__timestamp

    def getName(self):
        return self.__name


class Window:
    # TODO: current implementation does not consider graph
    def __init__(self):
        self.__tPath = {}
        self.__maxT = datetime.strptime("1000-01-01 00:01:01", "%Y-%m-%d %H:%M:%S")
        self.__maxT = datetime.strptime("1000-01-01 00:00:01", "%Y-%m-%d %H:%M:%S")

    def setMaxTimestamp(self, t):
        self.__maxT = self.__maxT if self.__maxT > t else t
        self.__minT = self.__maxT - datetime.timedelta(minutes = 1)

    def insertNewNode(self, node):
        newT = node.getTimestamp()
        if self.__minT <= newT:
            self.__tPath[newT] = node
            self.addDependents(node)
            self.setMaxTimestamp(newT)

    def addDependents(self, node):
        for _, d in node.getDependents():
            d.addDependent(node)

    def updateWindow(self):
        for t, nodes in self.__tPath:
            if t < self.__minT:
                for n in nodes:
                    self.delDependents(n)
                del self.__tPath[t]

    def delDependents(self, node):
        for _, d in node.getDependents():
            d.delDependent(node)

    def getMedianDegree(self):
        degrees = []
        for _, nodes in self.__tPath:
            for n in nodes:
                d = n.getNDependents()
                if d != 0:
                    degrees.append(d)
        degrees.sort()
        n = len(degrees)

        return degrees[n/2] if n%2 == 1 else (degrees[n/2 - 1] + degrees[n/2]) / 2.

    def getMaxT(self):
        return self.__maxT

    def getMinT(self):
        return self.__minT
