#!/usr/bin/env python3
# coding: utf8

from random import randint

import implem
from sys import argv

def main():

    n = int(input("Nombre de série: "))
    bin_size = int(input("Taille bin: "))
    nb_obj = int(input("Nombre d'objets: "))
    min_obj = int(input("Taille min d'un objet: "))
    max_obj = int(input("Taille max d'un objet: "))
    best_case = {}
    worst_case = {}
    average = {}
    progress = 0
    for _ in range(n):
        if int(_/n * 100 / 10) > progress:
            progress += 1
            print(str(progress*10)+"%...")
        objects = [randint(min_obj, max_obj) for _ in range(nb_obj)]
        all_res = implem.run_all(objects, bin_size, "-v" in argv)
        for res in all_res:
            algo = res[0]
            if not algo in best_case:
                best_case[algo] = {}
            bins = res[1]
            if not best_case[algo] or round(100 * sum(bins) / (len(bins)*bins.bin_size)) > best_case[algo]["Moyenne de remplissage d'un camion"]:
                best_case[algo]["Nombre de camions utilisés"] = len(bins)
                best_case[algo]["Nombre d'accès aux camions"] = bins.bin_access
                best_case[algo]["Moyenne de remplissage d'un camion"] = round(100 * sum(bins) / (len(bins)*bins.bin_size))
            if not algo in worst_case:
                worst_case[algo] = {}
            if not worst_case[algo] or round(100 * sum(bins) / (len(bins)*bins.bin_size)) < worst_case[algo]["Moyenne de remplissage d'un camion"]:
                worst_case[algo]["Nombre de camions utilisés"] = len(bins)
                worst_case[algo]["Nombre d'accès aux camions"] = bins.bin_access
                worst_case[algo]["Moyenne de remplissage d'un camion"] = round(100 * sum(bins) / (len(bins)*bins.bin_size))
            if not algo in average:
                average[algo] = {"Nombre de camions utilisés": 0, "Nombre d'accès aux camions": 0, "Moyenne de remplissage d'un camion": 0}
            average[algo]["Nombre de camions utilisés"] += len(bins)
            average[algo]["Nombre d'accès aux camions"] += bins.bin_access
            average[algo]["Moyenne de remplissage d'un camion"] += round(100 * sum(bins) / (len(bins) * bins.bin_size))
    for algo in average.keys():
        average[algo]["Nombre de camions utilisés"] /= n
        average[algo]["Nombre d'accès aux camions"] /= n
        average[algo]["Moyenne de remplissage d'un camion"] /= n
    for algo in best_case.keys():
        print("===", algo, "===")
        print("{} {}: {}".format(algo, "best case", ", ".join([k + " : " + str(best_case[algo][k]) for k in best_case[algo]])))
        print("{} {}: {}".format(algo, "average", ", ".join([k + " : " + str(average[algo][k]) for k in average[algo]])))
        print("{} {}: {}".format(algo, "worst case", ", ".join([k + " : " + str(worst_case[algo][k]) for k in worst_case[algo]])))
        print()



if __name__ == '__main__':
    main()
