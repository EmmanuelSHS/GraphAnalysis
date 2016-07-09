#!/usr/bin/env python
# coding=utf-8

import networkx as nx
from warnings import warn
from datetime import datetime, timedelta


class Window:
    def __init__(self):
        """
        flag for update, if no need for update, just output previous median degree
        initialize with a undirected graph
        """
        self.__g = nx.Graph()
        self.__maxT = datetime.strptime("1000-01-01 01:01:00", "%Y-%m-%d %H:%M:%S")
        self.__minT = datetime.strptime("1000-01-01 01:00:00", "%Y-%m-%d %H:%M:%S")
        self.__needUpdate = False
        self.__prevMedian = 0

    def insertRec(self, json):
        """
        insert json record,
        if actor or target field is missing, discard this record and raise ValueError
        """
        time = datetime.strptime(json["created_time"], "%Y-%m-%dT%H:%M:%SZ")
        act, tar = json["actor"], json["target"]
        if act != "" and tar != "":
            if time >= self.__minT:
                if not self.__g.has_edge(act, tar):
                    self.__g.add_node(act)
                    self.__g.add_node(tar)
                    self.__g.add_edge(act, tar, timestamp = time)
                else:
                    # update to the max timestamp, sometimes latter records would have smaller timestamp
                    self.__g[act][tar]["timestamp"] = max(self.__g[act][tar]["timestamp"], time)
                self.__updateT(time)
                self.__needUpdate = True
        else:
            warn("Discard a record with missing actor/target.")

    def __updateT(self, newT):
        if newT >= self.__maxT:
            self.__maxT = newT
            self.__minT = newT - timedelta(minutes = 1)

    def __updateGraph(self):
        """update the graph with timestamp filter"""
        self.__g = nx.Graph([(u, v, d) for u, v, d in self.__g.edges(data = True) if self.__minT <= d["timestamp"] <= self.__maxT])

    def __getDegrees(self):
        degrees = [len(self.__g.neighbors(n)) for n in self.__g.nodes_iter() if len(self.__g.neighbors(n)) > 0]
        degrees.sort()
        return len(degrees), degrees

    def returnMedian(self):
        if self.__needUpdate:
            self.__updateGraph()
            n, degrees = self.__getDegrees()

            if n == 0:
                self.__prevMedian = 0
            else:
                self.__prevMedian = degrees[n/2] if n%2 == 1 else (degrees[n/2-1] + degrees[n/2]) / 2.0
            self.__needUpdate = False
        return self.__prevMedian

    def getMaxT(self):
        return self.__maxT

    def getMinT(self):
        return self.__minT
        
