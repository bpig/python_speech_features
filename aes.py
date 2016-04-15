# -*- encoding: utf-8 -*-

import base64
from Crypto import Random
from Crypto.Cipher import AES

BS = 16
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
unpad = lambda s: s[0:-ord(s[-1])]

class AESCipher:
    def __init__(self, key):
        self.key = key

    def encrypt(self, raw):
        raw = pad(raw)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return base64.b64encode(iv + cipher.encrypt(raw))

    def decrypt(self, enc):
        enc = base64.b64decode(enc)
        cipher = AES.new(self.key, AES.MODE_ECB)
        return unpad(cipher.decrypt(enc))

if __name__ == '__main__':
    cipher = AESCipher('9c3587389ee2cb39b3b0a711c45466ae')
    print cipher.decrypt("mvDj7yEU5f65Y0Ua+tQYcXBWCkW3HdDlBF3HRAUXMs1Zo1vGSJ+XHhI20+iftTiA")
