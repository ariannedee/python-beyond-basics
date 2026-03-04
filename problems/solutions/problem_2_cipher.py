"""
Caesar cipher encoder
"""

from pprint import pprint


def build_cipher_map(shift: int) -> dict[str, str]:
    """Create a dictionary, mapping each letter to
    the letter shifted by the given amount.
    e.g. shift=1: a->b, b->c, c->d, etc.
    e.g. shift=-1: a->z, b->a, c->b, etc.
    e.g. shift=28: a->c, b->d, c->e, etc.
    """
    cipher_map = {}
    letters = "abcdefghijklmnopqrstuvwxyz"
    for i, letter in enumerate(letters):
        new_i = (i + shift) % 26
        cipher_map[letter] = letters[new_i]
    return cipher_map

def encrypt(message: str, shift: int) -> str:
    cipher_map = build_cipher_map(shift)
    encrypted_message = ""
    for char in message.lower():
        encrypted_letter = cipher_map.get(char, char)
        encrypted_message += encrypted_letter
    return encrypted_message

def main():
    while True:
        try:
            shift = int(input("Shift: "))
            break
        except ValueError:
            print("  Invalid value")
    message = input("Message: ")
    print(encrypt(message, shift))

if __name__ == "__main__":
    main()