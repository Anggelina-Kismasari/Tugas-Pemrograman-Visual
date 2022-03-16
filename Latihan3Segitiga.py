# Anggelina Kismasari 20051397034 2020MIB

class jawaban :
    #fungsi rumus untuk menampilkan output komponen rumus dan hasil luas keliling
    def rumus (angka): 
        print (' ')
        #untuk membedakan angka dari setiap komponen maka diberi penanda bill1, bill2, dan seterusnya
        print ('Panjang alas : ', angka.bil1) 
        print ('Panjang tinggi : ', angka.bil2)
        print ('Panjang sisi A : ', angka.bil3)
        print ('Panjang sisi B : ', angka.bil4)
        print ('Panjang sisi C : ', angka.bil5)
        print (' ')
        print ('Luas segitiga adalah :', 1/2*angka.bil1*angka.bil2)
        print ('Keliling segitiga adalah :', angka.bil3+angka.bil4+angka.bil5)
#class dibawah sebagai class turunan dari class jawaban, sehingga memiliki sifat-sifat yg ada pada class induk
class nilai(jawaban) :
    #fungsi konstruktor, untuk method pertama yang akan dieksekusi saat pertama kali membuat instance dari class
    def __init__(self):
        #parameter untuk mengakses Intance, bisa juga untuk memanggil method dalam method lain
        self.bil1 = int(input('Masukan panjang alasnya : '))
        self.bil2 = int(input('Masukan panjang tingginya : '))
        self.bil3 = int(input('Masukan panjang sisi A : '))
        self.bil4 = int(input('Masukan panjang sisi B : '))
        self.bil5 = int(input('Masukan panjang sisi C : '))

confirm = ("y")
#melakukan looping pada program
while confirm == ("y") :
    print ("Mencari Luas dan Keliling Segitiga")
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