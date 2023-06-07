def extended_euclidean_algorithm(a, b):
    if b == 0:
        return a, 1, 0
    else:
        gcd, x, y = extended_euclidean_algorithm(b, a % b)
        return gcd, y, x - (a // b) * y


# Sample input and output
a = 48
b = 18

gcd, x, y = extended_euclidean_algorithm(a, b)
print("GCD:", gcd)
print("x:", x)
print("y:", y)
