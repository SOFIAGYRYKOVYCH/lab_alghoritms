
class Values:
    def __init__(self, key: int, value):
        self.key = key
        self.value = value
        self.next = None
        self.valid = True

class HashTable:
    Tablesize = 6000
    def __init__(self):
        self.cells = [None] * HashTable.Tablesize

    @staticmethod
    def hash(key: int) -> int: # повертає хеш для ключа
        hsum = 0
        X = 31
        Y = 5987
        for i in range(len(key)):
            hsum = hsum * X + ord(key[i])
        return hsum % Y
        return key % HashTable.Tablesize

    def put(self, key, value): # додаємо ключ - значення до таблиці
        hkey = HashTable.hash(key)  
        cell = self.cells[hkey]     # визначаємо слот
        while cell != None:
            if cell.key == key:      
                cell.value.add(value)  
                cell.valid = True
                return  
            cell = cell.next  
        cell = Values(key, {value})
        cell.next = self.cells[hkey]
        self.cells[hkey] = cell

    def change(self, key, value):
        hkey = HashTable.hash(key)
        cell = self.cells[hkey]
        while cell != None:
            if cell.key == key:
                cell.value = value
                cell.valid = True
                return
            cell = cell.next

    def get(self, key): #повертає значення key
        hkey = HashTable.hash(key)
        cell = self.cells[hkey]      
        while cell != None:
            if cell.key == key:    
                return cell.value  
            cell = cell.next       
        return None

def init():
    global obj
    obj = HashTable()

def addBook(author, title):
    global obj
    obj.put(author, title)

def find(author, title):
    global obj
    el = obj.get(author)
    if el == None:
        return False
    else:
        if title in el:
            return True
        return False

def delete(author, title):
    global obj
    el = obj.get(author)
    if title in el:
        el.remove(title)
        obj.change(author, el)

def findByAuthor(author):
    global obj
    el = obj.get(author)
    if el == None:
        return []
    return el

