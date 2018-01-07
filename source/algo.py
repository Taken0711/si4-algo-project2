#!/usr/bin/env python3
# coding: utf8

from glob import glob

import implem


def main():
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
        res[path] = implem.run_all(objects, bin_size)
    return res


if __name__ == '__main__':
    main()
