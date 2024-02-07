alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(plain_text, shift_amount):
    cipher_text = ""
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        cipher_text += alphabet[new_position]
    return cipher_text   # Return the encrypted text

def decrypt(cypher_text, shift_amount):
    plain_text = ""
    for letter in cypher_text:
        position = alphabet.index(letter)
        new_position = position - shift_amount
        plain_text += alphabet[new_position]
    return plain_text   # Return the decrypted text

if direction == "encode":
    encoded_text = encrypt(plain_text=text, shift_amount=shift)
    print(f"The encoded text is {encoded_text}")

elif direction == "decode":
    decoded_text = decrypt(cypher_text=text, shift_amount=shift);
    print(f"The decoded text is {decoded_text}")
