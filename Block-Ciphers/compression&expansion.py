def compress_6_to_4_bits(bits_6):
    if len(bits_6) != 6:
        raise ValueError("Input must be 6 bits long")

    compressed_4 = bits_6[:4]  # Take the first 4 bits
    return compressed_4


def expand_4_to_6_bits(bits_4):
    if len(bits_4) != 4:
        raise ValueError("Input must be 4 bits long")

    expanded_6 = bits_4 + '00'  # Add two extra bits (00) to the input
    return expanded_6


# usage:
original_6_bits = '110110'
compressed_4_bits = compress_6_to_4_bits(original_6_bits)
expanded_6_bits = expand_4_to_6_bits(compressed_4_bits)

print("Original 6 bits:", original_6_bits)
print("Compressed 4 bits:", compressed_4_bits)
print("Expanded 6 bits:", expanded_6_bits)