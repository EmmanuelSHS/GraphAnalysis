#!/usr/bin/env python
# coding=utf-8

import unittest
import sys

sys.path.append("../")

from datetime import datetime, timedelta
from src.utils import outputFormatter
from src.window import Window

class UtilsTest(unittest.TestCase):
    rec1 = {"created_time": "2014-03-27T04:28:20Z", "target": "Jamie-Korn", "actor": "Jordan-Gruber"}
    rec2 = {"created_time": "2014-03-28T04:28:20Z", "target": "Jamie-Korn", "actor": "Jordan-Gruber"}

    t1 = datetime.strptime(rec1["created_time"], "%Y-%m-%dT%H:%M:%SZ")
    t2 = datetime.strptime(rec2["created_time"], "%Y-%m-%dT%H:%M:%SZ")

    def testSingleInsertion(self):
        w = Window()
        
        w.insertRec(self.rec1)
        m = outputFormatter(w.returnMedian())

        self.assertEqual(self.t1, w.getMaxT())
        self.assertEqual(self.t1 - timedelta(minutes=1), w.getMinT())
        self.assertEqual("1.00", m)

    def testNullInsertion(self):
        rec = {"created_time": "2014-03-27T04:28:21Z", "target": "Jamie-Korn", "actor": ""}

        w = Window()
        w.insertRec(self.rec1)
        w.insertRec(self.rec2)
        w.insertRec(rec)
        m = outputFormatter(w.returnMedian())
    
        self.assertEqual("1.00", m)
        self.assertEqual(self.t2 - timedelta(minutes=1), w.getMinT())
        self.assertEqual(self.t2, w.getMaxT())

    def testMultipleInsertion(self):
        # case 1: base case
        rec1 = {"created_time": "2016-04-07T03:34:18Z", "target": "Ying-Mo", "actor": "Jamie-Korn"}
        rec2 = {"created_time": "2016-04-07T03:34:58Z", "target": "Maddie-Franklin", "actor": "Maryann-Berry"}

        w = Window()
        w.insertRec(rec1)
        w.insertRec(rec2)

        m = outputFormatter(w.returnMedian())
        self.assertEqual(m, "1.00")

        # case2: one old record inserted, but in window
        rec3 = {"created_time": "2016-04-07T03:34:58Z", "target": "Ying-Mo", "actor": "Maddie-Franklin"}
        w.insertRec(rec3)

        m = outputFormatter(w.returnMedian())
        self.assertEqual(m, "1.50")

        # case 3: new insertion, one old removed
        rec4 = {"created_time": "2016-04-07T03:35:02Z", "target": "Connor-Liebman", "actor": "Nick-Shirreffs"}
        w.insertRec(rec4)

        m = outputFormatter(w.returnMedian())
        self.assertEqual(m, "1.00")


if __name__ == '__main__':
    unittest.main()
