#!/usr/bin/env python
# coding=utf-8

class Tester:
    def __init__(self):
        f1 = 0
        f2 = 1

def main():
    t1 = Tester()
    t2 = Tester()
    print t1
    print t2

    l = [t1, t2]
    d = {"t1": t1, "t2": t2}

    print l
    print d

    t1.f1 = 1

    print l[0].f1
    print d["t1"].f1

if __name__ == '__main__':
    main()
