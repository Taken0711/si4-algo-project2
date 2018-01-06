#!/usr/bin/env python3

import csv
import algo


def main():
    ex = algo.main()
    # Need to go step by step, python is exploding
    allStats = []
    for inFile, all_res in ex.items():
        with open("analytics_" + inFile + ".csv", 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=["Algorithme", "Nombre de camions utilisés", "Nombre d'accès aux camions", "Nombre de remplissage des camions",
                    "Moyenne de remplissage d'un camion", "% de camions remplis à 1-10%", "% de camions remplis à 11-20%", "% de camions remplis à 21-30%", "% de camions remplis à 31-40%",
                    "% de camions remplis à 41-50%", "% de camions remplis à 51-60%", "% de camions remplis à 61-70%", "% de camions remplis à 71-80%", "% de camions remplis à 81-90%",
                    "% de camions remplis à 91-100%"])
            writer.writeheader()
            rows = [];
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
                rows.append(row)
            allStats.append(rows)

    algo_names = []
    for row in allStats[0]:
        algo_names.append(row["Algorithme"])
    data = [[0] * (len(allStats[0][0])-1) for _ in range(len(algo_names))]
    writer = csv.DictWriter(open("analytics_exemples/analytics_summary.csv", 'w'), fieldnames=["Algorithme", "Nombre de camions utilisés", "Nombre d'accès aux camions", "Nombre de remplissage des camions",
            "Moyenne de remplissage d'un camion", "% de camions remplis à 1-10%", "% de camions remplis à 11-20%", "% de camions remplis à 21-30%", "% de camions remplis à 31-40%",
            "% de camions remplis à 41-50%", "% de camions remplis à 51-60%", "% de camions remplis à 61-70%", "% de camions remplis à 71-80%", "% de camions remplis à 81-90%",
            "% de camions remplis à 91-100%"])
    writer.writeheader()
    for example in allStats:
        for i in range(0, len(algo_names)):
            j = 0
            for stat in example[i]:
                if stat == "Algorithme":
                    continue
                data[i][j] += example[i][stat]
                j += 1
    for i in range(0, len(algo_names)):
        row = {}
        row["Algorithme"] = algo_names[i]
        row["Nombre de camions utilisés"] = round(data[i][0]/len(allStats), 2)
        row["Nombre d'accès aux camions"] = round(data[i][1]/len(allStats), 2)
        row["Nombre de remplissage des camions"] = round(data[i][2]/len(allStats), 2)
        row["Moyenne de remplissage d'un camion"] = round(data[i][3]/len(allStats), 2)
        j = 4
        for k in range(0, 100, 10):
            row["% de camions remplis à {0}-{1}%".format(k + 1, k + 10)] = round(data[i][j]/len(allStats), 2)
            j += 1
        writer.writerow(row)


if __name__ == '__main__':
    main()
