# Anggelina Kismasari 20051397034 2020MIB

matriks1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
matriks2 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for x in range (0, len(matriks1)) :
    for y in range (0, len(matriks1[0])) :
        print(matriks1[x][y] - matriks2[x][y], end = '')
        print