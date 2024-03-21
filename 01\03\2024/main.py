def cipher(text, shift):
    result = ''
    for i in range(len(text)):
        char = text[i]
        if not char.isalpha():
            result += char
            continue
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        else:
            result += chr((ord(char) + shift - 97) % 26 + 97)
    return result
        
def decipher(text, shift):
    return cipher(text, shift * -1)


def main():
    text = input("Enter text: ")
    shift = int(input("Enter shift: "))
    cipherMode = input("Enter mode (cipher/decipher): ") == "cipher"
    if cipherMode:
        print(cipher(text, shift))
    else:
        print(decipher(text, shift))
main()