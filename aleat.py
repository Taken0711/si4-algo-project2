from random import randint

import source.algo as algo

def main():
    bin_size = int(input("Taille bin: "))
    nb_obj = int(input("Nombre d'objets: "))
    min_obj = int(input("Taille min d'un objet: "))
    max_obj = int(input("Taille max d'un objet: "))
    objects = [randint(min_obj, max_obj) for _ in range(nb_obj)]
    algo.run_all(objects, bin_size)


if __name__ == '__main__':
    main()