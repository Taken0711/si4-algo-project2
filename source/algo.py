from operator import itemgetter


def run_all(objects, bin_size):
    print ("\n", objects, "\nFirst fit:", str(first_fit(objects, bin_size)))
    print ("\n", objects, "\nNext fit:", str(next_fit(objects, bin_size)))
    print ("\n", objects, "\nWorst fit:", str(worst_fit(objects, bin_size)))
    print ("\n", objects, "\nBest fit:", str(best_fit(objects, bin_size)))
    print ("\n", objects, "\nAlmost worst fit:", str(best_fit(objects, bin_size)))


def fit(bin, object, max):
    return bin + object <= max

def next_fit(objects, bin_size):
    bins = [0]
    for object in objects:
        if fit(bins[-1], object, bin_size):
            bins[-1] += object
        else:
            bins.append(object)
        print(bins)
    return len(bins)


def first_fit(objects, bin_size):
    bins = [0]
    for object in objects:
        fitted = False
        for i, bin in enumerate(bins):
            if fit(bin, object, bin_size):
                bins[i] += object
                fitted = True
                break
        if not fitted:
            bins.append(object)
        print(bins)
    return len(bins)


def worst_fit(objects, bin_size):
    bins = [0]
    for object in objects:
        i = min(enumerate(bins), key=itemgetter(1))[0]
        if fit(bins[i], object, bin_size):
            bins[i] += object
        else:
            bins.append(object)
        print(bins)
    return len(bins)


def best_fit(objects, bin_size):
    bins = [0]
    for object in objects:
        i = 0
        fitted = False
        for j, bin in enumerate(bins):
            if fit(bin, object, bin_size) and (bin > bins[i] or not fitted):
                i = j
                fitted = True
        if fitted:
            bins[i] += object
        else:
            bins.append(object)
        print(bins)
    return len(bins)


def almost_worst_fit(objects, bin_size):
    bins = [0]
    can_fit = []
    for object in objects:
        for e in enumerate(bins):
            if fit(e[1], object, bin_size):
                can_fit.append(e)
        if len(can_fit) > 1:
            bins[can_fit[1][0]] += object
        elif len(can_fit) == 1:
            bins[can_fit[0][0]] += object
        else:
            bins.append(object)
        print(bins)
    return len(bins)