#!/usr/bin/env python
# coding=utf-8

import networkx as nx
from datetime import datetime, timedelta


class Window:
    def __init__(self):
        self.__g = nx.Graph()
        self.__maxT = datetime.strptime("1000-01-01 01:01:00", "%Y-%m-%d %H:%M:%S")
        self.__minT = datetime.strptime("1000-01-01 01:00:00", "%Y-%m-%d %H:%M:%S")

    def insertRec(self, json):
        time = datetime.strptime(json["created_time"], "%Y-%m-%dT%H:%M:%SZ")
        act, tar = json["actor"], json["target"]
        if time >= self.__minT:
            if act != "" and tar != "":
                if not self.__g.has_edge(act, tar):
                    self.__g.add_node(act)
                    self.__g.add_node(tar)
                    self.__g.add_edge(act, tar, timestamp = time)
                else:
                    self.__g[act][tar]["timestamp"] = time
                self.__updateT(time)

    def __updateT(self, newT):
        if newT > self.__maxT:
            self.__maxT = newT
            self.__minT = newT - timedelta(minutes = 1)

    def __updateGraph(self):
        self.__g = nx.Graph([(u, v, d) for u, v, d in self.__g.edges(data = True) if self.__minT <= d["timestamp"] <= self.__maxT])

    def __getDegrees(self):
        degrees = []
        for n in self.__g.nodes_iter():
            ln = len(self.__g.neighbors(n))
            if ln > 0:
                degrees.append(ln)
        degrees.sort()
        return len(degrees), degrees

    def returnMedian(self):
        self.__updateGraph()
        n, degrees = self.__getDegrees()

        if n == 0:
            return 0
        return degrees[n/2] if n%2 == 1 else (degrees[n/2-1] + degrees[n/2]) / 2.0

    def getMaxT(self):
        return self.__maxT

    def getMinT(self):
        return self.__minT
        
