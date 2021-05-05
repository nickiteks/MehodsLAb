from scipy import optimize
import math

x = 0
f = -4 * x + math.exp(math.fabs(x - 0.2) * x)

###-----------Алгоритм свенна
x0 = 1
h = 1
xa = x0 - h
xb = x0 + h
trigger = True

while trigger:
    fa = -4 * xa + math.exp(math.fabs(xa - 0.2) * xa)
    f0 = -4 * x0 + math.exp(math.fabs(x0 - 0.2) * x0)
    fb = -4 * xb + math.exp(math.fabs(xb - 0.2) * xb)
    if fa >= f0 <= fb:
        trigger = False
    else:
        h = 2 * h
        xa = x0 - h
        xb = x0 + h

print(f'Интервал [{xa} , {xb}]')

# -----Метод равномерного поиска
N = int(input('введите N'))
functions = []
for i in range(N):
    xi = xa + i * ((xb - xa) / (N + 1))
    functions.append(-4 * xi + math.exp(math.fabs(xi - 0.2) * xi))

min = functions[0]
indexX = 0

for i in range(len(functions)):
    if functions[i] < min:
        min = functions[i]
        indexX = i

xi = xa + indexX * ((xb - xa) / (N + 1))

print(f'x = x{indexX} = {xi}')

# --- метод ньютона
x = int(input('введите x0'))
l = float(input('введите l'))
fpr1 = -4 + math.exp(math.fabs(x - 0.2) * x) * ((x * (x - 0.2)) / (math.fabs(x - 0.2)) + math.fabs(x - 0.2))
fpr2 = math.exp(math.fabs(x - 0.2) * x) * (4 * math.pow(x, 2) - 0.8 * x + 0.04) + math.exp(math.fabs(x - 0.2) * x) * (
        (x - 0.2) / (math.fabs(x - 0.2)) + (math.pow(x, 3) - 0.6 * math.pow(x, 2) - 0.008) / (
        math.fabs(x - 0.2) * math.pow(x - 0.2, 2)))

trigger = True

while trigger:
    x = x - (fpr1 / fpr2)
    fpr1 = -4 + math.exp(math.fabs(x - 0.2) * x) * ((x * (x - 0.2)) / (math.fabs(x - 0.2)) + math.fabs(x - 0.2))
    fpr2 = math.exp(math.fabs(x - 0.2) * x) * (4 * math.pow(x, 2) - 0.8 * x + 0.04) + math.exp(
        math.fabs(x - 0.2) * x) * (
                   (x - 0.2) / (math.fabs(x - 0.2)) + (math.pow(x, 3) - 0.6 * math.pow(x, 2) - 0.008) / (
                   math.fabs(x - 0.2) * math.pow(x - 0.2, 2)))
    if math.fabs(fpr1) <= l:
        trigger = False

print(f'x = {x}')

# -----метод золотого сечения
xa = xa
xb = xb
l = float(input('введите l'))

y = xa + ((3-math.sqrt(5)) / 2) * (xb - xa)
z = xa + xb - y

trigger = True

while trigger:
    fy = -4 * y + math.exp(math.fabs(y - 0.2) * y)
    fz = -4 * z + math.exp(math.fabs(z - 0.2) * z)

    if fy <= fz:
        xb = z
        z = y
        y = xa + xb - y
    else:
        xa = y
        y = z
        z = xa + xb - z
    de = math.fabs(xb - xa)
    if de <= l:
        x = (xa+xb)/2
        trigger = False

print(f'x = {x}')
