encry_category = {
    'a': '1', 'b': '2', 'c': '3', 'd': '4', 'e': '5', 'f': '6', 'g': '7', 'h': '8', 'i': '9', 'j': '10',
    'k': '11', 'l': '12', 'm': '13', 'n': '14', 'o': '15', 'p': '16', 'q': '17', 'r': '18', 's': '19',
    't': '20', 'u': '21', 'v': '22', 'w': '23', 'x': '24', 'y': '25', 'z': '26'
}

decry_category = {
    '1': 'a', '2': 'b', '3': 'c', '4': 'd', '5': 'e', '6': 'f', '7': 'g', '8': 'h', '9': 'i', '10': 'j',
    '11': 'k', '12': 'l', '13': 'm', '14': 'n', '15': 'o', '16': 'p', '17': 'q', '18': 'r', '19': 's',
    '20': 't', '21': 'u', '22': 'v', '23': 'w', '24': 'x', '25': 'y', '26': 'z'
}

while True:
    print("Welcome to NumCraX App!")
    print("1. Encryption")
    print("2. Decryption")
    print("3. About NumCraX")
    print("4. Exit")
    main_choice = input("Enter Your Choice (1-4): ")
    
    if main_choice == '1':
        print("=" * 15)
        print("# Encryption!")
        result = []
        plain_text = input("Enter Your Plain Text: ").lower()
        
        for char in plain_text:
            if char in encry_category:
                result.append(encry_category[char])
            elif char == " ":
                result.append("/")  # Space becomes '/'
            elif char == "\n":
                result.append("//")  # New line becomes '//'
            else:
                result.append(char)  # Keep symbols unchanged
        
        encrypted_text = "-".join(result)
        encrypted_text = encrypted_text.replace("-/-", " / ").replace("-//-", " // ")
        
        print(f"Original text: '{plain_text}'")
        print(f"Encrypted text: '{encrypted_text}'")
        print("=" * 15)
        
    elif main_choice == '2':
        print("=" * 15)
        print("# Decryption!")
        result = []
        encrypted_text = input("Enter Your Encrypted Text With '-': ")
        
        parts = encrypted_text.split(" ")  # Split by space to detect '/' and '//'
        
        for part in parts:
            if part == "/":
                result.append(" ")  # '/' becomes space
            elif part == "//":
                result.append("\n")  # '//' becomes new line
            else:
                numbers = part.split("-")
                for num in numbers:
                    if num in decry_category:
                        result.append(decry_category[num])
                    else:
                        result.append(num)  # Keep symbols unchanged
        
        decrypted_text = "".join(result).upper()
        
        print(f"Original text: '{encrypted_text}'")
        print(f"Decrypted text: '{decrypted_text}'")
        print("=" * 15)
        
    elif main_choice == '3':
        print("=" * 15)       
        print("# About NumCraX!")
        print("""Numcrypt is a simple encryption language that converts letters into numbers based on their alphabetical order (A=1, B=2, ..., Z=26).
Letters are separated by "-", sentences by "/", new lines by "//", and the encryption ends with "".
Symbols and punctuation remain unchanged, and decrypted text appears in CAPITAL LETTERS.

Example:
HELLO WORLD → 8-5-12-12-15 / 23-15-18-12-4.""")
        print("=" * 15)
        
    elif main_choice == '4':
        print("Logging out...")
        break
    else:
        print("Invalid Choice! Please choose a number between 1 and 4 only...")
