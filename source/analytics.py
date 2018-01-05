#!/usr/bin/env python3

import csv
import algo


def main():
    ex = algo.main()
    # Need to go step by step, python is exploding
    for inFile, all_res in ex.items():
        with open("analytics_" + inFile + ".csv", 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=["Algorithme", "Nombre de camions utilisés", "Nombre d'accès aux camions", "Nombre de remplissage des camions",
                    "Moyenne de remplissage d'un camion", "% de camions remplis à 1-10%", "% de camions remplis à 11-20%", "% de camions remplis à 21-30%", "% de camions remplis à 31-40%",
                    "% de camions remplis à 41-50%", "% de camions remplis à 51-60%", "% de camions remplis à 61-70%", "% de camions remplis à 71-80%", "% de camions remplis à 81-90%",
                    "% de camions remplis à 91-100%"])
            writer.writeheader()
            for res in all_res:
                row = {}
                row["Algorithme"] = res[0]
                bins = res[1]
                row["Nombre de camions utilisés"] = len(bins)
                row["Nombre d'accès aux camions"] = bins.bin_access
                row["Nombre de remplissage des camions"] = bins.bin_change
                row["Moyenne de remplissage d'un camion"] = round(100 * sum(bins) / (len(bins)*bins.bin_size))
                for i in range(0, 100, 10):
                    m_min = i + 1
                    m_max = i + 10
                    row["% de camions remplis à {0}-{1}%".format(m_min, m_max)] = round(100 * len(list(filter(lambda bin: m_min <= 100 * bin/bins.bin_size <= m_max, bins)))/len(bins), 2)
                writer.writerow(row)


if __name__ == '__main__':
    main()
