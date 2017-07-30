import random

def encrypt(text):
    cipher = ''
    key = ''
    arr = [ord(i) - ord('a') for i in text]
    for num in arr:
        c = random.randint(0,25)
        cipher += chr((num + c)%26 + ord('a'))
        key += chr(c%26 + ord('a'))
    return cipher.upper(), key

def decrypt(text, key):
    plain = ''
    text = text.lower()
    arr = [ord(i) - ord('a') for i in text]
    arr_key = [ord(i) - ord('a') for i in key]
    for n, k in zip(arr, arr_key):
        plain += chr((n - k)%26 + ord('a'))
    return plain

if __name__ == '__main__':
    print("===== VERNAM CIPHER =====")
    print("1. Encrypt \n2. Decrypt")
    print("=========================")
    choice = int(input())
    if choice == 1:
        print("\nEnter plain text :")
        cipher, key = encrypt(input().strip())
        print("\nCipher : {}\nKey : {}".format(cipher, key))
    elif choice == 2:
        print("\nEnter cipher text :")
        ct = input()
        print("\nEnter key")
        print("\nPlain text : {}".format(decrypt(ct, input())))
    