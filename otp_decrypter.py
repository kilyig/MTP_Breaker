from otp_phrase_checker import OTPPhraseChecker

chars = "abcdefghijklmnopqrstuvwxyz "


# text1 = "canim benim"
# text2 = "meine katze"
# ciphertexts = [[ 38,   6, 226,   5,  59,  75, 168, 190,  64,  21, 165],
#                 [ 40,   2, 229,   2,  51,  75, 161, 186,  90,   6, 173]]

def possible_keys(chars, cipher):
    possible_keys = []
    for char in chars:
        possible_keys.append(ord(char) ^ cipher)
    return possible_keys


ciphertexts = [[ 38,   6, 226,   5,  59],
                [ 40,   2, 229,   2,  51]]

possible_words = ["canim", "hahah", "yigit", "benim", "kuzum", "apple", "meine", "katze"]
checker = OTPPhraseChecker(possible_words)

keys = []
decrypted = [""] * 2
ctext_len = len(ciphertexts[0])
next_chars = [""] * 2
print(ctext_len)
for key_pos in range(ctext_len):
    a_key_worked = False
    for key in possible_keys(chars, ciphertexts[0][key_pos]):
        key_works = True
        for ctext in range(len(ciphertexts)):
            curr_prefix = decrypted[ctext][:key_pos+1]
            next_chars[ctext] = chr(ciphertexts[ctext][key_pos] ^ key)
            print(next_chars[ctext])
            if not checker.is_valid_prefix(curr_prefix + next_chars[ctext]):
                key_works = False
                break
        if key_works:
            a_key_worked = True
            keys.append(key)
            # update the decrypted ciphertexts
            for i in range(len(next_chars)):
                decrypted[i] += next_chars[i]
            break
    if not a_key_worked:
        print("The end")
        break

print(keys)
print(decrypted)






# thanks to Veronika for the German translation!! :)
# https://www.w3resource.com/python/python-bytes.php