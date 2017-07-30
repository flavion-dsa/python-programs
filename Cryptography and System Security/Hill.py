import numpy as np
import math

def modinv(a, m):
    for i in range(1, m):
        r = (i*a)%m
        if r == 1:
            break
    return i

def check_param(text, key):
    if len(key) * len(key) != sum([len(key[i]) for i in range(len(key))]):
        print("Error : matrix should be m x m")
        quit()
    elif len(text)%len(key) != 0:
        print("Error : length of text should be multiple of key")
        quit()
    try:
        np.linalg.inv(key)
    except Exception as e:
        print("Error : key non-invertible."+str(e))
        quit()

def key_inv(key):
    det = int(np.linalg.det(key))%26
    adj = (np.linalg.inv(key)*np.linalg.det(key))%26
    return (modinv(det, 26)*adj)%26

def encrpyt(text, key):
    check_param(text, key)
    cipher = ''
    key_len = len(key)
    key = np.array(key)
    arr = np.array([ord(i) - ord('a') for i in text])
    arr = np.reshape(arr, (-1, key_len))
    ans = []
    for row in arr:
        ans.append(np.dot(row, key)%26)
    for row in ans:
        for i in row:
            cipher += chr(int(i) + ord('a'))
    return "Cipher Text :"+cipher.upper()
        

def decrpyt(text, key):
    plain = ''
    text = text.lower()
    key_len = len(key)
    keyinv = key_inv(key)
    arr = np.array([ord(i) - ord('a') for i in text], dtype=int)
    arr = np.reshape(arr, (-1, key_len))
    ans = []
    for row in arr:
        ans.append(np.dot(row, keyinv)%26)
    for row in ans:
        for i in row:
            plain += chr(int(i) + ord('a'))
    return "Plain Text : "+plain

if __name__ == '__main__':
    print("===== HILL CIPHER =====")
    print("Enter key len:")
    n = int(input().strip())
    key = []
    print("Enter key:")
    for _ in range(n):
        key.append([int(i) for i in input().strip().split(' ')])
 
    print("Enter text :")
    text = str(input().strip())
    print("=======================")
    print("1. Encrypt\n2. Decrypt")
    choice = lambda x : encrpyt(text, key) if x == 1 else decrpyt(text, key)
    print(choice(int(input())))  
