#!/usr/bin/env python
# coding=utf-8

import unittest
import sys

sys.path.append("../../../")

from datetime import datetime
#from src.utils import outputFormatter
from src.window import Window

class UtilsTest(unittest.TestCase):
    rec1 = {"created_time": "2014-03-27T04:28:20Z", "target": "Jamie-Korn", "actor": "Jordan-Gruber"}
    rec2 = {"created_time": "2014-03-28T04:28:20Z", "target": "Jamie-Korn", "actor": "Jordan-Gruber"}

    t1 = datetime.strptime(rec1["created_time"], "%Y-%m-%dT%H:%M:%SZ")
    t2 = datetime.strptime(rec2["created_time"], "%Y-%m-%dT%H:%M:%SZ")

    w = Window()

    def testInitInsertion(self):
        self.w.insertRec(self.rec1)
        self.w.returnMedian()

        self.assertEqual(self.t1, self.w.getMaxT())

    def testSecondInsertion(self):
        self.w.insertRec(self.rec2)
        self.w.returnMedian()

        self.assertEqual(self.t2, self.w.getMaxT())


if __name__ == '__main__':
    unittest.main()
