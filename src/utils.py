#!/usr/bin/env python
# coding=utf-8

import json
from datetime import datetime
from window import Node

def recToNodes(jsonRec):
    # return two nodes
    time = datetime.strptime(jsonRec["created_time"], "%Y-%m-%dT%H:%M:%SZ")
    source = Node(jsonRec["actor"], time)
    target = Node(jsonRec["target"], time)

    source.addDependent(target)
    target.addDependent(source)

    return source, target

def jsonGenerator(filepath):
    with open(filepath, 'r') as f:
        for line in f:
            yield json.loads(line)
    f.close()

