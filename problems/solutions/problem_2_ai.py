"""
Simple Caesar cipher encoder.

This module provides a small, readable implementation of a Caesar cipher,
designed to be easy for a junior Python developer to understand.
"""


def build_cipher_map(shift: int) -> dict[str, str]:
    """Return a mapping from each lowercase letter to its shifted letter."""
    letters = "abcdefghijklmnopqrstuvwxyz"
    cipher_map: dict[str, str] = {}

    for index, letter in enumerate(letters):
        shifted_index = (index + shift) % len(letters)
        cipher_map[letter] = letters[shifted_index]

    return cipher_map


def encrypt(message: str, shift: int) -> str:
    """
    Return the message encoded with a Caesar cipher.

    The function:
    - converts the message to lowercase,
    - shifts letters a–z by the given amount,
    - leaves all other characters (spaces, punctuation, digits) unchanged.
    """
    cipher_map = build_cipher_map(shift)
    encrypted_chars: list[str] = []

    for char in message.lower():
        encrypted_chars.append(cipher_map.get(char, char))

    return "".join(encrypted_chars)


if __name__ == "__main__":
    example_message = "Hello, World!"
    shift_amount = 3

    encoded_message = encrypt(example_message, shift_amount)

    print(f"Original message: {example_message}")
    print(f"Shift amount: {shift_amount}")
    print(f"Encoded message: {encoded_message}")