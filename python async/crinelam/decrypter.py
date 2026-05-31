'''
Copyright 2026 crinelam

 This program is free software: you can redistribute it and/or modify it
under the terms of the GNU General Public License as published by the
Free Software Foundation, either version 3 of the License, or (at your option)
any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY
WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with
this program. If not, see <https://www.gnu.org/licenses/>.
'''
import string
import argparse

ALPHABET_LOWER = string.ascii_lowercase
ALPHABET_UPPER = string.ascii_uppercase
INVERTED_LOWER = ALPHABET_LOWER[::-1]
INVERTED_UPPER = ALPHABET_UPPER[::-1]

ALPHABET_LENGTH = len(ALPHABET_LOWER)


def is_int(val):
    '''checks if a str is an int.'''
    try:
        int(val)
        return True
    except ValueError:
        return False


def decrypt_caesar(message, key):
    '''decrypts a caesar message with the given key.'''
    decrypted_message = ""
    for c in message:
        if c in ALPHABET_LOWER:
            position = ALPHABET_LOWER.find(c)
            new_position = (position - key) % ALPHABET_LENGTH
            new_character = ALPHABET_LOWER[new_position]
            decrypted_message += new_character
        elif c in ALPHABET_UPPER:
            position = ALPHABET_UPPER.find(c)
            new_position = (position - key) % ALPHABET_LENGTH
            new_character = ALPHABET_UPPER[new_position]
            decrypted_message += new_character
        else:
            decrypted_message += c
    return decrypted_message


def decrypt_atbash(message):
    '''decrypts an atbash message.'''
    decrypted_message = ""
    for c in message:
        if c in ALPHABET_LOWER:
            position = ALPHABET_LOWER.find(c)
            new_character = INVERTED_LOWER[position]
            decrypted_message += new_character
        elif c in ALPHABET_UPPER:
            position = ALPHABET_UPPER.find(c)
            new_character = INVERTED_UPPER[position]
            decrypted_message += new_character
        else:
            decrypted_message += c
    return decrypted_message


def generate_key(message, key):
    '''Generates a vigenere key with the length of the message(minus puntuations and spaces).'''
    key = list(key.lower())
    j = 0
    for i in range(len(message) - len(key)):
        if message[i].lower() in ALPHABET_LOWER:
            key.append(key[j % len(key)])
            j += 1
    return "".join(key)


def decrypt_vigenere(message, key):
    '''decrypts an vigenere message with the given key.'''
    decrypted_message = ""
    key = generate_key(message, key)
    i = 0
    for c in message:
        if c in ALPHABET_LOWER:
            position = ALPHABET_LOWER.find(c)
            key_position = ALPHABET_LOWER.find(key[i])
            new_position = (position - key_position) % ALPHABET_LENGTH
            new_character = ALPHABET_LOWER[new_position]
            decrypted_message += new_character
            i += 1
        elif c in ALPHABET_UPPER:
            position = ALPHABET_UPPER.find(c)
            key_position = ALPHABET_LOWER.find(key[i])
            new_position = (position - key_position) % ALPHABET_LENGTH
            new_character = ALPHABET_UPPER[new_position]
            decrypted_message += new_character
            i += 1
        else:
            decrypted_message += c
    return decrypted_message


def encrypt_vigenere(message, key):
    '''encrypts an vigenere message with the given key.'''
    encrypted_message = ""
    key = generate_key(message, key)
    i = 0
    for c in message:
        if c in ALPHABET_LOWER:
            position = ALPHABET_LOWER.find(c)
            key_position = ALPHABET_LOWER.find(key[i])
            new_position = (position + key_position) % ALPHABET_LENGTH
            new_character = ALPHABET_LOWER[new_position]
            encrypted_message += new_character
            i += 1
        elif c in ALPHABET_UPPER:
            position = ALPHABET_UPPER.find(c)
            key_position = ALPHABET_LOWER.find(key[i])
            new_position = (position + key_position) % ALPHABET_LENGTH
            new_character = ALPHABET_UPPER[new_position]
            encrypted_message += new_character
            i += 1
        else:
            encrypted_message += c
    return encrypted_message


def __main__():
    '''Main method.'''
    parser = argparse.ArgumentParser(
        prog="decrypter",
        description="decrypts some simple codes")
    parser.add_argument("code", help="kind of code to use",
                        choices=["caesar", "atbash", "vigenere",
                                 "vigenerencrypt"])
    parser.add_argument("message", help="message to decrypt")
    parser.add_argument("key",
                        help="the key to use, you can use 'force' in some cases to try to brute force it.")
    args = parser.parse_args()
    if args.code == "caesar":
        if args.key == "force":
            for i in range(0, ALPHABET_LENGTH-1):
                result = decrypt_caesar(args.message, i)
                print("Result with key " + str(i) + ":" + result)
                print()
        elif (is_int(args.key) and int(args.key) >= -ALPHABET_LENGTH
              and int(args.key) <= ALPHABET_LENGTH):
            result = decrypt_caesar(args.message, int(args.key))
            print("Result: " + result)
            print()
        else:
            print("Not a valid key, it must be an integer between " +
                  str(-ALPHABET_LENGTH) + " and " +
                  str(ALPHABET_LENGTH))
            print()
    elif args.code == "atbash":
        result = decrypt_atbash(args.message)
        print("Result: " + result)
        print()
    elif args.code == "vigenere":
        result = decrypt_vigenere(args.message, args.key)
        print(result)
        print()
    elif args.code == "vigenerencrypt":
        result = encrypt_vigenere(args.message, args.key)
        print(result)
        print()


__main__()
