import numpy as np

def keyToOrder(key):
    order = []
    key = list(key)
    sorted_key = sorted(key)
    for ch in key:
        order.append(sorted_key.index(ch))
    return order

def encrypt(text, key):
    cipher = ''
    key_len = len(key)
    key_order = keyToOrder(key)
    text = text.lower()
    for _ in range(int(key_len - len(text)%key_len)):
        text += 'x'
    arr = [i for i in text]
    arr = np.reshape(arr, (-1, key_len))
    for i in key_order:
        cipher += ''.join(map(str, arr[:, int(i)]))
        cipher += ' '
    return "Cipher Text : "+cipher.upper()

def decrypt(text, key):
    plain = ''
    key_len = len(key)
    key_order = keyToOrder(key)
    key_order = np.argsort(key_order)
    text = text.lower()
    arr = [i for i in text]
    arr = np.reshape(arr, (key_len, -1))
    arr = np.transpose(arr)
    arr = arr[:, key_order]
    for row in arr:
        plain += ''.join(map(str, row))
    return "Plain Text : "+plain.lower()

if __name__ == '__main__':
    print("====== SINGLE COLUMNAR TRANSPOSITION ======")
    print("Enter text : ")
    text = input().strip().replace(' ', '')
    print("Enter key : ")
    key = input().strip()
    print("\n1. Encrypt \n2. Decrypt")
    print("===========================================")
    choice = lambda x : encrypt(text, key) if x == 1 else decrypt(text, key)
    print(choice(int(input())))