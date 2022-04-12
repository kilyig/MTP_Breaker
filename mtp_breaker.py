from distutils.command.clean import clean
from operator import index
import string
from mtp_phrase_checker import MTPPhraseChecker
import argparse

CHARS = "abcdefghijklmnopqrstuvwxyz "

class MTP_Breaker():
    def __init__(self, chars=CHARS, words=[]):
        self.chars = chars
        self.words = words
        self.phrase_checker = MTPPhraseChecker(self.words)

    def possible_keys(self, chars, cipher):
        possible_keys = []
        for char in chars:
            possible_keys.append(ord(char) ^ cipher)
        return possible_keys

    def latest_prefix(self, text):
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

    def decrypt(ciphertext, key):
        pass

    def mtp_break(self, ciphertexts):
        ciphertext_count = len(ciphertexts)
        decrypted = [""] * ciphertext_count
        ctext_len = len(ciphertexts[0])
        indexes_in_possible_keys = [-1] * ctext_len
        keys = [-1] * ctext_len
        next_chars = [""] * ciphertext_count

        solution_count = 0
        solutions = []

        key_pos = 0
        while key_pos < ctext_len:
            a_key_worked = False
            pos_keys = self.possible_keys(self.chars, ciphertexts[0][key_pos]) # the previous pos_keys should be used when backtracking
            i = indexes_in_possible_keys[key_pos] + 1
            # try all the keys that can be the next
            while i < len(pos_keys):
                key_candidate = pos_keys[i]
                key_works = True
                # try each ciphertext and see if the new character added due to the key makes sense 
                for ctext in range(len(ciphertexts)):
                    curr_prefix = self.latest_prefix(decrypted[ctext])
                    next_chars[ctext] = chr(ciphertexts[ctext][key_pos] ^ key_candidate)
                    if next_chars[ctext] == ' ':
                        if not self.phrase_checker.is_valid_word(curr_prefix):
                            key_works = False
                            break
                    elif next_chars[ctext].isalpha():
                        if not self.phrase_checker.is_valid_prefix(curr_prefix + next_chars[ctext]):
                            key_works = False
                            break
                    else:
                        key_works = False
                        break
                # this key has worked
                if key_works:
                    a_key_worked = True
                    keys[key_pos] = key_candidate
                    indexes_in_possible_keys[key_pos] = i
                    # update the decrypted ciphertexts (append the new character)
                    for j in range(len(next_chars)):
                        decrypted[j] += next_chars[j]
                    break
                else:
                    i += 1
                    
            if a_key_worked:
                # check if you are done
                if key_pos == ctext_len - 1:
                    # we are at the end of the ciphertexts, so we found a valid solution
                    solutions.append(keys[:])
                    solution_count += 1
                    for j in range(len(next_chars)):
                        decrypted[j] = decrypted[j][:ctext_len-1]
                    keys[key_pos] = -1
                else:
                    key_pos += 1
            else:
                if key_pos == 0:
                    # end of solutions
                    return solutions
                else:
                    # dead end. a previous key was wrong.
                    indexes_in_possible_keys[key_pos] = -1
                    key_pos -= 1
                    keys[key_pos] = -1
                    # remove the last characters -- they correspond by the incorrect key
                    decrypted_len = len(decrypted[0])
                    for j in range(len(next_chars)):
                        decrypted[j] = decrypted[j][:decrypted_len-1]


if __name__ == "__main__":
                                                           
    print(f"""╔╦╗╔╦╗╔═╗  ╔╗ ╦═╗╔═╗╔═╗╦╔═╔═╗╦═╗
║║║ ║ ╠═╝  ╠╩╗╠╦╝║╣ ╠═╣╠╩╗║╣ ╠╦╝
╩ ╩ ╩ ╩    ╚═╝╩╚═╚═╝╩ ╩╩ ╩╚═╝╩╚═
@ 2022 Yiğit Kılıçoğlu. yigitkilicoglu.com.\n""")

    parser = argparse.ArgumentParser()
    parser.add_argument("-ch", "--characters", help="file containing the characters that allowed to be in the plaintext. all characters in the 1. line", required=False)
    parser.add_argument("-c", "--ciphertexts", help="file containing the ciphertexts. 1 ciphertext per line", required=True)
    parser.add_argument("-w", "--words", help="file containing the words that allowed to be in the plaintexts. 1 word per line", required=True)
    parser.add_argument("-o", "--output", help="output file", required=False)

    args = parser.parse_args()

    print("Character file:  ", args.characters)
    print("Word file:       ", args.words)
    print("Ciphertext file: ", args.ciphertexts)
    print("Output file:     ", args.output)
    print("Running...")

    # collect the ciphertexts
    ciphertexts = []
    with open(args.ciphertexts) as ciphertext_file:
        for line in ciphertext_file:
            ciphertext_ints = []
            clean = line.rstrip()
            for i in range(0, len(clean), 2):
                ciphertext_ints.append(int(clean[i:i+2], 16))
            ciphertexts.append(ciphertext_ints)


    # collect the allowed words
    allowed_words = []
    with open(args.words) as word_file:
        linenum = 0
        for line in word_file:
            linenum += 1
            cleaned = line.rstrip()
            allowed_words.append(cleaned)

    #collect the allowed characters
    chars = []
    if args.characters:
        with open(args.characters) as character_file:
            char_line = character_file.readline()
            chars = char_line.rstrip('\n')
    else:
        chars = CHARS

    # initialize the breaker and start breaking
    mtp_breaker = MTP_Breaker(chars, allowed_words)
    decryption_keys = mtp_breaker.mtp_break(ciphertexts)

    print()
    print("Number of solutions:", len(decryption_keys))

    if args.output:
        with open(args.output, "w") as output_file:
            decryption_count = 0
            for key in decryption_keys:
                decryption_count += 1
                output_file.write("Decryption " + str(decryption_count) + ":\n")
                output_file.write("Key: ")

                # print the key
                for key_char in key:
                    output_file.write(f'{key_char:02x}')
                output_file.write("\n")
                

                # print the decrypted plaintexts
                for i in range(len(ciphertexts)):
                    output_file.write("Plaintext " + str(i+1) + ": ")
                    for j in range(len(ciphertexts[i])):
                        output_file.write(chr(ciphertexts[i][j] ^ key[j]))
                    output_file.write("\n")



                output_file.write("\n")
        print("Solutions saved to " + args.output + ".")
