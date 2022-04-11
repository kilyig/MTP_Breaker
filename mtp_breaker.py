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
        #print(ctext_len)


        solution_count = 0
        solutions = []

        key_pos = 0
        while key_pos < ctext_len:
            a_key_worked = False
            pos_keys = self.possible_keys(self.chars, ciphertexts[0][key_pos]) # the previous pos_keys should be used when backtracking
            #print(key_pos, pos_keys)
            i = indexes_in_possible_keys[key_pos] + 1
            while i < len(pos_keys):
                key_candidate = pos_keys[i]
                #print("Key candidate:", key_candidate)
                key_works = True
                for ctext in range(len(ciphertexts)):
                    curr_prefix = self.latest_prefix(decrypted[ctext])
                    next_chars[ctext] = chr(ciphertexts[ctext][key_pos] ^ key_candidate)
                    #print(next_chars[ctext])
                    if next_chars[ctext] == ' ':
                        if not self.phrase_checker.is_valid_word(curr_prefix):
                            key_works = False
                            break
                    elif next_chars[ctext].isalpha():
                        #print("Check:", curr_prefix + next_chars[ctext])
                        if not self.phrase_checker.is_valid_prefix(curr_prefix + next_chars[ctext]):
                            key_works = False
                            break
                    else:
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
                    
            if a_key_worked:
                # check if you are done
                if key_pos == ctext_len - 1:
                    #print("Found a valid solution.")
                    #print(keys)
                    solutions.append(keys[:])
                    #print("solutions:", solutions)
                    #print(decrypted)
                    solution_count += 1
                    for j in range(len(next_chars)):
                        decrypted[j] = decrypted[j][:ctext_len-1]
                    #print("After solution, decrypted:", decrypted)
                    keys[key_pos] = -1
                else:
                    key_pos += 1
            else:
                if key_pos == 0:
                    #print("End of solutions")
                    #print(solution_count)
                    #print("before returning:", solutions)
                    return solutions
                else:
                    #print("Dead end. a previous key was wrong.")
                    indexes_in_possible_keys[key_pos] = -1
                    key_pos -= 1
                    keys[key_pos] = -1
                    #print("removed incorrect key:", keys)
                    decrypted_len = len(decrypted[0])
                    for j in range(len(next_chars)):
                        decrypted[j] = decrypted[j][:decrypted_len-1]
                    #print("Removed last letters of decrypted:", decrypted)





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
            #print(ciphertext_ints)
            ciphertexts.append(ciphertext_ints)


    #ciphertext1 = [24, 57, 110, 178, 131, 253, 100, 139, 165, 37, 126, 203, 174, 19, 132, 229, 235, 36, 253, 213, 125, 94, 122, 217, 200, 119, 131, 200, 76, 185, 208, 71, 201, 158, 203, 11, 18, 40, 99, 22, 158, 21, 3, 166, 120, 7, 177, 157, 128, 102, 106, 208, 242, 152, 183, 189, 253, 90, 181, 46, 174, 69, 210, 169, 70, 70, 6, 43, 203, 253, 168, 159]
    #ciphertext2 = [1, 35, 114, 162, 141, 253, 97, 144, 184, 51, 118, 141, 173, 92, 140, 164, 239, 53, 241, 133, 108, 17, 97, 219, 193, 96, 131, 221, 86, 174, 145, 82, 136, 137, 211, 88, 29, 103, 101, 70, 154, 24, 4, 234, 126, 75, 172, 145, 138, 34, 40, 216, 239, 146, 228, 173, 177, 65, 178, 47, 235, 18, 205, 165, 77, 78, 73, 59, 153, 235, 184, 159]
    #ciphertext3 = [29, 41, 127, 165, 200, 170, 103, 141, 175, 32, 48, 134, 161, 16, 151, 229, 236, 48, 228, 205, 107, 19, 116, 219, 196, 102, 208, 156, 67, 176, 145, 88, 219, 196, 222, 66, 12, 38, 118, 82, 202, 3, 0, 166, 118, 7, 174, 157, 147, 108, 35, 217, 231, 217, 161, 184, 184, 64, 174, 37, 172, 69, 205, 161, 88, 82, 16, 124, 137, 235, 177, 133]



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















