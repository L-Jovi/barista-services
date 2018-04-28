#!/usr/bin/env python
# coding: utf-8

def test():
    for i in range(3):
        yield i

it = test()
for j in it:
    print j
