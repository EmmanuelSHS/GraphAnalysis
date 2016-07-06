#!/usr/bin/env python
# coding=utf-8

import unittest
import sys

sys.path.append("../../../")

from datetime import datetime
from src.window import Node

class NodeTest(unittest.TestCase):

    def testInit(self):
        t = datetime.strptime("2016-04-07T03:34:20Z", "%Y-%m-%dT%H:%M:%SZ")
        n = "Tester"

        node = Node(n, t)
        self.assertEqual(t, node.getTimestamp())
        self.assertEqual(0, node.getNDependents())

    def testCompare(self):
        t1 = datetime.strptime("2016-04-07T03:34:20Z", "%Y-%m-%dT%H:%M:%SZ")
        t2 = datetime.strptime("2016-04-08T03:34:20Z", "%Y-%m-%dT%H:%M:%SZ")

        n1 = Node("t1", t1)
        n2 = Node("t2", t2)

        self.assertEqual(True, n1.getTimestamp() < n2.getTimestamp())

if __name__ == '__main__':
    unittest.main()
