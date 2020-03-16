M = 9999991
N = 1


def hash_func(n):
    return n % M


def init():
    global keys, values
    keys = [None for i in range(M)]
    values = [None for i in range(M)]

    with open("input.txt") as file:
        for line in file:
            pair = line.strip().split('=')
            key_file, value = int(pair[0]), pair[1]
            key = hash_func(key_file)
            # keys[key] = key_file
            values[key] = value


def set(key: int, value: str) -> None:
    """ Встановлює значення value для ключа key.
    Якщо такий ключ відсутній у структурі - додає пару, інакше змінює значення для цього ключа.
    :param key: Ключ
    :param value: Значення
    """
    global values
    key = hash_func(key)
    values[key] = value


def get(key: int):
    """ За ключем key повертає значення зі структури.
    :param key: Ключ
    :return: Значення, що відповідає заданому ключу або None, якщо ключ відсутній у структурі.
    """
    global values
    key = hash_func(key)
    try:
        return values[key]
    except KeyError:
        return None


def delete(key: int) -> None:
    """ Видаляє пару ключ-значення за заданим ключем.
    Якщо ключ у структурі відсутній - нічого не робить.
    :param key: Ключ
    """
    global values
    key = hash_func(key)
    values[key] = None
