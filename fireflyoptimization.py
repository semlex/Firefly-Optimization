import numpy as np
from scipy.spatial import distance


def fireflyoptimization(f, dim, blo, bup, alpha=0.9, beta0=0.8, gamma=0.05, population_size=25, NmaxStep=50):
    population = np.random.uniform(blo, bup, (population_size, dim))
    intensity = np.apply_along_axis(f, 1, population)
    xmin = population[np.argmin(intensity)]
    fmin = f(xmin)

    coordinates = population.tolist()
    neval = population_size

    for k in range(NmaxStep):
        for i in range(population_size):
            for j in range(population_size):
                if intensity[i] > intensity[j]:
                    r = distance.euclidean(population[i], population[j])
                    beta = beta0 * np.exp(-gamma * r * r)
                    population[i] += beta * (population[j] - population[i]) + alpha * (np.random.rand(dim) - 0.5)
                    population[i] = np.clip(population[i], blo, bup)
                    intensity[i] = f(population[i])

                    coordinates.append(population[i])
                    neval += 1

                    if intensity[i] < fmin:
                        fmin = intensity[i]
                        xmin = population[i]

    answer_ = [xmin, fmin, neval, coordinates]
    return answer_
