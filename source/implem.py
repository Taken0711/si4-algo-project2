#!/usr/bin/env python3
# coding: utf8

from operator import itemgetter
from BinList import BinList


def run_all(objects, bin_size):
    print(objects)
    return [[f.__name__, run(objects, bin_size, f)] for f in [next_fit, first_fit, worst_fit, best_fit, almost_worst_fit]]


def run(objects, bin_size, algo):
    print("\n")
    print("===", algo.__name__, "===")
    res = algo(objects, bin_size)
    print("Nombre de camions utilisés :", len(res))
    print("Nombre d'accès aux camions :", res.bin_access)
    print("Nombre de remplissage des camions : ", res.bin_change)
    print("Moyenne de remplissage d'un camion :", round(100 * sum(res) / (len(res)*bin_size)), "%")

    binsCounter = [0 for _ in range(0, 5)]
    for filling in res:
        binsCounter[4 - (int)(4*filling / bin_size)] += 1
    for state, nbOfBin in zip(["pleins", "presque pleins", "bien remplis", "peu remplis", "presque vides"], binsCounter):
        print("Camions", state, ":", nbOfBin)

    return res


def next_fit(objects, bin_size):
    bins = BinList(bin_size)
    for object in objects:
        if bins.fit(-1, object):
            bins[-1] += object
        else:
            bins.append(object)
        print(bins)
    return bins


def first_fit(objects, bin_size):
    bins = BinList(bin_size)
    for object in objects:
        fitted = False
        for i in range(len(bins)):
            if bins.fit(i, object):
                bins[i] += object
                fitted = True
                break
        if not fitted:
            bins.append(object)
        print(bins)
    return bins


def worst_fit(objects, bin_size):
    bins = BinList(bin_size)
    for object in objects:
        i = min(enumerate(bins), key=itemgetter(1))[0]
        if bins.fit(i, object):
            bins[i] += object
        else:
            bins.append(object)
        print(bins)
    return bins


def best_fit(objects, bin_size):
    bins = BinList(bin_size)
    for object in objects:
        i = 0
        fitted = False
        for j, bin in enumerate(bins):
            if bins.fit(j, object) and (not fitted or bin > bins[i]):
                i = j
                fitted = True
        if fitted:
            bins[i] += object
        else:
            bins.append(object)
        print(bins)
    return bins


def almost_worst_fit(objects, bin_size):
    bins = BinList(bin_size)
    for object in objects:
        can_fit = list(filter(lambda i: bins.fit(i, object), range(len(bins))))
        can_fit.sort(key=lambda i: bins[i])
        if can_fit:
            bins[can_fit[1 if len(can_fit) > 1 else 0]] += object
        else:
            bins.append(object)
        print(bins)
    return bins
