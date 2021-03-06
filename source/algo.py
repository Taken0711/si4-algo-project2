#!/usr/bin/env python3
# coding: utf8

from glob import glob
from sys import argv

import implem

def run_exemples(verbose):
    res = {}
    for path in glob("exemples/*"):
        print("===", path, "===")
        f = open(path, 'r')
        # Taille bin
        f.readline()
        bin_size = int(f.readline())
        # Objets
        f.readline()
        objects = list(map(int, f.readline().strip()[:-1].split(", ")))
        res[path] = implem.run_all(objects, bin_size, verbose)
    return res


def main():
    run_exemples("-v" in argv)


if __name__ == '__main__':
    main()
