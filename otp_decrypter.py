from operator import index
from otp_phrase_checker import OTPPhraseChecker

chars = "abcdefghijklmnopqrstuvwxyz "

# key = [69, 103, 140, 108, 86, 107, 202, 219, 46, 124, 200]
# text1 = "canim benim"
# text2 = "meine katze"

ciphertext1 = [28, 9, 167, 202, 139, 232, 205, 169, 153, 20, 202]
ciphertext2 = [7, 13, 182, 202, 139, 232, 202, 169, 128, 12, 206]

ciphertexts = [ciphertext1, ciphertext2]

def possible_keys(chars, cipher):
    possible_keys = []
    for char in chars:
        possible_keys.append(ord(char) ^ cipher)
    return possible_keys

def latest_prefix(text):
    '''
    returns the substring that is between the last space character and the end of the string
    '''
    prefix = ""
    for char in reversed(text):
        if not char.isspace():
            prefix += char
        else:
            break
    return prefix[::-1]



# ciphertexts = [[ 38,   6, 226,   5,  59],
#                 [ 40,   2, 229,   2,  51]]

possible_words = ["canim", "hahah", "aslan", "askim", "kilic", "dener", "macun", "veron", "bavul", "lamba", "yigit", "benim", "kuzum", "apple", "meine", "katze"]
#possible_words = ["canim", "benim", "meine", "katze"]
checker = OTPPhraseChecker(possible_words)

decrypted = [""] * 2
ctext_len = len(ciphertexts[0])
indexes_in_possible_keys = [-1] * ctext_len
keys = [-1] * ctext_len
next_chars = [""] * 2
#print(ctext_len)


key_pos = 0
while key_pos < ctext_len:
    a_key_worked = False
    pos_keys = possible_keys(chars, ciphertexts[0][key_pos]) # the previous pos_keys should be used when backtracking
    #print(key_pos, pos_keys)
    i = indexes_in_possible_keys[key_pos] + 1
    while i < len(pos_keys):
        key_candidate = pos_keys[i]
        #print("Key candidate:", key_candidate)
        key_works = True
        for ctext in range(len(ciphertexts)):
            curr_prefix = latest_prefix(decrypted[ctext])
            next_chars[ctext] = chr(ciphertexts[ctext][key_pos] ^ key_candidate)
            #print(next_chars[ctext])
            if next_chars[ctext] == ' ':
                if not checker.is_valid_word(curr_prefix):
                    key_works = False
                    break
            else:
                if not checker.is_valid_prefix(curr_prefix + next_chars[ctext]):
                    key_works = False
                    break
        if key_works:
            #print("Key candidate worked:", key_candidate)
            a_key_worked = True
            keys[key_pos] = key_candidate
            #print(keys)
            indexes_in_possible_keys[key_pos] = i
            # update the decrypted ciphertexts
            for j in range(len(next_chars)):
                decrypted[j] += next_chars[j]
            #print("Current decrypted:", decrypted)
            break
        else:
            i += 1
    if not a_key_worked:
        if key_pos == 0:
            print("End of solutions")
            break
        elif key_pos != ctext_len:
            #print("Dead end. a previous key was wrong.")
            indexes_in_possible_keys[key_pos] = -1
            key_pos -= 1
            keys[key_pos] = -1
            #print("removed incorrect key:", keys)
            decrypted_len = len(decrypted[0])
            for j in range(len(next_chars)):
                decrypted[j] = decrypted[j][:decrypted_len-1]
            #print("Removed last letters of decrypted:", decrypted)
        else:
            print("Finished")
            break

            
        # then, find the right i to continue with. if you start from i = 0 again with key_pos - 1, you will end up in a loop
    else:
        # check if you are done
        if key_pos == ctext_len - 1:
            #print("Found a valid solution.")
            print(keys)
            print(decrypted)
            for j in range(len(next_chars)):
                decrypted[j] = decrypted[j][:ctext_len-1]
            #print("After solution, decrypted:", decrypted)
            keys[key_pos] = -1
        else:
            key_pos += 1

# print(keys)
# print(decrypted)






# thanks to Veronika for the German translation!! :)
# https://www.w3resource.com/python/python-bytes.php