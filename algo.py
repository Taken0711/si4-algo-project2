from random import randint
from glob import glob

from source import implem


def main():
    print(glob("*"))
    for path in glob("exemples/*"):
        print("===", path, "===")
        f = open(path, 'r')
        # Taille bin
        f.readline()
        bin_size = int(f.readline())
        # Objets
        f.readline()
        objects = list(map(int, f.readline().strip()[:-1].split(", ")))
        return implem.run_all(objects, bin_size)


if __name__ == '__main__':
    main()