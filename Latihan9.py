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
        rev_str = input_str[::-1]
        if (rev_str == input_str):
            print ("Palindrom")
            break
        else :
            print ("Bukan palindrom!")
            break
    return rev_str


stack = stack()
input_str = "sugus"
print("Jika dibalik menjadi : ",reverse_string(stack, input_str))