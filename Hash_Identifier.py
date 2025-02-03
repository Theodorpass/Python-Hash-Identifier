import re

def identify_hash_type(hash_string):
    # Remove any spaces or unexpected characters
    hash_string = hash_string.strip()

    # Check for valid hexadecimal characters (0-9, a-f)
    if not re.match(r'^[0-9a-fA-F]+$', hash_string):
        return "Invalid hash: contains non-hexadecimal characters"

    # Length-based identification
    length = len(hash_string)

    # Hash Type Identification based on length and predefined conditions
    if length == 32:
        return "MD5"
    elif length == 40:
        return "SHA-1"
    elif length == 64:
        # Check for truncated SHA-512/256 (64 characters)
        if hash_string[:8] == "cf83e135":  # A pattern unique to SHA-512/256
            return "SHA-512/256"
        else:
            return "SHA-256"
    elif length == 56:
        return "SHA-224"
    elif length == 128:
        return "SHA-512"
    else:
        return "Unknown hash type"

def main():
    print("Hash Type Recognizer")
    print("=====================")
    
    while True:
        # Input the hash string
        hash_string = input("Enter hash to identify (or type 'exit' to quit): ").strip()

        if hash_string.lower() == 'exit':
            print("Exiting program.")
            break  # Exit the loop and terminate the program
        
        # Identify and output the hash type
        result = identify_hash_type(hash_string)
        print(f"Hash Type: {result}")

if __name__ == "__main__":
    main()
