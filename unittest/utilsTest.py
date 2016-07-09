#!/usr/bin/env python
# coding=utf-8

import unittest
import sys

sys.path.append("../../../")

from datetime import datetime
from src.utils import jsonGenerator, outputFormatter

class UtilsTest(unittest.TestCase):
    toyJson = {"created_time": "2014-03-27T04:28:20Z", "target": "Jamie-Korn", "actor": "Jordan-Gruber"}
    t = datetime.strptime(toyJson["created_time"], "%Y-%m-%dT%H:%M:%SZ")

    def testGenerator(self):
        generator = jsonGenerator("../../../data-gen/venmo-trans.txt")
        c = 0
        while True:
            try:
                next(generator)
                c += 1
            except StopIteration:
                break

        self.assertEqual(1831, c)

    def testFormatter(self):
        self.assertEqual("0.00", outputFormatter(0))
        self.assertEqual("1.00", outputFormatter(1))
        self.assertEqual("1.25", outputFormatter(1.25333))
        self.assertEqual("1.25", outputFormatter(1.249))

if __name__ == '__main__':
    unittest.main()
