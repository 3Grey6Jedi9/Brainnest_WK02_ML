import string
import datetime


class Caesar_Cipher():

    british_alphabet = list(string.ascii_uppercase)

    def __init__(self, key):
        self.key = key

    def host(self):
        current_time = datetime.datetime.now()
        moment = ''
        if  6 <= current_time.hour and current_time.hour < 12:
            moment = 'morning'
        elif 12 <= current_time.hour and current_time.hour < 18:
            moment = 'afternoon'
        elif 18 <= current_time.hour and current_time.hour < 22:
            moment = 'evening'
        elif  22 <= current_time.hour and current_time.hour < 6:
            moment = 'night'
        return f'''Good {moment}, I will help you encrypting or decrypting the message you desire'''
    def encrypt(self, word):
        global british_alphabet
        ciphertext = []
        for w in word.upper():
            for l in british_alphabet:
                



    def decrypt(self):
        pass
    def proceed(self):
        pass


encryptor = Caesar_Cipher(5)

print(Caesar_Cipher.british_alphabet)


