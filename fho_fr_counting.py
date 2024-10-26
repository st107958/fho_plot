import math
import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt

c = 299792458
h = 6.6261e-34
k = 1.3806e-23
spectr_constants = {
    'N2': 235857,
    'O2': 158019,
    'NO': 190420
}
pa_to_atm = 9.86923e-6

molecule = 'NO-O' # тут менять
particle = 'NO' # тут

lines_to_skip = 1
def rel_times(temperature: np.array, coefficient: np.array, molecule: str):
    t_array = []
    for i in range(len(coefficient)):
        T = temperature[i]
        kvt = coefficient[i]

        t = (k * T) / (kvt * (1 - math.exp(-(spectr_constants[particle] * c * h) / (k * T)))) * pa_to_atm

        t_array.append([float(T), float(t)])

    return t_array

path = molecule + '.txt'
fullpath = os.path.join('FHO_coef', path)

values_fho = []
with open(fullpath, 'r') as file:
    for _ in range(lines_to_skip):
        next(file)

    for line in file:
        data = line.strip().split()
        values_fho.append([float(i) for i in data])
values_array_fho = np.array(values_fho)

temperature_kvt_fho = values_array_fho[:, 2]
values_kvt_fho = values_array_fho[:, 3]
pt_T_array_fho = np.array(rel_times(temperature_kvt_fho, values_kvt_fho, molecule))



filename = 'FHO_FR.csv' #тут
fullfilename = os.path.join(molecule, filename) #тут
np.savetxt(fullfilename, pt_T_array_fho)

