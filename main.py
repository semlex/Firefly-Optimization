from draw import *
from functions import *
from fireflyoptimization import *
import numpy as np


def main():
    print("Himmelblau function:")
    [xmin, f, neval, coords] = fireflyoptimization(fH, 2, -4, 4)  #функция Химмельблау
    print('x_min = (', xmin[0], ',', xmin[1], '),', 'f_min = ', f, ', neval = ', neval)
    draw(coords, xmin, neval, fH, -4, 4, "Himmelblau")

    print("Rosenbrock function:")
    [xmin, f, neval, coords] = fireflyoptimization(fR, 2, -4, 4)  # функция Розенброка
    print('x_min = (', xmin[0], ',', xmin[1], '),', 'f_min = ', f, ', neval = ', neval)
    draw(coords, xmin, neval, fR, -4, 4, "Rosenbrock")

    print("Branin function:")
    [xmin, f, neval, coords] = fireflyoptimization(fBr, 2, -5, 10)  # функция Бранина
    print('x_min = (', xmin[0], ',', xmin[1], '),', 'f_min = ', f, ', neval = ', neval)
    draw(coords, xmin, neval, fR, -5, 10, "Branin")

    print("Beale function:")
    [xmin, f, neval, coords] = fireflyoptimization(fBe, 2, -4.5, 4.5)  # функция Била
    print('x_min = (', xmin[0], ',', xmin[1], '),', 'f_min = ', f, ', neval = ', neval)
    draw(coords, xmin, neval, fBe, -4.5, 4.5, "Beale")

    print("Beale function:")
    [xmin, f, neval, coords] = fireflyoptimization(fSph, 3, -5.12, 5.12)  # функция сферы
    print('x_min = (', xmin[0], ',', xmin[1], ',', xmin[2], '),', 'f_min = ', f, ', neval = ', neval)
    draw(coords, xmin, neval, fSph, -5.12, 5.12, "Sphere", True)

if __name__ == '__main__':
    main()
