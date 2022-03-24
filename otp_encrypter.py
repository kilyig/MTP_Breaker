import numpy as np

text1 = "canim benim"
text2 = "meine katze"

key = '45678c6c566bcadb2e7cc8'
messages = [text1, text2]

ciphertexts = []
for message in messages:
    key_bytes = list(bytes.fromhex(key))
    message_bytes = list(message.encode("ascii"))
    ciphertexts.append(np.bitwise_xor(key_bytes, message_bytes))

print(key_bytes)
print(ciphertexts)
