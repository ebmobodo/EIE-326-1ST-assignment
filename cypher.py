message = input("Enter your message: ")
shift = int(input("Enter shift number: "))
encrypted_message = ""

for letter in message:
    if letter.isalpha():
        # Shift letter
        shifted = ord(letter) + shift

        # Handle lowercase letters
        if letter.islower():
            if shifted > ord('z'):
                shifted -= 26
            encrypted_message += chr(shifted)
        # Handle uppercase letters
        elif letter.isupper():
            if shifted > ord('Z'):
                shifted -= 26
            encrypted_message += chr(shifted)
    else:
        # Leave non-letters unchanged
        encrypted_message += letter

print("Encrypted message:", encrypted_message)