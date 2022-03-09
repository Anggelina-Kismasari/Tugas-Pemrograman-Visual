# Anggelina Kismasari 20051397034 MI20B

abjad = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

# Berikut untuk menginput jumlah key dengan int berupa angka
kunci = int(input('Masukkan jumlah kunci, misal (9): '))

# Berikut merupakan fungsi untuk mendekripsikan kata menggunakan variabel kata dan kunci serta loop 
def enkripsi(kata,kunci) :
  kata = kata.lower()
  hasil = ''
  for i in kata : # i merupakan karakter
    if i in abjad :
      j = abjad.index(i) # j merupakan index lama
      k = (j + kunci ) % len(abjad) # k merupakan index baru
      abjad_baru = abjad[k]
      hasil = hasil + abjad_baru 
    else:
       hasil = hasil + ' ' 
  return hasil
  
# Berikut untuk menginput kata yang akan dienkripsi
kata = input('Masukkan kata ')

# Output
kata_hasil = enkripsi(kata,kunci)
print('Kata yang dimasukkan adalah:',kata)
print('Hasil enkripsi kata dengan jumlah kunci:',kunci, 'adalah', kata_hasil)

# Menggunakan enkripsi ulang dengan selisih kunci)
kata_awal = enkripsi(kata_hasil,-kunci)
print('Hasil enkripsi ulang menggunakan nilai selisih dari jumlah kunci sebelumnya adalah:',-kunci, 'adalah', kata_awal)