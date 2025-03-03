import struct

def decrypt(v, k):
    v0, v1 = v[0], v[1]
    delta = 0x9E3779B9
    sum_ = 0xC6EF3720
    k0, k1, k2, k3 = k[0], k[1], k[2], k[3]
    for _ in range(32):
        v1 = (v1 - (((v0 << 4) + k2) ^ (v0 + sum_) ^ ((v0 >> 5) + k3))) & 0xFFFFFFFF
        v0 = (v0 - (((v1 << 4) + k0) ^ (v1 + sum_) ^ ((v1 >> 5) + k1))) & 0xFFFFFFFF
        sum_ = (sum_ - delta) & 0xFFFFFFFF
    return [v0, v1]

hex_words = [
    "E3238557", "6204A1F8", "E6537611", "174E5747",
    "5D954DA8", "8C2DFE97", "2911CB4C", "2CB7C66B",
    "E7F185A0", "C7E3FA40", "42419867", "374044DF",
    "2519F07D", "5A0C24D4", "F4A960C5", "31159418",
    "F2768EC7", "AEAF14CF", "071B2C95", "C9F22699",
    "FFB06F41", "2AC90051", "A53F035D", "830601A7",
    "EB475702", "183BAA6F", "12626744", "9B75A72F",
    "8DBFBFEC", "73C1A46E", "FFB06F41", "2AC90051",
    "97C5E4E9", "B1C26A21", "DD4A3463", "6B71162F",
    "8C075668", "7975D565", "6D95A700", "7272E637"
]

# Convert hex strings to a list of integers
enc_words = [int(x, 16) for x in hex_words]

key = [0, 4, 5, 1]

plain_bytes = b""
# Use little-endian when packing 32-bit words
for i in range(0, len(enc_words), 2):
    block = [enc_words[i], enc_words[i+1]]
    decrypted = decrypt(block, key)
    plain_bytes += struct.pack("<2I", decrypted[0], decrypted[1])

# Try to interpret the resulting bytes as a sequence of 16-bit words (UTF-16LE)
if len(plain_bytes) % 2 == 0:
    try:
        text = plain_bytes.decode("utf-16le")
        # Replace non-printable characters with spaces
        text = ''.join(c if c.isprintable() else ' ' for c in text)
    except UnicodeDecodeError as e:
        text = f"UTF-16LE decoding error: {e}"
else:
    text = plain_bytes.hex()

print("Decrypted message (UTF-16LE):")
print(text)