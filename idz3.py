#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    for i in range(10, 1000):
        s = i // 10 + i % 10
        if s + s**2 == i:
            print(i)