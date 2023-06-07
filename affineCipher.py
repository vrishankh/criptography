def affine_cipher_encrypt(plaintext, a, b):
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            if char.islower():
                ciphertext += chr((a * (ord(char) - ord('a')) + b) % 26 + ord('a'))
            else:
                ciphertext += chr((a * (ord(char) - ord('A')) + b) % 26 + ord('A'))
        else:
            ciphertext += char
    return ciphertext
def affine_cipher_decrypt(ciphertext, a, b):
    plaintext = ""
    a_inv = 0
    for i in range(26):
        if (a * i) % 26 == 1:
            a_inv = i
            break
    for char in ciphertext:
        if char.isalpha():
            if char.islower():
                plaintext += chr((a_inv * (ord(char) - ord('a') - b)) % 26 + ord('a'))
            else:
                plaintext += chr((a_inv * (ord(char) - ord('A') - b)) % 26 + ord('A'))
        else:
            plaintext += char
    return plaintext

plaintext = "Hello, World!"
a = 5
b = 8
ciphertext = affine_cipher_encrypt(plaintext, a, b)
print("Ciphertext:", ciphertext)
decrypted_text = affine_cipher_decrypt(ciphertext, a, b)
print("Decrypted text:", decrypted_text)
