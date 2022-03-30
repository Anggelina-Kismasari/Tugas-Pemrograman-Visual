# Anggelina Kismasari 20051397034 2020MIB

class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self): # Memeriksa stack apakah kosong atau tidak
        return self.items == []

    def push(self, items): # Menambahkan item kedalam stack
        self.items.append(items)
 
    def pop(self): # Menghapus item dalam stack
        return self.items.pop()

    def peek(self): # Mengembalikan top item dari stack tetapi tidak menghapusnya
        return self.items[len(self.items)-1]

def infixToPostfix(infixexpr):
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    opStack = Stack()
    postfixList = []
    tokenList = infixexpr.split()

    for token in tokenList:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfixList.append(token)
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            topToken = opStack.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opStack.pop()
        else:
            while (not opStack.isEmpty()) and \
               (prec[opStack.peek()] >= prec[token]):
                  postfixList.append(opStack.pop())
            opStack.push(token)

    while not opStack.isEmpty():
        postfixList.append(opStack.pop())
    return " ".join(postfixList)

print("Infix  = 5 * ( 4 - 2 )")
print("Posfix =",infixToPostfix("5 * ( 4 - 2 )"))