# Anggelina Kismasari 20051397034 2020MIB

class Matrix:
  #fungsi konstruktor, untuk method pertama yang akan dieksekusi saat pertama kali membuat instance dari class
  def __init__(self, data):
    self.data = data
  #fungsi untuk mengembalikan string representasi dari suatu objek
  def __repr__(self):
    return repr(self.data)  
  #fungsi untuk menambahkan suatu objek tertentu
  def __add__(self, other):
    data = []

    for j in range(len(self.data)):
        data.append([])
        for k in range(len(self.data[0])):
            data[j].append(self.data[j][k] + other.data[j][k])

    return Matrix(data)

x = Matrix([[1,4,6],[8,2,5],[7,9,3]])
y = Matrix([[1,4,6],[8,2,5],[7,9,3]])
# Menampilkan output hasil penjumlahan matriks
print(x + y)