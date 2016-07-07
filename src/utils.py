#!/usr/bin/env python
# coding=utf-8

import json


def jsonGenerator(filepath):
    with open(filepath, 'r') as f:
        for line in f:
            yield json.loads(line)
    f.close()

def outputFormatter(out):
    return "%.2f" % float(out)


class Savor:
    def __init__(self, filepath):
        self.f = open(filepath, 'w')

    def writeLine(self, line):
        self.f.write(line+'\n')

    def close(self):
        self.f.close()
