![MTP Breaker Logo](./mtpbreaker_logo.png "MTP Breaker Logo")

# Multiple-Time Pad Breaker
Reveals messages that were encrypted using the one-time pad scheme with the same key. 

Other MTP breaker programs on GitHub use the decryption technique explanied [here](https://www.thecrowned.org/the-one-time-pad-and-the-many-time-pad-vulnerability). This technique works when there are many ciphertexts and space characters in the plaintexts do not align. Also, in most cases, this technique offers partial decryption only. Thus, another program is needed to fill in the gaps.

OTP Breaker approaches the problem from a different angle. Rather than treating the ciphertexts as a list of characters and trying to find certain characters inside them, OTP Breaker assumes that the ciphertexts follow a certain structure, like sentences in a language do, and tries to build meaningful plaintexts from the ciphertexts.

Inputs:
* a set of `N` (>1) ciphertexts.
* a list of characters that the ciphertexts can contain. The default is `abcdefghijklmnopqrstuvwxyz `.
* a list of words (i.e. non-space character sequences delimited by space (` `) characters) that the plaintexts are allowed to contain.

Output:
* a list of `N`-tuples each of which contain a valid decryption of the ciphertexts.

 the ciphertexts follow a certain structure, like having a space character between words. 


## Usage

```
$ python mtp_breaker.py -h
usage: mtp_breaker.py [-h] [-ch CHARACTERS] -c CIPHERTEXTS -w WORDS [-o OUTPUT]

optional arguments:
  -h, --help            show this help message and exit
  -ch CHARACTERS, --characters CHARACTERS
                        file containing the characters that allowed to be in the plaintext. all
                        characters in the 1. line
  -c CIPHERTEXTS, --ciphertexts CIPHERTEXTS
                        file containing the ciphertexts. 1 ciphertext per line
  -w WORDS, --words WORDS
                        file containing the words that allowed to be in the plaintexts. 1 word per line
  -o OUTPUT, --output OUTPUT
                        output file
```

## Checklist

### Code
- [x] Break with 2 encryptions
- [x] Break with >2 encryptions
- [x] Take long word lists as input
- [x] Accept non-alphabetic and/or incomplete endings
- [x] Output keys that work
- [x] Terminate gracefully if no solution was found
- [ ] Accept numbers in the plaintext
- [ ] Accept punctuation in the plaintext
- [ ] Handle ciphertexts of different lengths
- [ ] More efficient trie traversal algorithm
- [ ] Testing suite


### User Interactions
- [x] Logo
- [x] CLI
- [x] Stats
- [x] Read ciphertexts from file
- [x] Write keys and plaintexts to file
- [ ] Progress bar
- [ ] Ciphertext format warnings
    - [ ] Partial one-time pad
- [ ] Turkish README.md


# Acknowledgements
The current code uses a Trie from [Tutorialspoint](https://www.tutorialspoint.com/implement-trie-prefix-tree-in-python).

For the logo, the template called "Blue and Red Shop Free Delivery Shadow Text Effect" by "Canva Creative Studio" was used.

CLI logo made at [patorjk.com](http://www.patorjk.com/software/taag/). Font: Calvin S.