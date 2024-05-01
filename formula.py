import math
import numpy as np
import matplotlib.pyplot as plt

c = 299792458
h = 6.6261e-34
k = 1.3806e-23
we_02 = 158019
pa_to_atm = 9.86923e-6

def rel_times(temperature: np.array, coefficient: np.array):
    pt_array = []

    for i in range(len(coefficient)):
        T = temperature[i]
        kvt = coefficient[i]

        pt = (k * T) / (kvt * (1 - math.exp(-(we_02 * c * h) / (k * T))))

        pt_array.append([float(T), float(pt)])

    return pt_array

values = []
lines_to_skip = 1

with open('kvt_FHO-FR_O2-O2.txt', 'r') as file:
    for _ in range(lines_to_skip):
        next(file)

    for line in file:
        data = line.strip().split()
        values.append([float(i) for i in data])
values_array = np.array(values)

temperature_kvt = values_array[:, 2]
values_kvt = values_array[:, 3]

pt_T_array = np.array(rel_times(temperature_kvt, values_kvt))

print(pt_T_array)

x_values_pt_FHO_FR = pt_T_array[:, 0]
y_values_pt_FHO_FR = pt_T_array[:, 1]




values_to_comp_1 = []

with open('relaxation_times_O2-O2.tsv', 'r') as file:
    for _ in range(lines_to_skip):
        next(file)

    for line in file:
        data = line.strip().split()
        values_to_comp_1.append([float(i.replace(',', '.')) for i in data])
values_to_comp_array_1 = np.array(values_to_comp_1)

# print(values_to_comp_array_1)

x_values_pt_T_1 = values_to_comp_array_1[:, 0]
y_values_pt_FHO = values_to_comp_array_1[:, 2]
y_values_pt_M_W = values_to_comp_array_1[:, 1]

values_to_comp_2 = []

with open('ibr.tsv', 'r') as file:
    for i in range(lines_to_skip):
        next(file)

    for line in file:
        data = line.strip().split()
        values_to_comp_2.append([float(i.replace(',', '.')) for i in data])
values_to_comp_array_2 = np.array(values_to_comp_2)

x_values_pt_T_2 = values_to_comp_array_2[:, 0]
y_values_pt_Ibr = values_to_comp_array_2[:, 1]

values_to_comp_3 = []

with open('owen.tsv', 'r') as file:
    for i in range(lines_to_skip):
        next(file)

    for line in file:
        data = line.strip().split()
        values_to_comp_3.append([float(i.replace(',', '.')) for i in data])
values_to_comp_array_3 = np.array(values_to_comp_3)

x_values_pt_T_3 = values_to_comp_array_3[:, 0]
y_values_pt_Owen = values_to_comp_array_3[:, 1]

values_fho =[]

with open('kvt_FHO.txt', 'r') as file:
    for _ in range(lines_to_skip):
        next(file)

    for line in file:
        data = line.strip().split()
        values_fho.append([float(i) for i in data])
values_array_fho = np.array(values_fho)

temperature_kvt_fho = values_array_fho[:, 2]
values_kvt_fho = values_array_fho[:, 3]

pt_T_array_fho = np.array(rel_times(temperature_kvt_fho, values_kvt_fho))

print(pt_T_array_fho)

x_values_pt_fho = pt_T_array_fho[:, 0]
y_values_pt_fho = pt_T_array_fho[:, 1]





# fig, (ax1, ax2) = plt.subplots(2, 1)

fig, ax2 = plt.subplots()
fig.suptitle('Relaxation times 02-02')

# ax1.plot(x_values_kvt, y_values_kvt)
# ax1.set_ylabel('k')
# ax1.set_yscale('log')
# ax1.grid(True)

# ax2.plot(x_values_pt_fho**(-1/3), y_values_pt_fho * pa_to_atm, label='FHO!')   # ptau в атмосферах
ax2.plot(x_values_pt_FHO_FR**(-1/3), y_values_pt_FHO_FR * pa_to_atm, label='FHO-FR')   # ptau в атмосферах
ax2.plot(x_values_pt_T_1, y_values_pt_FHO, label="FHO")
ax2.plot(x_values_pt_T_1, y_values_pt_M_W, label="M-W")

ax2.scatter(x_values_pt_T_3, y_values_pt_Owen, s=20, marker='^', color='indigo', label="Owen")
ax2.scatter(x_values_pt_T_2, y_values_pt_Ibr, s=20,marker='d', color='black', label="Ibraguimova")

ax2.set_yscale('log')
ax2.grid(True)
ax2.set_xlabel(r'$T^{-1/3}, K$')
ax2.set_ylabel(r'$lg p \tau _{O2}^{Vt}$')
ax2.legend()

plt.show()

