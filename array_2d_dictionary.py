array_2d = {
    'Senin' : [1,2,3],
    'Selasa' : [4,5,6]
}

print(array_2d['Senin'])
print(array_2d['Selasa'][2])

for hari, value in array_2d.items(): #'items()' untuk memanggil key dan value nya
    print(f'{hari} : {value[0]}')