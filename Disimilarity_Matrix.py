from math import sqrt
import numpy as np
import csv

def euclidean_distance(val1, val2, nums):
    return (abs(val1-val2)/(max(nums)-min(nums)))


data, nums, num_rec = [], [], 0

f=open('disim_mat_dat.csv', 'r')
reader=csv.DictReader(f)
for row in reader:
    x = row['NominalAttribute']
    y = float(row['NumericAttribute'])
    nums.append(y)
    rec = {"x":x, "y":y}
    data.append(rec)

n = len(data)
nom_disim_mat = np.zeros((n, n))
num_disim_mat = np.zeros((n, n))
mxd_disim_mat = np.zeros((n, n))

for i in range(n):
    for j in range(n):
        if (data[i]['x'] == data[i]['x']):
            x_disim = 0
        else:
            x_disim = 1
        y_disim = round(euclidean_distance(float(data[i]['y']), float(data[j]['y']), nums), 2)
        nom_disim_mat[i][j] = x_disim
        num_disim_mat[i][j] = y_disim
        mxd_disim_mat[i][j] = round((x_disim + y_disim)/2, 2)

print(f"Nominal Dissimilarity Matrix is : \n{nom_disim_mat}\nNumeric Dissimilarity Matrix is : \n{num_disim_mat}\nMixed Dissimilarity Matrix is : \n{mxd_disim_mat}")
