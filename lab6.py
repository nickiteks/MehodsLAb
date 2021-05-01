import math as m
import numpy as np

x1 = 30
x2 = 50
l = 0.00001
new_grad = np.zeros(2)
f = m.pow(x2 - x1, 2) + m.pow(1 - x1, 2)


def fpr1x1(x1, x2):
    return 4 * x1 - 2 * x2 - 2


def fpr1x2(x1, x2):
    return 2 * x2 - 2 * x1


grad = np.zeros(2)

Hesse_table = np.array([[4, -2],
                        [-2, 2]])
Hesse_table_obr = np.linalg.inv(Hesse_table)

iteration = 0

trigger = True

while trigger:
    grad[0] = fpr1x1(x1, x2)
    grad[1] = fpr1x2(x1, x2)

    xes = np.zeros(2)
    xes[0] = -1 * Hesse_table_obr[0][0] * grad[0] + -1 * Hesse_table_obr[0][1] * grad[1]
    xes[1] = -1 * Hesse_table_obr[1][0] * grad[0] + -1 * Hesse_table_obr[1][1] * grad[1]
    x1 = x1 + xes[0]
    x2 = x2 + xes[1]

    new_grad[0] = fpr1x1(x1, x2)
    new_grad[1] = fpr1x2(x1, x2)
    f = m.pow(x2 - x1, 2) + m.pow(1 - x1, 2)
    print(f'--Итерация номер: {iteration} x1 = {x1}  x2 = {x2} Значение функции : {f}')
    iteration += 1
    if m.fabs(np.linalg.norm(new_grad - grad)) < l:
        trigger = False
