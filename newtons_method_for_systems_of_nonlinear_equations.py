# Метод Ньютона решения системы из 2-х нелинейных уравнений

from math import cos, sin
import numpy as np
from tabulate import tabulate

# 1. Входные данные

e = 0.001  # Погрешность


# Система:
def f1(x, y):
    return -x + sin(y + 0.5) - 1


def f2(x, y):
    return -y - cos(x - 2) + 0


# Производные данных фунций:
def f1x(x):
    return -1


def f1y(y):
    return cos(y + 0.5)


def f2x(x):
    return sin(x - 2)


def f2y(y):
    return -1


# Начальные значения x и y:
x_i = 0.2
y_i = 0.5

# 2. Расчеты и вывод ответа

# Изменение значения переменных в ходе итерации цикла:
delta_x = 0
delta_y = 0

# Шапка таблицы:
table = [["i", "x", "Δx", "y", "Δy"]]

for i in range(0, 100):

    # Строка таблицы:
    table += [[i, x_i, delta_x, y_i, delta_y]]

    # Якобиан:
    W = np.array([
        [f1x(x_i), f1y(y_i)],
        [f2x(x_i), f2y(y_i)]
    ])

    # Транспонированный якобиан:
    W_r = np.linalg.inv(W)

    # Столбец значений функций:
    f = [f1(x_i, y_i),
         f2(x_i, y_i)]

    # W_r * f:
    w_r_multiplied_by_f = [
        W_r[0][0] * f[0] + W_r[0][1] * f[1],
        W_r[1][0] * f[0] + W_r[1][1] * f[1],
    ]

    # Изменение значения переменных в ходе итерации цикла:
    delta_x = w_r_multiplied_by_f[0]
    delta_y = w_r_multiplied_by_f[1]

    # Новые x и y:
    new_x = x_i - delta_x
    new_y = y_i - delta_y

    # Выходим из цикла, если срабатывает критерий остановки:
    if (not abs(x_i - new_x) > e) and (not abs(y_i - new_y) > e):
        table += [[i + 1, new_x, "...", new_y, "..."]]
        break

    # Присваиваем x и y новые значения:
    x_i = new_x
    y_i = new_y

print(tabulate(table, headers='firstrow', tablefmt='grid'))
