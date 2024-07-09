import numpy as np

array_2d = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])

print(array_2d[0,2])
print(array_2d[0][2])

total_perbaris = np.sum(array_2d, axis=0)
total_perkolom = np.sum(array_2d, axis=1)
print(total_perbaris)
print(total_perkolom)

nilai_tertinggi_perbaris = np.max(array_2d, axis=0)
nilai_tertinggi_perkolom = np.max(array_2d, axis=1)
print(nilai_tertinggi_perbaris)
print(nilai_tertinggi_perkolom)

print('====================')
index_nilai_tertinggi_baris = np.argmax(array_2d, axis=0)
index_nilai_tertinggi_kolom = np.argmax(array_2d, axis=1)
print(index_nilai_tertinggi_baris)
print(index_nilai_tertinggi_kolom)