import random
import string

def encrypt(word):
  words = str(word)
  first_letter = words[0]
  modified_text = (words[1:] + first_letter)
  prefix = ''.join(random.choices(string.ascii_letters +string.digits,k=5))
  suffix = ''.join(random.choices(string.ascii_letters + string.digits,k=5))
  if len(words) < 3:
    words[1:] + words[0]
  else:
    encrypted_word = (prefix+modified_text+suffix)
    return encrypted_word

def decrypt(word):
  words = str(word)
  if len(words) < 3:
    words[-1] + words[::-1]
  else:
    decrypted_word = (words[-6]+words[5:-6])
    return decrypted_word


print(encrypt("yourname"))
print(decrypt ("NfgMDournameyeR54g"))#Enter the encrypted output here to decrypt



