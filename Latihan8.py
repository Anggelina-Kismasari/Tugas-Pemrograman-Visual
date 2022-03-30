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

def reverse_string(stack, input_str):
    for i in range(len(input_str)):
        stack.push(input_str[i])

    rev_str = ""
    while not stack.IsEmpty():
        rev_str += stack.pop()

    return rev_str

stack = stack()
input_str = "Saatnya tidur"
print("Kalimat awal : ",input_str)
print("Hasil: ",reverse_string(stack, input_str))