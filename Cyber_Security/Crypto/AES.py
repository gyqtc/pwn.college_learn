from Crypto.Util.Padding import pad, unpad
from Crypto.Cipher import AES
key = bytes.fromhex('a6a76351b9827f2845600356fe200ede')
print(key)
print(len(key))
cipher = AES.new(key=key, mode=AES.MODE_ECB)
cipher_text = bytes.fromhex('1820bb53116797b791479caceff0cbbc8ba235abb471828d0682e020dfb2148449dfd013e6e54d8acfbf489b3a047696cc1a34775cdffe0f42e12c851fe63bdf')
flag = cipher.decrypt(cipher_text)
print(flag)
