import string
import datetime


class Caesar_Cipher():

    british_alphabet = list(string.ascii_uppercase*2)

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
        ciphertext = []
        for w in word.upper():
            for l in Caesar_Cipher.british_alphabet:
                if w == l:
                    initial_index = Caesar_Cipher.british_alphabet.index(l)
                    final_index = initial_index + self.key
                    ciphertext.append(Caesar_Cipher.british_alphabet[final_index])
                    break
                else:
                    continue
        return ciphertext

    def decrypt(self, ciphertext):
        original_word = []
        for w in ciphertext.upper():
            for l in Caesar_Cipher.british_alphabet:
                if w == l:
                    initial_index = Caesar_Cipher.british_alphabet.index(l)
                    final_index = initial_index - self.key
                    original_word.append(Caesar_Cipher.british_alphabet[final_index])
                    break
                else:
                    continue
        return original_word

    def proceed(self):
        pass


encryptor = Caesar_Cipher(5)

print(encryptor.decrypt())


