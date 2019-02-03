from math import ceil as c

alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'];

#key generation 
def keyGen(ln, key):
    key = key*c(ln/len(key))
    return key[:ln]

#encryption process
def encryptText(msg_ip,keyval):
    encrypt=str()
    for i in range(len(msg_ip)):
        x = (alphabets.index(msg_ip[i])+alphabets.index(keyval[i]))%26
        encrypt+=alphabets[x]
        print(encrypt)
    return encrypt

#decryption process
def decryptText(msg_op, keyval):
        decrypt=str()
        for i in range(len(msg_op)):
                x = (alphabets.index(msg_op[i])-alphabets.index(keyval[i]))%26
                decrypt+=alphabets[x]
                print(decrypt)
        return decrypt


#input message and key
msg_ip = input("Enter text to encrypt\n").lower()
key = input("Enter key string\n").lower()

keyval = keyGen(len(msg_ip),key)
msg_encrypt = encryptText(msg_ip, keyval)

print("\n\n")
print(msg_encrypt)
print("\n\n")

msg_decrypt = decryptText(msg_encrypt,keyval)
print(msg_decrypt)