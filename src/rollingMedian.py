#!/usr/bin/env python
# coding=utf-8

from sys import argv
from utils import jsonGenerator, outputFormatter, Savor
from window import Window

def main(frompath, topath):
    generator = jsonGenerator(frompath)
    win = Window()
    savor = Savor(topath)
    while True:
        try:
            rec = next(generator)
            win.insertRec(rec)
            savor.writeLine(outputFormatter(win.returnMedian()))
        except StopIteration:
            break
    savor.close()

if __name__ == '__main__':
    main(argv[1], argv[2])
