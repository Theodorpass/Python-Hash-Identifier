# Python-Hash-Identifier

This Python script identifies various hash types (MD5, SHA-1, SHA-224, SHA-256, SHA-512, etc.) based on the input hash string. It supports a wide range of hash algorithms and provides easy-to-understand feedback for the user.

## Features

- Identifies MD5, SHA-1, SHA-224, SHA-256, SHA-512, and other common hash types.
- Provides user-friendly output with the hash type name.
- Handles input validation for hash format.

## Requirements

- Python 3.x
- No external libraries are required.

## Usage

1. Clone or download this repository to your local machine.

   ```bash
   git clone https://github.com/Theodorpass/hash-type-identifier.git
   ```

2. Navigate to the project directory.

   ```bash
   cd hash-type-identifier
   ```

3. Run the Python script.

   ```bash
   python hash_identifier.py
   ```

4. Enter the hash string when prompted to identify the hash type.

## Example Usage

```bash
Enter hash to identify (or type 'exit' to quit): 9e107d9d372bb6826bd81d3542a419d6
Hash Type: MD5

Enter hash to identify (or type 'exit' to quit): cf83e1357eefb8bdf1542850d66d8007d620e4dba5a5e3f091bb9b0adbe1fe083c4e9f8d5f6639d7b4709c9487d8ad4600ad1f011d255fb58e0f4416bcdef6237
Hash Type: SHA-512
```

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-name`).
3. Make changes and commit (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-name`).
5. Create a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
