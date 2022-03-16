# Anggelina Kismasari 20051397034 2020MIB

class jawaban :
    #fungsi rumus untuk menampilkan output komponen rumus dan hasil volume
    def rumus (angka): 
        print (' ')
        #untuk membedakan angka dari setiap komponen maka diberi penanda bill1, bill2, dan seterusnya
        print ('Ukuran alas permukaan : ', angka.bil1)
        print ('Ukuran tinggi permukaan : ', angka.bil2)
        print ('Ukuran tinggi prisma : ', angka.bil3)
        print (' ')
        print ('Volume prisma segitiga adalah :', (1/2*angka.bil1*angka.bil2)*angka.bil3)
#class dibawah sebagai class turunan dari class jawaban, sehingga memiliki sifat-sifat yg ada pada class induk
class nilai(jawaban) :
    #fungsi konstruktor, untuk method pertama yang akan dieksekusi saat pertama kali membuat instance dari class
    def __init__(self):
        #parameter untuk mengakses Intance, bisa juga untuk memanggil method dalam method lain
        self.bil1 = int(input('Masukan ukuran alas permukaannya : '))
        self.bil2 = int(input('Masukan ukuran tinggi permukaannya : '))
        self.bil3 = int(input('Masukan ukuran tinggi prisma : '))

confirm = ("y")
#melakukan looping pada program
while confirm == ("y") :
    print ("Mencari Volume Prisma Segitiga")
    #untuk memanggil class jawaban dan class nilai
    objek = nilai()
    objek.rumus()
    print(" ")
    confirm = input("Apakah anda ingin memulai lagi? : ")
    if confirm == ("y") :
        print (" ")
        continue
    elif confirm == ("n") :
        break
    else :
        print ("Pilihan yang Anda inputkan salah!")
        break