import csv
import algo


def main():
    ex = algo.main()
    # Need to go step by step, python is exploding
    for inFile, all_res in ex.items():
        with open("analytics_" + inFile + ".csv", 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=["Algorithme", "Nombre de camions utilisés", "Nombre d'accès aux camions", "Nombre de remplissage des camions",
                    "Moyenne de remplissage d'un camion", "Camions remplis à 1-10%", "Camions remplis à 11-20%", "Camions remplis à 21-30%", "Camions remplis à 31-40%",
                    "Camions remplis à 41-50%", "Camions remplis à 51-60%", "Camions remplis à 61-70%", "Camions remplis à 71-80%", "Camions remplis à 81-90%",
                    "Camions remplis à 91-100%"])
            writer.writeheader()
            for res in all_res:
                row = {}
                row["Algorithme"] = res[0]
                bins = res[1]
                row["Nombre de camions utilisés"] = len(bins)
                row["Nombre d'accès aux camions"] = bins.bin_access
                row["Nombre de remplissage des camions"] = bins.bin_change
                row["Moyenne de remplissage d'un camion"] = round(100 * sum(bins) / (len(bins)*bins.bin_size))
                for i in range(0, 90, 10):
                    min = i + 1
                    max = i + 10
                    row["Camions remplis à {0}-{1}%".format(min, max)] = len(list(filter(lambda bin: min <= bin/bins.bin_size <= max, bins)))/len(bins)
                writer.writerow(row)


if __name__ == '__main__':
    main()
