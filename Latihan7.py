# Anggelina Kismasari 20051397034 2020MIB

class stack():
    def __init__(self):
        self.items = []

    def push(self, item): # Menambahkan item kedalam stack 
        self.items.append(item)

    def pop(self): # Menghapus item dalam stack
        return self.items.pop()

    def IsEmpty(self): # Memeriksa stack apakah kosong atau tidak
        return self.items == []

    def peek (self): # Mengembalikan top item dari stack tetapi tidak menghapusnya
        if not self.IsEmpty():
            return self.items[-1]

    def get_stack (self): # Memperoleh nilai dari setiap elemen yang terdapat dalam stack
        return self.items

def convert(stack, input_int):
    for i in range(len(input_int)):
        stack.push(input_int[i])

    rev_int = ""
    while not stack.IsEmpty():
        rev_int += stack.pop()

    return rev_int

stack = stack()
input_int = 50
des = input_int
bin = bin(des).replace("0b","")
oct = oct(des).replace("0o","")
hexa = hex(des).replace('0x',"")

print (f"Desimal : {des}")
print(f"Biner : {bin}")
print(f"Octal : {oct}")
print(f"Hexa  : {hexa}")