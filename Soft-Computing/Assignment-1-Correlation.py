# %%
import numpy as np
from tabulate import tabulate

while True:
    input_list = list()

    while True:
        try:
            a = float(input('Enter elements for parameter 1 (-1 to stop): '))
        except:
            print('Check input and enter from last element again')
        if a == -1:
            break
        input_list.append(a)

    x = np.asarray(input_list)

    input_list = list()

    while True:
        try:
            a = float(input('Enter elements for parameter 2 (-1 to stop): '))
        except:
            print('Check input and enter from last element again')
        if a == -1:
            break
        input_list.append(a)

    y = np.asarray(input_list)

    if len(x) == len(y):
            break
    else:
        print('Enter the elements for both the arrays again')


sigma_x = np.sum(x)
sigma_y = np.sum(y)

sigma_x_square = np.sum(np.square(x))
sigma_y_square = np.sum(np.square(y))

sigma_xy = np.sum(np.multiply(x, y))

n = len(x)

r = np.divide(
            (np.subtract(np.multiply(n, sigma_xy), np.multiply(sigma_x, sigma_y))),
            (
                np.multiply(
                np.sqrt(np.subtract(np.multiply(n, sigma_x_square), np.square(sigma_x))),
                np.sqrt(np.subtract(np.multiply(n, sigma_y_square), np.square(sigma_y)))                
                )
            )
            )

data_table = {
    'x': x,
    'y': y,
    'x-square': np.square(x),
    'y-square': np.square(y),
    'xy': np.multiply(x, y),
}

print(tabulate(data_table, headers = 'keys'))
print()
print('The correlation coefficient is', round(r, 4))