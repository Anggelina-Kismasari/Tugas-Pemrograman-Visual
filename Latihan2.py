# Anggelina Kismasari 20051397034 MI20B

# Berikut merupakan judul dari tabel perkalian
print ("Tabel Perkalian 1 hingga 10")
print ()

for i in range(1,11) : # i merupakan nilai yang akan dikalikan yakni dari 1 sampai 10
    print(i, end="\t")
print()
print("______________________________________")

for j in range(1,11) : # j merupakan nilai pada garis horizontal
    for k in range(1,11) : # k merupakan nilai pada garis vertikal
        print(j * k, end = "\t") # setiap nilai dari masing-masing garis dikalikan 
    print()