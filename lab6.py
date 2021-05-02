import math
import math as m
import numpy as np
import sympy as sp

x1 = 0.5
x2 = 1
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
print('\n')
print('\n')

# Метод наискорейшего спуска

x1 = 100
x2 = 100

grad = np.zeros(2)

iteration = 0

trigger = True

while trigger :
    grad[0] = fpr1x1(x1, x2)
    grad[1] = fpr1x2(x1, x2)

    if math.sqrt(math.pow(grad[0],2) + math.pow(grad[1],2)) < l:
        trigger = False

    x = sp.symbols('x', float=True)

    x1_new = x1 - x * grad[0]
    x2_new = x2 - x * grad[1]

    expr = (x2_new - x1_new) ** 2 + (1 - x1_new) ** 2

    result = sp.solve(expr, x)
    # print(type(expr))
    lmbd = str(result[0])
    lmbd = float(lmbd[0] + lmbd[1] + lmbd[2] + lmbd[3])

    x1 = x1 - lmbd * grad[0]
    x2 = x2 - lmbd * grad[1]

    f = m.pow(x2 - x1, 2) + m.pow(1 - x1, 2)
    print(f'--Итерация номер: {iteration} x1 = {x1}  x2 = {x2} Значение функции : {f}')
    iteration += 1

