def get_ordered_columns(key):
    key_order = sorted([(char, i) for i, char in enumerate(key)])  # Sort key numerically
    return [i for _, i in key_order]  # Extract original indices in sorted order


def fill_grid(plain_text, key_length):
    grid = []
    for i in range(0, len(plain_text), key_length):
        row = list(plain_text[i:i + key_length])
        while len(row) < key_length:
            row.append('X')  # Padding with 'X'
        grid.append(row)
    return grid


def encrypt_columnar(plain_text, key):
    columns_order = get_ordered_columns(key)
    grid = fill_grid(plain_text, len(key))
    cipher_text = ""

    for index in columns_order:
        for row in grid:
            cipher_text += row[index]

    return cipher_text


plain_text = "HELLOWORLD"
key = "3215"
cipher = encrypt_columnar(plain_text, key)
print("Encrypted Text:", cipher)
