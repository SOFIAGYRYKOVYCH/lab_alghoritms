bibl = dict()


def init():
    pass


def addBook(author, title):
    if author in bibl :
        if title not in bibl[author] :
            bibl[author].append(title)
    else :
        bibl[author] = list(title)
    
    


def find(author, title):
    if author in bibl :
        if title in bibl[author] :
            return True
    return False


def delete(author, title):
    if author in bibl :
        if title in bibl[author] :
            book = bibl[author]
            del book[book.index(title)]
    


def findByAuthor(author):
    if author in bibl :
        bibl[author].sort()
        return bibl[author]
    return []

