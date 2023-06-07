def diffie_hellman(g, p, x, y):
    public_key_x = (g ** x) % p
    public_key_y = (g ** y) % p

    shared_key_x = (public_key_y ** x) % p
    shared_key_y = (public_key_x ** y) % p

    if shared_key_x == shared_key_y:
        return shared_key_x
    else:
        return None


# Sample input and output
g = 5
p = 23
x = 6
y = 15

symmetric_key = diffie_hellman(g, p, x, y)
print("Symmetric Key:", symmetric_key)
