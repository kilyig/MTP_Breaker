from textwrap import shorten
import numpy as np

np.set_printoptions(formatter={'int':hex})

text1 = "quick brown fox jumps over the lazy dog table road grass tree window sun"
text2 = "house giraffe panda bottle array mask apple clock book cloud wheel green"
text3 = "text water milk mathematics glass lizard walk morning evening happy belt"

key = '694c07d1e8dd06f9ca5210ebc87cfcc5815190a50e7e15afad05a3bc24dcf02ba8e4b22b76470436ea7461ca1d27c3f2e1024ab780f9c4cedd2ec74bcb65a5c02822695ceb8eddf1fbd170a514f3b3c81b9b1dc91210028b7087f24c7f8e443bb5a4d42aabc944feeec92f3aef1192cfee4f3e66a212a347099eeae060cd18cb175f28b3d98538bed69cc1833dbd70fe28f13acb543310d9d36598e1321218e454323611955f20a43aeb95c9d38e75b7440a4e97f131e7f8cd49d2f455fba403501bab58af5811993461578e0f1dfbacda49925de0ca9aa298fd82a1eeacffee99e10cb175b583e06dd3a807c6984301f4654ce6be825405772aa08f85f00a3d7e43ace9a4777ce30b78a1a8cfea3a8d13ef054e84b294503205529d7f7294b4581860e2672ca4cb2151e72da0287499d02a6c770bc551148266a0711534ccd8fc43e187b181590a7a8eea342f0907d90d8237a5c20f0bb714a51fe645fd468a8d9d3917cf526ec4738dcacfd26881c2a7544373d96ba141b17954318ce1656d06f1fe851bfbcabe55ae8c09e7facb021e40412b854952785aaffef00098fd3cee6854667115498843e4125e1fc8b8c977dd457766173e434215c858d20c1e4ab979fb4a8414cadf4a89bd871a088f1f073da8ef50446467a450f5785b238db1414cd8e4442d3def1f46695732299b676cb3a7ef56168c678f2441fba4f621b6cae199507bb8eb9c0e12fca54a628e13c637704f91928fbd02f28f2845b04af334f5ee81d64ff5ff0c157c7bde9c83a8529b759dd90c90114785b0'
messages = [text1, text2, text3]


ciphertexts = []
for message in messages:
    shortened_key = key[:2*len(message)]
    key_bytes = list(bytes.fromhex(shortened_key))
    message_bytes = list(message.encode("ascii"))
    ciphertexts.append(np.bitwise_xor(key_bytes, message_bytes))

#print(key_bytes)

for i in range(len(messages)):
    print(messages[i])
    print(ciphertexts[i].tolist())
    for char in ciphertexts[i].tolist():
        print(f'{char:02x}', end='')
    print()



