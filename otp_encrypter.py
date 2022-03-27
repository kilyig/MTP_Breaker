from textwrap import shorten
import numpy as np

np.set_printoptions(formatter={'int':hex})

text1 = "cat caravan"
text2 = "veron katze"

key = '7168c4abe5c8a1c8f476abec54b8c8bf2f0e5020e5ae1aeaa7b'
messages = [text1, text2]


ciphertexts = []
for message in messages:
    shortened_key = key[:2*len(text1)]
    key_bytes = list(bytes.fromhex(shortened_key))
    message_bytes = list(message.encode("ascii"))
    ciphertexts.append(np.bitwise_xor(key_bytes, message_bytes))

print(key_bytes)
print(text1, ciphertexts[0].tolist())
print(text2, ciphertexts[1].tolist())

