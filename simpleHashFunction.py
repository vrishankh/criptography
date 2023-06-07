def simple_hash(message):
    hash_value = sum(ord(char) for char in message)
    return hash_value


message = "Welcome Back Soldier"
original_hash = simple_hash(message)
print("Original Message:", message)
print("Original Hash:", original_hash)

changed_message = "Welcome Back, Soldier!"
changed_hash = simple_hash(changed_message)
print("Changed Message:", changed_message)
print("Changed Hash:", changed_hash)

if original_hash == changed_hash:
    print("Integrity: Matched!")
else:
    print("Integrity: Not Matched!")
